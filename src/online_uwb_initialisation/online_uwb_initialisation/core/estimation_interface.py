from abc import ABC, abstractmethod
from typing import List, Dict, Tuple, Optional, Union, Any, Protocol
import numpy as np
import logging
from dataclasses import dataclass, field
from scipy.optimize import least_squares, minimize
from enum import Enum, auto
from sklearn.mixture import GaussianMixture

# Import the EstimationResult
from online_uwb_initialisation.core.estimation_result import EstimationResult

# Set up logging
logger = logging.getLogger(__name__)


class EstimationMethod(Enum):
    """Enumeration of available estimation methods."""
    SIMPLE_LINEAR = auto()
    LINEAR_REWEIGHTED = auto()
    TRIMMED_REWEIGHTED = auto()
    NONLINEAR_LM = auto()
    NONLINEAR_IRLS = auto()
    NONLINEAR_EM = auto()
    NONLINEAR_MM = auto()

@dataclass
class EstimationConfig:
    """Configuration parameters for estimation algorithms."""
    # Linear estimation parameters
    use_linear_bias: bool = True
    """Whether to include linear bias in the estimation"""
    
    use_constant_bias: bool = True
    """Whether to include constant bias in the estimation"""
    
    normalised: bool = False
    """Whether to use the normalised formulation for linear least squares"""
    
    regularise: bool = True
    """Whether to regularize the optimization problem"""
    
    reweighting_iterations: int = 5
    """Number of reweighting iterations for robust estimation"""
    
    # Weighting function parameters
    weighting_function: str = "mad"
    """Weighting function for robust estimation: 'huber', 'tukey', 'geman_mcclure', 'welsch', 'mad'"""
    
    huber_delta: float = 0.01
    """Delta parameter for Huber weighting function"""
    
    tukey_c: float = 4.685
    """C parameter for Tukey weighting function"""
    
    welsch_c: float = 2.0
    """C parameter for Welsch weighting function"""
    
    # Regularization parameters
    position_regularization: float = 0.0
    """Regularization strength for position parameters"""
    
    bias_regularization: float = 1000.0
    """Regularization strength for bias parameters"""
    
    linear_bias_regularization: float = 1000.0
    """Regularization strength for linear bias parameters"""
    
    # Nonlinear optimization parameters
    max_iterations: int = 20
    """Maximum number of iterations for iterative methods"""
    
    tolerance: float = 1e-6
    """Convergence tolerance for iterative methods"""
    
    # EM algorithm parameters
    noise_variance: float = 0.4
    """Noise variance for FIM computation and EM algorithm"""


class EstimationStrategy(ABC):
    """Abstract base class for estimation strategies.
    
    This class defines the interface for all estimation strategies used
    to estimate anchor positions from UWB measurements.
    """
    
    def __init__(self, config: Optional[EstimationConfig] = None):
        """Initialize the estimation strategy.
        
        Args:
            config: Configuration parameters for the estimation strategy
        """
        self.config = config or EstimationConfig()
    
    @abstractmethod
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate the anchor position from measurements.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Optional initial guess for the anchor position and bias terms
            weights: Optional weights for the measurements
            
        Returns:
            EstimationResult containing the estimated position and related metrics
        """
        pass
    
    def setup_linear_least_square(self, measurements: List[Tuple[float, float, float, float]]) -> Tuple[np.ndarray, np.ndarray]:
        """Set up the linear least squares problem.
        
        This method sets up the linear system A * x = b for position estimation.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            
        Returns:
            Tuple of (A, b) matrices for the linear system
        """
        measurements = np.array(measurements)
        
        # Normalized formulation (only works for both biases)
        if self.config.normalised:
            A = []
            b = []

            for measurement in measurements:
                x, y, z, measured_dist = measurement[0:4]
                norm_squared = x**2 + y**2 + z**2
                A.append([2*x, 2*y, 2*z, measured_dist**2, -2*measured_dist, -norm_squared])
                b.append(1)

            return np.array(A), np.array(b)
        
        # Standard formulation with configurable bias terms
        if self.config.use_constant_bias and self.config.use_linear_bias:
            A = []
            b = []
            for measurement in measurements:
                x, y, z, measured_dist = measurement[0:4]
                norm_squared = x**2 + y**2 + z**2
                A.append([2*x, 2*y, 2*z, measured_dist**2, -2*measured_dist, 1])
                b.append(norm_squared)

        elif self.config.use_constant_bias:
            A = []
            b = []
            for measurement in measurements:
                x, y, z, measured_dist = measurement[0:4]
                norm_squared = x**2 + y**2 + z**2
                A.append([-2*x, -2*y, -2*z, 2*measured_dist, 1])
                b.append(measured_dist**2 - norm_squared)

        elif self.config.use_linear_bias:
            A = []
            b = []
            for measurement in measurements:
                x, y, z, measured_dist = measurement[0:4]
                norm_squared = x**2 + y**2 + z**2
                A.append([2*x, 2*y, 2*z, measured_dist**2, 1])
                b.append(norm_squared)

        else:
            A = []
            b = []
            for measurement in measurements:
                x, y, z, measured_dist = measurement[0:4]
                norm_squared = x**2 + y**2 + z**2
                A.append([-2*x, -2*y, -2*z, 1])
                b.append(measured_dist**2 - norm_squared)

        return np.array(A), np.array(b)
    
    def compute_condition_number(self, A: np.ndarray) -> float:
        """Compute the condition number of matrix A.
        
        Args:
            A: Matrix to compute condition number for
            
        Returns:
            Condition number of A
        """
        return np.linalg.cond(A)
    
    def compute_residuals(self, A: np.ndarray, b: np.ndarray, x: np.ndarray) -> np.ndarray:
        """Compute residuals for a linear system.
        
        Args:
            A: Matrix of the linear system
            b: Vector of the linear system
            x: Solution vector
            
        Returns:
            Residuals vector
        """
        return b - A @ x
    
    def compute_covariance_matrix(self, A: np.ndarray, b: np.ndarray, x: np.ndarray, W: Optional[np.ndarray] = None) -> np.ndarray:
        """Compute the covariance matrix for the estimated parameters.
        
        Args:
            A: Matrix of the linear system
            b: Vector of the linear system
            x: Solution vector
            W: Optional diagonal weight matrix
            
        Returns:
            Covariance matrix
        """
        if W is None:
            W = np.eye(A.shape[0])
        
        residuals = self.compute_residuals(A, b, x)
        residual_sum_of_squares = np.sum(residuals**2 * np.diag(W))
        dof = A.shape[0] - A.shape[1]  # Degrees of freedom
        
        if dof <= 0:
            logger.warning("Not enough degrees of freedom for covariance estimation")
            return np.eye(A.shape[1])
        
        sigma_hat_squared = residual_sum_of_squares / dof
        
        try:
            # Use pseudoinverse for better numerical stability
            covariance_matrix = sigma_hat_squared * np.linalg.pinv(A.T @ W @ A)
            return covariance_matrix
        except np.linalg.LinAlgError:
            logger.warning("Error computing covariance matrix, using identity")
            return np.eye(A.shape[1])
    
    def compute_verification_value(self, x: np.ndarray) -> float:
        """Compute verification value for the estimated parameters.
        
        This is an internal consistency check specific to the UWB estimation problem.
        
        Args:
            x: Estimated parameters
            
        Returns:
            Verification value
        """
        if self.config.use_constant_bias and self.config.use_linear_bias:
            x_a, y_a, z_a = x[:3]
            inv_beta_squared = x[3]
            gamma_beta_squared = x[4]
            p_a = x[5]
            
            norm_squared = np.linalg.norm([x_a, y_a, z_a])**2
            verification = p_a - (gamma_beta_squared**2 / inv_beta_squared - norm_squared)
            
        elif self.config.use_constant_bias:
            x_a, y_a, z_a = x[:3]
            gamma = x[3]
            p_a_gamma = x[4]
            
            norm_squared = np.linalg.norm([x_a, y_a, z_a])**2
            verification = p_a_gamma - norm_squared + gamma**2
            
        elif self.config.use_linear_bias:
            x_a, y_a, z_a = x[:3]
            inv_beta_squared = x[3]
            neg_p_a = x[4]
            
            norm_squared = np.linalg.norm([x_a, y_a, z_a])**2
            verification = norm_squared + neg_p_a
            
        else:
            x_a, y_a, z_a = x[:3]
            p_a = x[3]
            
            norm_squared = np.linalg.norm([x_a, y_a, z_a])**2
            verification = p_a - norm_squared
        
        return float(np.abs(verification))
    
    def retrieve_estimator(self, x: np.ndarray) -> np.ndarray:
        """Extract the estimator parameters from the raw solution.
        
        The estimator is a 5-element array: [x, y, z, constant_bias, linear_bias]
        
        Args:
            x: Raw solution from the least squares problem
            
        Returns:
            Estimator parameters [x, y, z, constant_bias, linear_bias]
        """
        if self.config.normalised:
            squared_norm_of_anchor = 1/x[5]
            position = x[:3] * squared_norm_of_anchor
            beta_squared = 1/(x[3]*squared_norm_of_anchor)
            bias = x[4]/x[3]
            linear_bias = (np.sqrt(beta_squared) if beta_squared > 0 else 1)
            return np.array([*position, bias, linear_bias])
            
        if self.config.use_constant_bias and self.config.use_linear_bias:
            squared_linear_bias = x[3] if x[3] > 0 else 1
            linear_bias = np.sqrt(1/squared_linear_bias)
            bias = x[4]/squared_linear_bias
            position = x[:3]
            return np.array([*position, bias, linear_bias])
        
        elif self.config.use_constant_bias:
            position = x[:3]
            bias = x[3]
            return np.array([*position, bias, 1.0])
        
        elif self.config.use_linear_bias:
            squared_linear_bias = x[3] if x[3] > 0 else 1
            linear_bias = np.sqrt(1/squared_linear_bias)
            position = x[:3]
            return np.array([*position, 0.0, linear_bias])
        
        else:
            position = x[:3]
            return np.array([*position, 0.0, 1.0])
    
    def update_weights(self, residuals: np.ndarray) -> np.ndarray:
        """Update weights for robust estimation based on residuals.
        
        Args:
            residuals: Residuals from the previous estimation iteration
            
        Returns:
            Updated weights for each measurement
        """
        def compute_mad_scale(residuals: np.ndarray) -> float:
            """Compute scale based on Median Absolute Deviation."""
            mad = np.median(np.abs(residuals - np.median(residuals)))
            return mad / 0.6745
        
        # Get the scale for the residuals
        scale = compute_mad_scale(residuals)
        if scale < 1e-10:  # Avoid division by zero
            scale = 1.0
        
        # Apply the selected weighting function
        if self.config.weighting_function == 'huber':
            delta = self.config.huber_delta
            weights = np.where(np.abs(residuals) <= delta, 
                             1, 
                             delta / np.abs(residuals))
            
        elif self.config.weighting_function == 'tukey':
            c = self.config.tukey_c
            scaled_residuals = residuals / scale
            weights = np.where(np.abs(scaled_residuals) <= c, 
                             (1 - (scaled_residuals/c)**2)**2, 
                             0)
            
        elif self.config.weighting_function == 'geman_mcclure':
            scaled_residuals = residuals / scale
            weights = 1 / (1 + scaled_residuals**2)
            
        elif self.config.weighting_function == 'welsch':
            c = self.config.welsch_c
            scaled_residuals = residuals / scale
            weights = np.exp(-0.5 * (scaled_residuals/c)**2)
            
        elif self.config.weighting_function == 'mad':
            c = self.config.tukey_c
            scaled_residuals = residuals / scale
            weights_tukey = np.where(np.abs(scaled_residuals) <= c, 
                                   (1 - (scaled_residuals/c)**2)**2, 
                                   0)
            # Avoid division by zero
            weights = np.where(np.abs(scaled_residuals) < 1e-10, 
                             1.0, 
                             weights_tukey / np.abs(scaled_residuals))
        else:
            # Default to inverse squared residuals
            weights = 1 / np.maximum(residuals**2, 1e-8)
        
        return weights
    
    def compute_gdop(self, measurements: List[Tuple[float, float, float, float]], target_coords: np.ndarray) -> float:
        """Compute the Geometric Dilution of Precision.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            target_coords: Target coordinates [x, y, z]
            
        Returns:
            GDOP value
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
            return np.sqrt(np.trace(inv_at_a))
            
        except np.linalg.LinAlgError:
            return float('inf')
    
    def compute_fim(self, measurements: List[Tuple[float, float, float, float]], target_estimator: np.ndarray) -> np.ndarray:
        """Compute the Fisher Information Matrix.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            target_estimator: Target estimator [x, y, z, constant_bias, linear_bias]
            
        Returns:
            FIM matrix
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
        C_q = self.config.noise_variance * np.diag((1 + z_m)**2)
        
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
        dC_dx = self.config.noise_variance * np.diag((1 + z_m) / z_m * x_differences)
        dC_dy = self.config.noise_variance * np.diag((1 + z_m) / z_m * y_differences)
        dC_dz = self.config.noise_variance * np.diag((1 + z_m) / z_m * z_differences)
        
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


class SimpleLinearEstimation(EstimationStrategy):
    """Simple linear least squares estimation strategy."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate anchor position using simple linear least squares.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Not used in this method, included for API consistency
            weights: Not used in this method, included for API consistency
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        # Set up the linear system
        A, b = self.setup_linear_least_square(measurements)
        
        # Compute condition number
        condition_number = self.compute_condition_number(A)
        
        # Solve the linear system
        try:
            x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        except np.linalg.LinAlgError:
            logger.warning("LinAlgError in linear least squares, using pseudoinverse")
            x = np.linalg.pinv(A) @ b
            residuals = self.compute_residuals(A, b, x)
            
        # Compute covariance matrix
        covariance_matrix = self.compute_covariance_matrix(A, b, x)
        
        # Retrieve estimator [x, y, z, constant_bias, linear_bias]
        estimator = self.retrieve_estimator(x)
        
        # Compute verification value
        verification_value = self.compute_verification_value(x)
        
        # Compute GDOP
        gdop = self.compute_gdop(measurements, estimator[:3])
        
        # Compute FIM
        fim = self.compute_fim(measurements, estimator)
        
        # Create and return the estimation result
        return EstimationResult(
            estimator=estimator,
            covariance_matrix=covariance_matrix,
            residuals=self.compute_residuals(A, b, x),
            raw_params=x,
            condition_number=condition_number,
            verification_value=verification_value,
            gdop=gdop,
            fim=fim,
            is_nonlinear=False
        )


class LinearReweightedEstimation(EstimationStrategy):
    """Robust linear least squares estimation using iterative reweighting."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate anchor position using iteratively reweighted least squares.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Not used in this method, included for API consistency
            weights: Optional initial weights for the measurements
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        # Set up the linear system
        A, b = self.setup_linear_least_square(measurements)
        
        # Compute condition number
        condition_number = self.compute_condition_number(A)
        
        # Initialize weights if not provided
        if weights is None or len(weights) != len(measurements):
            weights = np.ones(len(measurements))
        else:
            weights = np.array(weights)
        
        # Perform iterative reweighted least squares
        for iteration in range(self.config.reweighting_iterations):
            # Create the weight matrix
            W = np.diag(weights)
            
            # Set up regularization if enabled
            if self.config.regularise:
                # Create regularization matrix based on parameter types
                reg_matrix = np.zeros((A.shape[1], A.shape[1]))
                
                # Apply regularization based on parameter type
                if self.config.use_constant_bias and self.config.use_linear_bias:
                    # Position parameters
                    reg_matrix[:3, :3] = np.eye(3) * self.config.position_regularization
                    # Bias parameters
                    reg_matrix[3, 3] = self.config.linear_bias_regularization
                    reg_matrix[4, 4] = self.config.bias_regularization
                elif self.config.use_constant_bias:
                    # Position parameters
                    reg_matrix[:3, :3] = np.eye(3) * self.config.position_regularization
                    # Bias parameter
                    reg_matrix[3, 3] = self.config.bias_regularization
                elif self.config.use_linear_bias:
                    # Position parameters
                    reg_matrix[:3, :3] = np.eye(3) * self.config.position_regularization
                    # Linear bias parameter
                    reg_matrix[3, 3] = self.config.linear_bias_regularization
                
                # Solve the regularized weighted least squares problem
                # (A^T W A + λ I)^{-1} A^T W b
                try:
                    x = np.linalg.pinv(A.T @ W @ A + reg_matrix) @ (A.T @ W @ b)
                except np.linalg.LinAlgError:
                    logger.warning("LinAlgError in regularized weighted least squares")
                    # Fall back to simple least squares
                    x = np.linalg.pinv(A) @ b
            else:
                # Solve the weighted least squares problem
                # (A^T W A)^{-1} A^T W b
                try:
                    x = np.linalg.pinv(A.T @ W @ A) @ (A.T @ W @ b)
                except np.linalg.LinAlgError:
                    logger.warning("LinAlgError in weighted least squares")
                    # Fall back to simple least squares
                    x = np.linalg.pinv(A) @ b
            
            # Compute residuals
            residuals = self.compute_residuals(A, b, x)
            
            # Update weights for next iteration
            weights = self.update_weights(residuals)
        
        # Compute final covariance matrix
        covariance_matrix = self.compute_covariance_matrix(A, b, x, W)
        
        # Retrieve estimator [x, y, z, constant_bias, linear_bias]
        estimator = self.retrieve_estimator(x)
        
        # Compute verification value
        verification_value = self.compute_verification_value(x)
        
        # Compute GDOP
        gdop = self.compute_gdop(measurements, estimator[:3])
        
        # Compute FIM
        fim = self.compute_fim(measurements, estimator)
        
        # Create and return the estimation result
        return EstimationResult(
            estimator=estimator,
            covariance_matrix=covariance_matrix,
            residuals=residuals,
            raw_params=x,
            condition_number=condition_number,
            verification_value=verification_value,
            gdop=gdop,
            fim=fim,
            is_nonlinear=False,
            iteration_count=self.config.reweighting_iterations
        )


class TrimmedReweightedEstimation(EstimationStrategy):
    """Robust linear least squares with iterative reweighting and trimming."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None,
                trim_fraction: float = 0.1) -> EstimationResult:
        """Estimate anchor position using trimmed iteratively reweighted least squares.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Not used in this method, included for API consistency
            weights: Optional initial weights for the measurements
            trim_fraction: Fraction of measurements to trim (e.g., 0.1 for 10%)
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        # First perform standard reweighted estimation
        reweighted_estimator = LinearReweightedEstimation(self.config)
        result = reweighted_estimator.estimate(measurements, initial_guess, weights)
        
        # Get the weights for trimming
        weights = result.residuals.copy()
        weights = self.update_weights(weights)
        
        # Set up the linear system
        A, b = self.setup_linear_least_square(measurements)
        
        # Compute threshold for trimming
        threshold = np.percentile(weights, 100 * (1 - trim_fraction))
        
        # Create mask for trimming
        mask = weights > threshold
        
        # Skip trimming if we would remove too many measurements
        if np.sum(mask) < 4:  # Need at least 4 measurements
            logger.warning("Not enough measurements after trimming, using all measurements")
            return result
        
        # Apply mask to A, b, and weights
        A_trimmed = A[mask]
        b_trimmed = b[mask]
        weights_trimmed = weights[mask]
        
        # Create weight matrix
        W = np.diag(weights_trimmed)
        
        # Compute condition number of trimmed matrix
        condition_number = self.compute_condition_number(A_trimmed)
        
        # Set up regularization if enabled
        if self.config.regularise:
            # Create regularization matrix based on parameter types
            reg_matrix = np.zeros((A_trimmed.shape[1], A_trimmed.shape[1]))
            
            # Apply regularization based on parameter type
            if self.config.use_constant_bias and self.config.use_linear_bias:
                # Position parameters
                reg_matrix[:3, :3] = np.eye(3) * self.config.position_regularization
                # Bias parameters
                reg_matrix[3, 3] = self.config.linear_bias_regularization
                reg_matrix[4, 4] = self.config.bias_regularization
            elif self.config.use_constant_bias:
                # Position parameters
                reg_matrix[:3, :3] = np.eye(3) * self.config.position_regularization
                # Bias parameter
                reg_matrix[3, 3] = self.config.bias_regularization
            elif self.config.use_linear_bias:
                # Position parameters
                reg_matrix[:3, :3] = np.eye(3) * self.config.position_regularization
                # Linear bias parameter
                reg_matrix[3, 3] = self.config.linear_bias_regularization
            
            # Solve the regularized weighted least squares problem
            # (A^T W A + λ I)^{-1} A^T W b
            try:
                x = np.linalg.pinv(A_trimmed.T @ W @ A_trimmed + reg_matrix) @ (A_trimmed.T @ W @ b_trimmed)
            except np.linalg.LinAlgError:
                logger.warning("LinAlgError in regularized weighted least squares")
                # Fall back to untrimmed result
                return result
        else:
            # Solve the weighted least squares problem
            # (A^T W A)^{-1} A^T W b
            try:
                x = np.linalg.pinv(A_trimmed.T @ W @ A_trimmed) @ (A_trimmed.T @ W @ b_trimmed)
            except np.linalg.LinAlgError:
                logger.warning("LinAlgError in weighted least squares")
                # Fall back to untrimmed result
                return result
        
        # Compute residuals for all measurements using the trimmed solution
        residuals = self.compute_residuals(A, b, x)
        
        # Compute covariance matrix
        covariance_matrix = self.compute_covariance_matrix(A_trimmed, b_trimmed, x, W)
        
        # Retrieve estimator [x, y, z, constant_bias, linear_bias]
        estimator = self.retrieve_estimator(x)
        
        # Compute verification value
        verification_value = self.compute_verification_value(x)
        
        # Find outliers (points that were trimmed)
        outliers = np.where(~mask)[0].tolist()
        
        # Compute GDOP
        gdop = self.compute_gdop(measurements, estimator[:3])
        
        # Compute FIM
        fim = self.compute_fim(measurements, estimator)
        
        # Create and return the estimation result
        return EstimationResult(
            estimator=estimator,
            covariance_matrix=covariance_matrix,
            residuals=residuals,
            raw_params=x,
            condition_number=condition_number,
            verification_value=verification_value,
            gdop=gdop,
            fim=fim,
            outliers=outliers,
            is_nonlinear=False,
            iteration_count=self.config.reweighting_iterations
        )





class NonlinearLMEstimation(EstimationStrategy):
    """Nonlinear least squares estimation using Levenberg-Marquardt algorithm."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate anchor position using nonlinear Levenberg-Marquardt optimization.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Initial guess for the anchor position and bias terms
            weights: Not used directly, included for API consistency
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        measurements = np.array(measurements)
        
        # Use default initial guess if not provided
        if initial_guess is None or len(initial_guess) != 5:
            initial_guess = np.array([0.0, 0.0, 0.0, 0.0, 1.0])
        
        # Define the loss function and its Jacobian
        def loss_function(x):
            """Calculate residuals for all measurements."""
            anchor_pos = x[0:3]
            bias = x[3]
            linear_bias = x[4]
            
            residuals = []
            for measurement in measurements:
                drone_pos = measurement[0:3]
                measured_dist = measurement[3]
                
                # Calculate true distance
                true_dist = np.linalg.norm(anchor_pos - drone_pos)
                
                # Calculate expected measurement with bias terms
                expected_dist = true_dist * linear_bias + bias
                
                # Calculate residual
                residual = expected_dist - measured_dist
                residuals.append(residual)
                
            return np.array(residuals)
        
        def jacobian(x):
            """Calculate the Jacobian matrix."""
            anchor_pos = x[0:3]
            bias = x[3]
            linear_bias = x[4]
            
            J = np.zeros((len(measurements), 5))
            
            for i, measurement in enumerate(measurements):
                drone_pos = measurement[0:3]
                
                # Vector from drone to anchor
                diff_vector = anchor_pos - drone_pos
                
                # True distance
                true_dist = np.linalg.norm(diff_vector)
                
                if true_dist > 1e-10:  # Avoid division by zero
                    # Derivatives with respect to anchor position
                    J[i, 0:3] = linear_bias * diff_vector / true_dist
                    
                    # Derivative with respect to bias
                    J[i, 3] = 1.0
                    
                    # Derivative with respect to linear bias
                    J[i, 4] = true_dist
                else:
                    # Handle the case where drone and anchor are very close
                    J[i, 0:3] = 0.0
                    J[i, 3] = 1.0
                    J[i, 4] = 0.0
                    
            return J
                
        # Perform the optimization
        try:
            result = least_squares(
                loss_function,
                initial_guess,
                jac=jacobian,
                method='lm',
                ftol=self.config.tolerance,
                xtol=self.config.tolerance,
                max_nfev=self.config.max_iterations
            )
            
            # Extract the solution
            x = result.x
            converged = result.success
            iteration_count = result.nfev
            
            # Calculate residuals
            residuals = loss_function(x)
            
            # Calculate Jacobian at solution
            J = jacobian(x)
            
            # Calculate covariance matrix
            # C = (J^T J)^{-1} σ²
            try:
                residual_sum_of_squares = np.sum(residuals**2)
                dof = len(measurements) - len(x)
                
                if dof > 0:
                    sigma_squared = residual_sum_of_squares / dof
                    covariance_matrix = sigma_squared * np.linalg.pinv(J.T @ J)
                else:
                    logger.warning("Not enough degrees of freedom for covariance estimation")
                    covariance_matrix = np.eye(len(x))
            except np.linalg.LinAlgError:
                logger.warning("Error computing covariance matrix in nonlinear estimation")
                covariance_matrix = np.eye(len(x))
            
            # Compute GDOP
            gdop = self.compute_gdop(measurements, x[:3])
            
            # Compute FIM
            fim = self.compute_fim(measurements, x)
            
            # Create the estimation result
            return EstimationResult(
                estimator=x,
                covariance_matrix=covariance_matrix,
                residuals=residuals,
                raw_params=x,
                condition_number=float('inf'),  # Not directly applicable for nonlinear estimation
                verification_value=float('inf'),  # Not directly applicable for nonlinear estimation
                gdop=gdop,
                fim=fim,
                is_nonlinear=True,
                iteration_count=iteration_count,
                converged=converged
            )
            
        except Exception as e:
            logger.error(f"Error in nonlinear LM estimation: {e}")
            # Fall back to linear estimation
            linear_estimator = LinearReweightedEstimation(self.config)
            result = linear_estimator.estimate(measurements.tolist(), initial_guess, weights)
            result.is_nonlinear = False
            result.converged = False
            return result


class NonlinearIRLSEstimation(EstimationStrategy):
    """Nonlinear estimation using Iteratively Reweighted Least Squares."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate anchor position using nonlinear IRLS optimization.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Initial guess for the anchor position and bias terms
            weights: Initial weights for the measurements (optional)
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        measurements = np.array(measurements)
        
        # Use default initial guess if not provided
        if initial_guess is None or len(initial_guess) != 5:
            initial_guess = np.array([0.0, 0.0, 0.0, 0.0, 1.0])
        
        # Make a copy of the initial guess to avoid modifying the original
        params = np.array(initial_guess, dtype=float)
        
        # Define the loss function and Jacobian
        def loss_function(params, measurements):
            """Calculate residuals for all measurements."""
            x_a, y_a, z_a, gamma, beta = params
            anchor_pos = np.array([x_a, y_a, z_a])
            
            residuals = []
            for measurement in measurements:
                drone_pos = measurement[0:3]
                measured_dist = measurement[3]
                
                # Calculate true distance
                true_dist = np.linalg.norm(anchor_pos - drone_pos)
                
                # Calculate expected measurement with bias terms
                expected_dist = beta * true_dist + gamma
                
                # Calculate residual
                residual = measured_dist - expected_dist
                residuals.append(residual)
                
            return np.array(residuals)
        
        def jacobian(params, measurements):
            """Calculate the Jacobian matrix."""
            x_a, y_a, z_a, gamma, beta = params
            anchor_pos = np.array([x_a, y_a, z_a])
            
            J = []
            for measurement in measurements:
                drone_pos = measurement[0:3]
                
                # Vector from drone to anchor
                diff_vector = anchor_pos - drone_pos
                
                # True distance
                true_dist = np.linalg.norm(diff_vector)
                
                if true_dist > 1e-10:  # Avoid division by zero
                    # Derivatives with respect to anchor position
                    dx = -beta * diff_vector[0] / true_dist
                    dy = -beta * diff_vector[1] / true_dist
                    dz = -beta * diff_vector[2] / true_dist
                    
                    # Derivative with respect to bias
                    dgamma = -1.0
                    
                    # Derivative with respect to linear bias
                    dbeta = -true_dist
                    
                    J.append([dx, dy, dz, dgamma, dbeta])
                else:
                    # Handle the case where drone and anchor are very close
                    J.append([0.0, 0.0, 0.0, -1.0, 0.0])
                    
            return np.array(J)
        
        def compute_scale(residuals):
            """Compute robust scale estimate using Median Absolute Deviation."""
            mad = np.median(np.abs(residuals - np.median(residuals)))
            return 1.4826 * mad  # Consistent with normal distribution
        
        # IRLS iterations
        converged = False
        iteration_count = 0
        best_residuals = None
        
        for iteration in range(self.config.max_iterations):
            # Compute current residuals
            residuals = loss_function(params, measurements)
            
            # Save residuals for output
            best_residuals = residuals.copy()
            
            # Compute scale
            scale = compute_scale(residuals)
            if scale < 1e-10:
                scale = 1.0  # Avoid division by zero
                
            # Compute weights using Huber function
            weights = np.where(
                np.abs(residuals / scale) <= 1.345,  # Standard Huber constant
                1.0,
                1.345 * scale / np.abs(residuals)
            )
            
            # Apply weights to residuals for weighted optimization
            sqrt_weights = np.sqrt(weights)
            
            # Solve the weighted least squares problem
            try:
                result = least_squares(
                    lambda p: sqrt_weights * loss_function(p, measurements),
                    params,
                    jac=lambda p: sqrt_weights[:, np.newaxis] * jacobian(p, measurements),
                    method='lm',
                    ftol=self.config.tolerance,
                    xtol=self.config.tolerance
                )
                
                new_params = result.x
                
                # Check for convergence
                if np.linalg.norm(new_params - params) < self.config.tolerance:
                    converged = True
                    params = new_params
                    break
                    
                params = new_params
                iteration_count += 1
                
            except Exception as e:
                logger.warning(f"Error in IRLS iteration {iteration}: {e}")
                break
        
        if best_residuals is None:
            best_residuals = loss_function(params, measurements)
            
        # Compute final Jacobian and covariance matrix
        try:
            J = jacobian(params, measurements)
            residual_sum_of_squares = np.sum(best_residuals**2)
            dof = len(measurements) - len(params)
            
            if dof > 0:
                sigma_squared = residual_sum_of_squares / dof
                covariance_matrix = sigma_squared * np.linalg.pinv(J.T @ J)
            else:
                covariance_matrix = np.eye(len(params))
        except np.linalg.LinAlgError:
            covariance_matrix = np.eye(len(params))
        
        # Compute GDOP
        gdop = self.compute_gdop(measurements, params[:3])
        
        # Compute FIM
        fim = self.compute_fim(measurements, params)
        
        # Create the estimation result
        return EstimationResult(
            estimator=params,
            covariance_matrix=covariance_matrix,
            residuals=best_residuals,
            raw_params=params,
            condition_number=float('inf'),  # Not directly applicable
            verification_value=float('inf'),  # Not directly applicable
            gdop=gdop,
            fim=fim,
            is_nonlinear=True,
            iteration_count=iteration_count,
            converged=converged
        )


class NonlinearEMEstimation(EstimationStrategy):
    """Nonlinear estimation using Expectation-Maximization algorithm."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate anchor position using EM algorithm.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Initial guess for the anchor position and bias terms
            weights: Not used in this method, included for API consistency
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        measurements = np.array(measurements)
        
        # Use default initial guess if not provided
        if initial_guess is None or len(initial_guess) != 5:
            initial_guess = np.array([0.0, 0.0, 0.0, 0.0, 1.0])
            
        # Initialize with linear least squares if initial_guess is all zeros
        if np.all(np.abs(initial_guess) < 1e-6):
            linear_estimator = LinearReweightedEstimation(self.config)
            linear_result = linear_estimator.estimate(measurements.tolist())
            initial_guess = linear_result.estimator
            
        def gaussian_likelihood_log(residuals, sigma, mu, eps=1e-6):
            """Log of Gaussian likelihood for numerical stability."""
            return -0.5 * np.log(2 * np.pi * (sigma + eps)**2) - 0.5 * ((residuals - mu) / (sigma + eps))**2
        
        def compute_residuals(params, measurements):
            """Compute residuals for the given parameters."""
            object_pos = params[:3]
            
            residuals = []
            for measurement in measurements:
                drone_pos = measurement[:3]
                measured_dist = measurement[3]
                
                # Calculate true distance
                true_dist = np.linalg.norm(drone_pos - object_pos)
                
                # Calculate residual (we'll model biases in the GMM)
                residual = measured_dist - true_dist
                residuals.append(residual)
                
            return np.array(residuals)
        
        # Identify possible outliers for initial GMM parameters
        initial_residuals = compute_residuals(initial_guess[:3], measurements)
        
        # Find outliers using z-score
        mean_res = np.mean(initial_residuals)
        std_res = np.std(initial_residuals)
        z_scores = np.abs((initial_residuals - mean_res) / std_res)
        outlier_mask = z_scores > 2.0
        
        # Set initial GMM parameters
        if np.any(outlier_mask):
            pi_los = 1.0 - np.sum(outlier_mask) / len(measurements)
            mu_los = np.mean(initial_residuals[~outlier_mask])
            mu_nlos = np.mean(initial_residuals[outlier_mask])
            sigma_los = np.std(initial_residuals[~outlier_mask])
            sigma_nlos = np.std(initial_residuals[outlier_mask])
        else:
            pi_los = 0.9  # Default: expect 90% line-of-sight measurements
            mu_los = 0.0  # Default: expect no bias in LOS
            mu_nlos = 3.0  # Default: expect positive bias in NLOS
            sigma_los = 0.1  # Default: small variance for LOS
            sigma_nlos = 1.0  # Default: larger variance for NLOS
        
        # Fix numerical issues
        sigma_los = max(sigma_los, 0.01)
        sigma_nlos = max(sigma_nlos, 0.02)
        pi_los = np.clip(pi_los, 0.5, 0.99)
        
        # GMM likelihood function for optimization
        def gmm_objective(params):
            # Extract anchor position
            object_pos = params[:3]
            
            # Compute residuals
            residuals = compute_residuals(object_pos, measurements)
            
            # GMM log-likelihood calculation
            los_log_prob = np.log(pi_los) + gaussian_likelihood_log(residuals, sigma_los, mu_los)
            nlos_log_prob = np.log(1 - pi_los) + gaussian_likelihood_log(residuals, sigma_nlos, mu_nlos)
            
            # Use log-sum-exp trick for numerical stability
            log_likelihood = np.sum(np.logaddexp(los_log_prob, nlos_log_prob))
            
            # Return negative log-likelihood for minimization
            return -log_likelihood
            
        # Perform EM iterations
        converged = False
        iteration_count = 0
        current_position = initial_guess[:3]
        
        for iteration in range(self.config.max_iterations):
            # E-step: compute responsibilities
            residuals = compute_residuals(current_position, measurements)
            
            # Compute component likelihoods
            los_likelihood = pi_los * np.exp(gaussian_likelihood_log(residuals, sigma_los, mu_los))
            nlos_likelihood = (1 - pi_los) * np.exp(gaussian_likelihood_log(residuals, sigma_nlos, mu_nlos))
            
            # Compute responsibilities (normalized likelihoods)
            total_likelihood = los_likelihood + nlos_likelihood + 1e-10  # Avoid division by zero
            responsibilities_los = los_likelihood / total_likelihood
            
            # M-step part 1: update GMM parameters
            pi_los = np.mean(responsibilities_los)
            pi_los = np.clip(pi_los, 0.5, 0.99)  # Constrain pi_los
            
            # Update component means and variances
            if np.sum(responsibilities_los) > 0:
                mu_los = np.sum(responsibilities_los * residuals) / np.sum(responsibilities_los)
                mu_nlos = np.sum((1 - responsibilities_los) * residuals) / np.sum(1 - responsibilities_los)
                
                sigma_los = np.sqrt(np.sum(responsibilities_los * (residuals - mu_los)**2) / np.sum(responsibilities_los))
                sigma_nlos = np.sqrt(np.sum((1 - responsibilities_los) * (residuals - mu_nlos)**2) / np.sum(1 - responsibilities_los))
                
                # Constrain variances to avoid numerical issues
                sigma_los = max(sigma_los, 0.01)
                sigma_nlos = max(sigma_nlos, 0.02)
            
            # M-step part 2: update position estimate
            # Use responsibilities as weights for position estimation
            try:
                result = minimize(
                    gmm_objective,
                    current_position,
                    method='L-BFGS-B',
                    options={'ftol': 1e-5, 'gtol': 1e-5}
                )
                
                new_position = result.x
                
                # Check for convergence
                if np.linalg.norm(new_position - current_position) < self.config.tolerance:
                    converged = True
                    current_position = new_position
                    break
                
                current_position = new_position
                iteration_count += 1
                
            except Exception as e:
                logger.warning(f"Error in EM iteration {iteration}: {e}")
                break
        
        # Final residuals
        final_residuals = compute_residuals(current_position, measurements)
        
        # Compute component probabilities for final classification
        los_prob = pi_los * np.exp(gaussian_likelihood_log(final_residuals, sigma_los, mu_los))
        nlos_prob = (1 - pi_los) * np.exp(gaussian_likelihood_log(final_residuals, sigma_nlos, mu_nlos))
        
        # Classify outliers
        outliers = np.where(nlos_prob > los_prob)[0].tolist()
        
        # Create covariance matrix
        # For simplicity, use a diagonal covariance matrix based on component variances
        # weighted by responsibilities
        responsibilities_los = los_prob / (los_prob + nlos_prob + 1e-10)
        weighted_variance = np.mean(responsibilities_los * sigma_los**2 + (1 - responsibilities_los) * sigma_nlos**2)
        
        covariance_matrix = np.eye(5)
        covariance_matrix[:3, :3] *= weighted_variance
        
        # Compute GDOP
        gdop = self.compute_gdop(measurements, current_position)
        
        # Compute FIM
        fim = self.compute_fim(measurements, np.array([*current_position, 0.0, 1.0]))
        
        # Create estimator with position and default bias terms
        # (biases were modeled in the GMM component means)
        estimator = np.array([
            current_position[0],
            current_position[1],
            current_position[2],
            mu_los,  # Use LOS mean as constant bias
            1.0      # Default linear bias
        ])
        
        # Create the estimation result
        return EstimationResult(
            estimator=estimator,
            covariance_matrix=covariance_matrix,
            residuals=final_residuals,
            raw_params=np.array([*current_position, mu_los, mu_nlos, sigma_los, sigma_nlos, pi_los]),
            condition_number=float('inf'),  # Not applicable for EM
            verification_value=float('inf'),  # Not applicable for EM
            gdop=gdop,
            fim=fim,
            outliers=outliers,
            is_nonlinear=True,
            iteration_count=iteration_count,
            converged=converged
        )
    
class NonlinearMMEstimation(EstimationStrategy):
    """Nonlinear estimation using Mixture Model with distance-dependent noise."""
    
    def estimate(self, measurements: List[Tuple[float, float, float, float]], 
                initial_guess: Optional[np.ndarray] = None,
                weights: Optional[List[float]] = None) -> EstimationResult:
        """Estimate anchor position using mixture model optimization.
        
        Args:
            measurements: List of measurements, each as a tuple (x, y, z, distance)
            initial_guess: Initial guess for the anchor position and bias terms
            weights: Not used in this method, included for API consistency
            
        Returns:
            EstimationResult with the estimated position and related metrics
        """
        measurements = np.array(measurements)
        
        # Use default initial guess if not provided
        if initial_guess is None or len(initial_guess) != 5:
            initial_guess = np.array([0.0, 0.0, 0.0, 0.0, 1.0])
        
        def gaussian_likelihood_log(residuals: np.ndarray, sigma: np.ndarray, mu: float, eps: float = 1e-6) -> np.ndarray:
            """Compute log of Gaussian likelihood for numerical stability.
            
            Args:
                residuals: Array of residuals
                sigma: Array of standard deviations
                mu: Mean value
                eps: Small value to prevent division by zero
                
            Returns:
                Array of log-likelihoods
            """
            return -0.5 * np.log(2 * np.pi * (sigma + eps)**2) - 0.5 * ((residuals - mu) / (sigma + eps))**2
        
        def compute_residuals(params: np.ndarray, measurements: np.ndarray) -> np.ndarray:
            """Compute measurement residuals.
            
            Args:
                params: Parameter vector [x, y, z, gamma, beta]
                measurements: Array of measurements
                
            Returns:
                Array of residuals
            """
            object_pos = params[:3]
            gamma = params[3]
            beta = params[4]
            
            distances = np.linalg.norm(measurements[:, :3] - object_pos, axis=1)
            return measurements[:, 3] - distances * beta - gamma
        
        def compute_z_score(residuals):
            """Compute the z-score of the residuals from the linear least squares problem
            
            Parameters:
            - residuals: numpy array, the residuals of the linear least squares problem
            
            Returns:
            - z_scores: numpy array, the computed z-scores
            """
            
            mean_residuals = np.mean(residuals)
            std_residuals = np.std(residuals)
            z_scores = (residuals - mean_residuals) / std_residuals

            return z_scores
    
        def outlier_finder(residuals):
            """Find the outliers in the residuals using the z-score method
            
            Parameters:
            - residuals: numpy array, the residuals of the linear least squares problem
            
            Returns:
            - outliers: numpy array, the indices of the outliers in the residuals
            """

            threshold = 2.0

            z_score = compute_z_score(residuals)

            outliers = np.where(np.abs(z_score) > threshold)[0]
            return outliers
    
        def gmm_likelihood_distance_dependent(params: np.ndarray, measurements: np.ndarray) -> float:
            """Compute negative log-likelihood for the mixture model.
            
            Args:
                params: Parameter vector containing position and mixture model parameters
                measurements: Array of measurements
                
            Returns:
                Negative log-likelihood value
            """
            # Extract parameters
            object_pos = params[:3]
            pi_los = np.clip(params[3], 0.001, 0.999)
            sigma_0_los, alpha_los = params[4:6]
            sigma_0_nlos, alpha_nlos = params[6:8]
            mu_los, mu_nlos = params[8:10]
            
            # Compute distances and residuals
            distances = np.linalg.norm(measurements[:, :3] - object_pos, axis=1)
            ranges = measurements[:, 3]
            residuals_los = ranges - distances
            residuals_nlos = ranges - distances
            
            # Distance-dependent noise models
            sigma_los = sigma_0_los + alpha_los * distances
            sigma_nlos = sigma_0_nlos + alpha_nlos * distances
            
            # Compute component log-probabilities
            los_log_prob = np.log(pi_los) + gaussian_likelihood_log(residuals_los, sigma_los, mu_los)
            nlos_log_prob = np.log(1 - pi_los) + gaussian_likelihood_log(residuals_nlos, sigma_nlos, mu_nlos)
            
            # Compute total log-likelihood with regularization
            log_likelihood = np.sum(np.logaddexp(los_log_prob, nlos_log_prob))
            regularization = np.sum(np.maximum(0, sigma_los - sigma_nlos))
            
            return -(log_likelihood - regularization)
        
        # Initialize mixture model parameters using initial residuals
        residuals = compute_residuals(initial_guess, measurements)
        outliers = outlier_finder(residuals)
        outlier_mask = np.zeros(len(residuals), dtype=bool)
        outlier_mask[outliers] = True
        
        # Compute initial statistics
        if len(outliers) > 0:
            mu_los = np.mean(residuals[~outlier_mask])
            mu_nlos = np.mean(residuals[outlier_mask])
            sigma_los = np.std(residuals[~outlier_mask])
            sigma_nlos = np.std(residuals[outlier_mask])
            pi_los = 1 - len(outliers) / len(measurements)
        else:
            mu_los = np.mean(residuals)
            mu_nlos = mu_los
            sigma_los = np.std(residuals)
            sigma_nlos = sigma_los
            pi_los = 1.0
        
        # Set up initial parameters for optimization
        initial_params = np.array([
            *initial_guess[:3],  # position
            pi_los,             # mixing weight
            sigma_los, 0.0,     # LOS noise parameters
            sigma_nlos, 0.0,    # NLOS noise parameters
            mu_los, mu_nlos     # component means
        ])
        
        # Define optimization bounds
        bounds = [
            (None, None), (None, None), (None, None),  # position
            (0.7, 0.999),                              # pi_los
            (0.01, None), (0.0, None),                 # LOS noise
            (0.01, None), (0.0, None),                 # NLOS noise
            (-0.5, 0.5), (-2.0, 2.0)                   # means
        ]
        
        # Perform optimization
        try:
            result = minimize(
                gmm_likelihood_distance_dependent,
                initial_params,
                args=(measurements,),
                method='L-BFGS-B',
                bounds=bounds
            )
            
            # Extract results
            estimated_position = result.x[:3]
            converged = result.success
            
            # Compute final residuals
            final_residuals = compute_residuals(
                np.array([*estimated_position, 0, 1]), 
                measurements
            )
            
            # Compute GDOP and FIM
            gdop = self.compute_gdop(measurements, estimated_position)
            fim = self.compute_fim(measurements, np.array([*estimated_position, 0, 1]))
            
            # Create estimation result
            return EstimationResult(
                estimator=np.array([*estimated_position, 0, 1]),
                covariance_matrix=np.zeros((5, 5)),  # TODO: Implement proper covariance
                residuals=final_residuals,
                raw_params=result.x,
                condition_number=float('inf'),
                verification_value=float('inf'),
                gdop=gdop,
                fim=fim,
                is_nonlinear=True,
                iteration_count=result.nfev,
                converged=converged
            )
            
        except Exception as e:
            logger.warning(f"Error in mixture model optimization: {e}")
            # Fall back to linear estimation
            linear_estimator = LinearReweightedEstimation(self.config)
            return linear_estimator.estimate(measurements.tolist(), initial_guess, weights)


class EstimationFactory:
    """Factory for creating estimation strategies based on method name."""
    
    @staticmethod
    def create_estimator(method: Union[str, EstimationMethod], config: Optional[EstimationConfig] = None) -> EstimationStrategy:
        """Create an estimation strategy based on the method name.
        
        Args:
            method: Method name or EstimationMethod enum
            config: Configuration parameters for the estimation strategy
            
        Returns:
            An instance of the appropriate EstimationStrategy
        """
        # Convert string to enum if needed
        if isinstance(method, str):
            method_upper = method.upper()
            try:
                # Handle common method name variations
                if method_upper == "SIMPLE_LINEAR" or method_upper == "LINEAR":
                    method = EstimationMethod.SIMPLE_LINEAR
                elif method_upper == "LINEAR_REWEIGHTED" or method_upper == "REWEIGHTED":
                    method = EstimationMethod.LINEAR_REWEIGHTED
                elif method_upper == "TRIMMED_REWEIGHTED" or method_upper == "TRIMMED":
                    method = EstimationMethod.TRIMMED_REWEIGHTED
                elif method_upper == "NONLINEAR_LM" or method_upper == "LM":
                    method = EstimationMethod.NONLINEAR_LM
                elif method_upper == "NONLINEAR_IRLS" or method_upper == "IRLS":
                    method = EstimationMethod.NONLINEAR_IRLS
                elif method_upper == "NONLINEAR_EM" or method_upper == "EM" or method_upper == "EM_NEW":
                    method = EstimationMethod.NONLINEAR_EM
                elif method_upper == "NONLINEAR_MM" or method_upper == "MM":
                    method = EstimationMethod.NONLINEAR_MM
                else:
                    # Try direct enum lookup
                    method = EstimationMethod[method_upper]
            except (KeyError, ValueError):
                logger.warning(f"Unknown estimation method: {method}, falling back to LINEAR_REWEIGHTED")
                method = EstimationMethod.LINEAR_REWEIGHTED
        
        # Create the appropriate strategy
        if method == EstimationMethod.SIMPLE_LINEAR:
            return SimpleLinearEstimation(config)
        elif method == EstimationMethod.LINEAR_REWEIGHTED:
            return LinearReweightedEstimation(config)
        elif method == EstimationMethod.TRIMMED_REWEIGHTED:
            return TrimmedReweightedEstimation(config)
        elif method == EstimationMethod.NONLINEAR_LM:
            return NonlinearLMEstimation(config)
        elif method == EstimationMethod.NONLINEAR_IRLS:
            return NonlinearIRLSEstimation(config)
        elif method == EstimationMethod.NONLINEAR_EM:
            return NonlinearEMEstimation(config)
        elif method == EstimationMethod.NONLINEAR_MM:
            return NonlinearMMEstimation(config)
        else:
            logger.warning(f"Unsupported estimation method: {method}, falling back to LINEAR_REWEIGHTED")
            return LinearReweightedEstimation(config)