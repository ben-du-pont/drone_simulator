import numpy as np
from typing import List, Dict, Tuple, Optional, Union, Any, Sequence
import logging
from dataclasses import dataclass
from sklearn.mixture import GaussianMixture

# Set up logging
logger = logging.getLogger(__name__)


@dataclass
class MetricsResult:
    """Container for quality metrics of anchor position estimation."""
    gdop: float
    """Geometric Dilution of Precision."""
    
    fim: Optional[np.ndarray] = None
    """Fisher Information Matrix."""
    
    fim_determinant: float = float('inf')
    """Determinant of the FIM; smaller is better."""
    
    condition_number: float = float('inf')
    """Condition number of the estimation matrix."""
    
    mean_residual: float = float('inf')
    """Mean of the absolute residuals."""
    
    median_residual: float = float('inf')
    """Median of the absolute residuals."""
    
    verification_value: float = float('inf')
    """Verification value for internal consistency check."""
    
    covariances: Optional[np.ndarray] = None
    """Covariance values for the position parameters."""
    
    outliers: List[int] = None
    """Indices of detected outliers."""
    
    def __post_init__(self):
        """Initialize derived values and handle missing fields."""
        # Ensure outliers is a list
        if self.outliers is None:
            self.outliers = []
        
        # Calculate FIM determinant if FIM is provided
        if self.fim is not None and self.fim_determinant == float('inf'):
            try:
                self.fim_determinant = np.linalg.det(self.fim)
                if self.fim_determinant <= 0:
                    self.fim_determinant = float('inf')
            except:
                self.fim_determinant = float('inf')


class MetricsCalculator:
    """Calculates quality metrics for anchor position estimation.
    
    This class encapsulates the computation of various metrics used to evaluate
    the quality of anchor position estimates and determine when to stop
    collecting measurements.
    """
    
    def __init__(self, noise_variance: float = 0.4):
        """Initialize the MetricsCalculator.
        
        Args:
            noise_variance: Variance of the measurement noise model for FIM calculation
        """
        self.noise_variance = noise_variance
    
    def compute_metrics(self, 
                       measurements: List[Tuple[float, float, float, float]],
                       estimator: np.ndarray,
                       residuals: Optional[np.ndarray] = None,
                       matrix_a: Optional[np.ndarray] = None) -> MetricsResult:
        """Compute all metrics for an anchor position estimate.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            estimator: Estimated parameters [x, y, z, constant_bias, linear_bias]
            residuals: Optional residuals from the estimation
            matrix_a: Optional matrix A from the linear system
            
        Returns:
            MetricsResult containing all computed metrics
        """
        # Extract position from estimator
        position = estimator[:3]
        
        # Compute GDOP
        gdop = self.compute_gdop(measurements, position)
        
        # Compute FIM
        fim = self.compute_fim(measurements, estimator)
        
        # Compute condition number if matrix_a is provided
        condition_number = float('inf')
        if matrix_a is not None:
            condition_number = self.compute_condition_number(matrix_a)
        
        # Process residuals if provided
        mean_residual = float('inf')
        median_residual = float('inf')
        outliers = []
        
        if residuals is not None:
            mean_residual = float(np.mean(np.abs(residuals)))
            median_residual = float(np.median(np.abs(residuals)))
            outliers = self.identify_outliers(residuals)
        
        # Compute covariances (diagonal elements of position covariance)
        covariances = np.array([float('inf')] * 3)
        
        return MetricsResult(
            gdop=gdop,
            fim=fim,
            condition_number=condition_number,
            mean_residual=mean_residual,
            median_residual=median_residual,
            verification_value=float('inf'),  # Not computed here
            covariances=covariances,
            outliers=outliers
        )
    
    def compute_gdop(self, measurements: List[Tuple[float, float, float, float]], 
                    target_coords: np.ndarray) -> float:
        """Compute the Geometric Dilution of Precision (GDOP).
        
        Lower GDOP values indicate better geometric distributions of measurements
        for accurate position estimation.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            target_coords: Target coordinates [x, y, z]
            
        Returns:
            GDOP value (lower is better)
        """
        if len(measurements) < 4:
            return float('inf')  # Not enough measurements
        
        x, y, z = target_coords
        A = []
        
        for measurement in measurements:
            x_i, y_i, z_i, _ = measurement
            R = np.linalg.norm([x_i - x, y_i - y, z_i - z])
            
            if R < 1e-10:  # Avoid division by zero
                continue
                
            A.append([(x_i - x)/R, (y_i - y)/R, (z_i - z)/R, 1])
        
        if len(A) < 4:
            return float('inf')  # Not enough valid measurements
            
        A = np.array(A)
        
        try:
            # Use SVD for better numerical stability
            u, s, vh = np.linalg.svd(A, full_matrices=False)
            
            # Filter out near-zero singular values
            s_inv = np.zeros_like(s)
            mask = s > 1e-10
            s_inv[mask] = 1.0 / s[mask]
            
            # Compute pseudoinverse and then get trace
            inv_at_a = vh.T @ np.diag(s_inv**2) @ u.T
            return float(np.sqrt(np.trace(inv_at_a)))
            
        except np.linalg.LinAlgError:
            logger.warning("LinAlgError in GDOP computation")
            return float('inf')
    
    def compute_fim(self, measurements: List[Tuple[float, float, float, float]], 
                   target_estimator: np.ndarray) -> np.ndarray:
        """Compute the Fisher Information Matrix (FIM).
        
        The FIM quantifies how much information the measurements provide about the 
        anchor position and bias parameters.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            target_estimator: Target estimator [x, y, z, constant_bias, linear_bias]
            
        Returns:
            FIM matrix (3x3 for position parameters)
        """
        x0, y0, z0 = target_estimator[:3]
        measurements = np.array(measurements)
        
        # Use only position data from measurements
        position_data = measurements[:, :3]
        
        # Compute distances between measurements and target
        z_m = np.linalg.norm(position_data - np.array([x0, y0, z0]), axis=1)
        
        # Ensure no zero distances
        z_m = np.maximum(z_m, 1e-10)
        
        # Differences in x, y, z coordinates
        x_differences = x0 - position_data[:, 0]
        y_differences = y0 - position_data[:, 1]
        z_differences = z0 - position_data[:, 2]
        
        # Compute derivatives
        dzm_dx = x_differences / z_m
        dzm_dy = y_differences / z_m
        dzm_dz = z_differences / z_m
        
        # Create noise covariance matrix
        C_q = self.noise_variance * np.diag((1 + z_m)**2)
        
        try:
            # Invert C_q safely using SVD
            u, s, vh = np.linalg.svd(C_q)
            s_inv = 1.0 / np.maximum(s, 1e-10)
            inv_C_q = vh.T @ np.diag(s_inv) @ u.T
        except np.linalg.LinAlgError:
            # Fallback
            logger.warning("SVD failed in noise covariance inversion")
            C_q_reg = C_q + np.eye(len(C_q)) * 1e-6
            inv_C_q = np.linalg.inv(C_q_reg)
        
        # Compute derivatives of C w.r.t. x, y, and z
        dC_dx = self.noise_variance * np.diag((1 + z_m) / z_m * x_differences)
        dC_dy = self.noise_variance * np.diag((1 + z_m) / z_m * y_differences)
        dC_dz = self.noise_variance * np.diag((1 + z_m) / z_m * z_differences)
        
        # Initialize FIM
        FIM = np.zeros((3, 3))
        
        # Helper function to compute FIM elements
        def compute_fim_element(dzm_a, dzm_b, dC_a, dC_b):
            term1 = dzm_a.T @ inv_C_q @ dzm_b
            term2 = 0.5 * np.trace(inv_C_q @ dC_a @ inv_C_q @ dC_b)
            return term1 + term2
        
        # Compute diagonal terms
        FIM[0, 0] = compute_fim_element(dzm_dx, dzm_dx, dC_dx, dC_dx)
        FIM[1, 1] = compute_fim_element(dzm_dy, dzm_dy, dC_dy, dC_dy)
        FIM[2, 2] = compute_fim_element(dzm_dz, dzm_dz, dC_dz, dC_dz)
        
        # Compute off-diagonal terms
        FIM[0, 1] = compute_fim_element(dzm_dx, dzm_dy, dC_dx, dC_dy)
        FIM[0, 2] = compute_fim_element(dzm_dx, dzm_dz, dC_dx, dC_dz)
        FIM[1, 2] = compute_fim_element(dzm_dy, dzm_dz, dC_dy, dC_dz)
        
        # Fill symmetric part
        FIM[1, 0] = FIM[0, 1]
        FIM[2, 0] = FIM[0, 2]
        FIM[2, 1] = FIM[1, 2]
        
        # Check for NaN or Inf
        if np.any(np.isnan(FIM)) or np.any(np.isinf(FIM)):
            logger.warning("NaN or Inf in FIM matrix")
            FIM = np.nan_to_num(FIM, nan=1e10, posinf=1e10, neginf=-1e10)
        
        return FIM
    
    def compute_condition_number(self, A: np.ndarray) -> float:
        """Compute the condition number of a matrix.
        
        The condition number measures how sensitive the solution of a linear system
        is to errors in the input data. Lower values indicate better numerical stability.
        
        Args:
            A: Matrix to compute condition number for
            
        Returns:
            Condition number of the matrix
        """
        try:
            return float(np.linalg.cond(A))
        except np.linalg.LinAlgError:
            logger.warning("LinAlgError in condition number computation")
            return float('inf')
    
    def compute_mad(self, residuals: np.ndarray) -> float:
        """Compute the Median Absolute Deviation (MAD) of residuals.
        
        MAD is a robust measure of the variability of a univariate sample of quantitative data.
        
        Args:
            residuals: Residual values from the estimation
            
        Returns:
            MAD value
        """
        return float(np.median(np.abs(residuals - np.median(residuals))))
    
    def compute_z_score(self, residuals: np.ndarray) -> np.ndarray:
        """Compute z-scores for residuals.
        
        Z-scores indicate how many standard deviations a value is from the mean.
        
        Args:
            residuals: Residual values from the estimation
            
        Returns:
            Z-scores for each residual
        """
        mean_residuals = np.mean(residuals)
        std_residuals = np.std(residuals)
        
        # Avoid division by zero
        if std_residuals < 1e-10:
            return np.zeros_like(residuals)
            
        return (residuals - mean_residuals) / std_residuals
    
    def identify_outliers(self, residuals: np.ndarray, z_score_threshold: float = 2.0) -> List[int]:
        """Identify outliers in residuals using z-scores.
        
        Args:
            residuals: Residual values from the estimation
            z_score_threshold: Threshold for classifying outliers
            
        Returns:
            List of indices of outliers
        """
        z_scores = self.compute_z_score(residuals)
        outliers = np.where(np.abs(z_scores) > z_score_threshold)[0]
        return outliers.tolist()
    
    def identify_outliers_gmm(self, residuals: np.ndarray, threshold_prob: float = 0.05) -> List[int]:
        """Identify outliers using a Gaussian Mixture Model (GMM).
        
        This method uses a two-component GMM to model the residuals as a mixture
        of "inliers" and "outliers", identifying measurements that are more likely
        to belong to the outlier component.
        
        Args:
            residuals: Residual values from the estimation
            threshold_prob: Probability threshold for classifying outliers
            
        Returns:
            List of indices of outliers
        """
        if len(residuals) < 5:  # Need enough data for GMM to be meaningful
            return []
            
        try:
            # Reshape for GMM
            X = residuals.reshape(-1, 1)
            
            # Fit GMM with 2 components (inliers and outliers)
            gmm = GaussianMixture(n_components=2, random_state=0)
            gmm.fit(X)
            
            # Get component probabilities
            probabilities = gmm.predict_proba(X)
            
            # Determine which component corresponds to outliers (larger variance)
            variances = gmm.covariances_.flatten()
            outlier_idx = np.argmax(variances)
            
            # Identify outliers as points more likely to belong to the outlier component
            outlier_prob = probabilities[:, outlier_idx]
            outliers = np.where(outlier_prob > (1 - threshold_prob))[0]
            
            return outliers.tolist()
            
        except Exception as e:
            logger.warning(f"Error in GMM outlier detection: {e}")
            # Fallback to z-score method
            return self.identify_outliers(residuals)
    
    def check_convergence(self, current_value: float, previous_value: float, 
                         ratio_threshold: float) -> bool:
        """Check if a metric has converged based on relative change.
        
        Args:
            current_value: Current value of the metric
            previous_value: Previous value of the metric
            ratio_threshold: Threshold for relative change
            
        Returns:
            True if the metric has converged, False otherwise
        """
        if np.isinf(previous_value) or np.isnan(previous_value) or previous_value == 0:
            return False
            
        if np.isinf(current_value) or np.isnan(current_value):
            return False
            
        ratio = abs(current_value - previous_value) / abs(previous_value)
        return ratio < ratio_threshold
    
    def check_threshold(self, value: float, threshold: float, lower_is_better: bool = True) -> bool:
        """Check if a metric has reached a threshold value.
        
        Args:
            value: Value of the metric
            threshold: Threshold value
            lower_is_better: Whether lower values are better
            
        Returns:
            True if the metric has reached the threshold, False otherwise
        """
        if np.isinf(value) or np.isnan(value):
            return False
            
        if lower_is_better:
            return value < threshold
        else:
            return value > threshold