"""
Trajectory Optimization for Drone-based UWB Anchor Initialization

This module provides tools for optimizing drone flight trajectories to improve
the accuracy of UWB anchor position estimates through optimal measurement placement.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize
from pathlib import Path
from typing import List, Tuple, Optional, Union, Dict, Any, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import logging
from enum import Enum

# Configure logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
logger = logging.getLogger(__name__)

# Add a stream handler for console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Get package path and CSV directory
PACKAGE_PATH = Path(__file__).parent.resolve()
CSV_DIR = PACKAGE_PATH / 'csv_files'


class MetricType(Enum):
    """Enum for different optimization metrics."""
    GDOP = "GDOP"
    FIM = "FIM"


@dataclass
class OptimizationParams:
    """Parameters for trajectory optimization.
    
    Attributes:
        max_waypoints: Maximum number of waypoints to generate
        marginal_gain_threshold: Minimum improvement required to add a waypoint
        radius_of_search: Radius for search sphere around current position
        lambda_penalty: Penalty factor for optimization constraints
    """
    max_waypoints: int = 8
    marginal_gain_threshold: float = 0.01
    radius_of_search: float = 1.0
    lambda_penalty: float = 10.0


class CoordinateTransformer:
    """Handles coordinate system transformations between Cartesian and spherical.
    
    This class provides static methods for converting between coordinate systems,
    which is essential for the local optimization approach used in trajectory planning.
    """
    
    @staticmethod
    def cartesian_to_spherical(point: np.ndarray, center: np.ndarray) -> Tuple[float, float, float]:
        """Convert Cartesian coordinates to spherical coordinates.
        
        Args:
            point: Point in Cartesian coordinates [x, y, z]
            center: Center point for spherical coordinates [x, y, z]
            
        Returns:
            Tuple of (r, theta, phi) in spherical coordinates
        """
        relative_point = point - center
        r = np.linalg.norm(relative_point)
        
        # Handle the special case where r is zero
        if np.isclose(r, 0):
            return 0.0, 0.0, 0.0
            
        theta = np.arccos(np.clip(relative_point[2] / r, -1.0, 1.0))
        phi = np.arctan2(relative_point[1], relative_point[0])
        return r, theta, phi

    @staticmethod
    def spherical_to_cartesian(r: float, theta: float, phi: float, center: np.ndarray) -> np.ndarray:
        """Convert spherical coordinates to Cartesian coordinates.
        
        Args:
            r: Radius
            theta: Polar angle (inclination)
            phi: Azimuthal angle
            center: Center point in Cartesian coordinates [x, y, z]
            
        Returns:
            Point in Cartesian coordinates [x, y, z]
        """
        x = r * np.sin(theta) * np.cos(phi) + center[0]
        y = r * np.sin(theta) * np.sin(phi) + center[1]
        z = r * np.cos(theta) + center[2]
        return np.array([x, y, z])
    
    @staticmethod
    def get_spherical_bounds(center: np.ndarray, 
                             radius: float, 
                             cartesian_bounds: Optional[List[Tuple[float, float]]] = None) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """Get bounds for the local spherical coordinates given constraints.
        
        Determines the valid ranges for theta and phi angles within a sphere of given radius,
        taking into account the Cartesian bounds of the environment.
        
        Args:
            center: Center of the spherical coordinates [x, y, z]
            radius: Radius of the sphere
            cartesian_bounds: Optional Cartesian coordinate bounds [(x_min, x_max), (y_min, y_max), (z_min, z_max)]
            
        Returns:
            Tuple of ((theta_min, theta_max), (phi_min, phi_max)) in radians
        """
        # Default bounds for unbounded space
        if cartesian_bounds is None:
            return (0, np.pi), (0, 2 * np.pi)
            
        x_min, x_max = cartesian_bounds[0]
        y_min, y_max = cartesian_bounds[1]
        z_min, z_max = cartesian_bounds[2]
        x_c, y_c, z_c = center
        
        # Check if the center is outside bounds, making optimization impossible
        if (x_c > x_max or x_c < x_min or 
            y_c > y_max or y_c < y_min or 
            z_c > z_max or z_c < z_min):
            logger.warning(f"Center point {center} is outside specified bounds, optimization not possible")
            return (None, None), (None, None)
        
        # Default bounds
        theta_min, theta_max = 0, np.pi
        phi_min, phi_max = 0, 2 * np.pi
        
        # Adjust theta bounds based on z constraints
        if abs(z_c - z_max) < radius:
            theta_min = np.pi/2
        if abs(z_c - z_min) < radius:
            theta_max = np.pi/2
            
        # Adjust phi bounds based on x constraints
        phi_min_x, phi_max_x = phi_min, phi_max
        if abs(x_c - x_max) < radius:
            phi_min_x = np.pi/2
            phi_max_x = 3*np.pi/2
        if abs(x_c - x_min) < radius:
            phi_min_x = -np.pi/2
            phi_max_x = np.pi/2
            
        # Adjust phi bounds based on y constraints
        phi_min_y, phi_max_y = phi_min, phi_max
        if abs(y_c - y_max) < radius:
            phi_min_y = np.pi
            phi_max_y = 2 * np.pi
        if abs(y_c - y_min) < radius:
            phi_min_y = 0
            phi_max_y = np.pi
            
        # Combine constraints using intersection
        phi_bounds = CoordinateTransformer._intersect_angle_intervals(
            phi_min_x, phi_max_x, phi_min_y, phi_max_y
        )
        
        return (theta_min, theta_max), phi_bounds
    
    @staticmethod
    def _intersect_angle_intervals(phi1_min: Optional[float], phi1_max: Optional[float], 
                                   phi2_min: Optional[float], phi2_max: Optional[float]) -> Tuple[Optional[float], Optional[float]]:
        """Find the intersection of two angular intervals.
        
        Args:
            phi1_min, phi1_max: First interval bounds
            phi2_min, phi2_max: Second interval bounds
            
        Returns:
            Tuple of (intersection_min, intersection_max) or (None, None) if no valid intersection
        """
        if phi1_min is None or phi2_min is None:
            return None, None

        # Find the intersection
        phi_min = max(phi1_min, phi2_min)
        phi_max = min(phi1_max, phi2_max)

        if phi_min > phi_max:  # No valid intersection
            return None, None

        return phi_min, phi_max


class OptimizationMetric(ABC):
    """Abstract base class for optimization metrics.
    
    This defines the interface for different optimization metrics used to
    evaluate measurement configurations for localizing a target.
    """
    
    @abstractmethod
    def compute(self, target_coords: np.ndarray, measurements: np.ndarray) -> float:
        """Compute the metric value for a given configuration.
        
        Args:
            target_coords: Estimated target coordinates [x, y, z]
            measurements: Array of measurement positions, shape (n, 3)
            
        Returns:
            Metric value (lower is better)
        """
        pass

    @abstractmethod
    def evaluate_gain(self, new_measurement: np.ndarray, target_coords: np.ndarray, 
                      previous_measurements: np.ndarray) -> float:
        """Evaluate the improvement from adding a new measurement.
        
        Args:
            new_measurement: Potential new measurement position [x, y, z]
            target_coords: Estimated target coordinates [x, y, z]
            previous_measurements: Existing measurement positions, shape (n, 3)
            
        Returns:
            Metric value with the new measurement (lower is better)
        """
        pass


class GDOPMetric(OptimizationMetric):
    """Geometric Dilution of Precision (GDOP) optimization metric.
    
    GDOP measures how receiver-transmitter geometry affects positioning precision.
    Lower GDOP values indicate better geometric configurations.
    """
    
    def _build_geometry_matrix(self, target_coords: np.ndarray, measurements: np.ndarray) -> np.ndarray:
        """Build geometry matrix for GDOP computation."""
        # logger.debug(f"Building geometry matrix with:")
        # logger.debug(f"Target coords: {target_coords}")
        # logger.debug(f"Measurements shape: {measurements.shape}")
        # logger.debug(f"First few measurements: {measurements[:3]}")
        
        num_measurements = len(measurements)
        A = np.zeros((num_measurements, 3))
        
        for i in range(num_measurements):
            diff = measurements[i] - target_coords
            dist = np.linalg.norm(diff)
            if dist < 1e-10:
                logger.warning(f"Very small distance detected at measurement {i}: {dist}")
                dist = 1e-10
            A[i] = diff / dist
            
        # logger.debug(f"Resulting geometry matrix A:\n{A}")
        return A

    def compute(self, target_coords: np.ndarray, measurements: np.ndarray) -> float:
        """Compute GDOP value for the given configuration."""
        # logger.debug("\n=== Starting GDOP computation ===")
        # logger.debug(f"Target coordinates: {target_coords}")
        # logger.debug(f"Number of measurements: {len(measurements)}")
        
        if len(measurements) < 4:
            logger.debug("Not enough measurements, returning inf")
            return float('inf')
            
        try:
            A = self._build_geometry_matrix(target_coords, measurements)

            inv_at_a = np.linalg.inv(A.T @ A)
            gdop = np.sqrt(np.trace(inv_at_a))
            if gdop is not None:
                return gdop
            else:
                return float('inf')
        except np.linalg.LinAlgError:
            return float('inf')
        
            # Use SVD-based pseudo-inverse for numerical stability
            u, s, vh = np.linalg.svd(A, full_matrices=False)
            
            # Filter out near-zero singular values to avoid numerical issues
            s_inv = np.zeros_like(s)
            mask = s > 1e-10
            s_inv[mask] = 1.0 / s[mask]
            
            # Compute pseudo-inverse and then get trace
            inv_at_a = vh.T @ np.diag(s_inv**2) @ u.T
            try:
                gdop = np.sqrt(np.trace(inv_at_a))
                if np.isnan(gdop):
                    # logger.warning("GDOP computation resulted in NaN")
                    # logger.warning(f"Trace of inv_at_a: {np.trace(inv_at_a)}")
                    # # print condition number
                    # logger.warning(f"Condition number of inv_at_a: {np.linalg.cond(inv_at_a)}")
                    return float('inf')
                return gdop
            except Exception as e:
                logger.warning(f"Error computing trace in GDOP: {e}")
                return float('inf')
            
        except np.linalg.LinAlgError as e:
            logger.warning(f"Linear algebra error in GDOP computation: {e}")
            return float('inf')
    
    def evaluate_gain(self, new_measurement: np.ndarray, target_coords: np.ndarray, 
                      previous_measurements: np.ndarray) -> float:
        """Evaluate GDOP with the addition of a new measurement.
        
        Args:
            new_measurement: Potential new measurement position [x, y, z]
            target_coords: Estimated target coordinates [x, y, z]
            previous_measurements: Existing measurement positions, shape (n, 3)
            
        Returns:
            GDOP value with the new measurement
        """
        # Ensure new_measurement is properly shaped
        new_measurement = np.array(new_measurement).reshape(1, -1)
        
        # Combine with previous measurements
        if len(previous_measurements) == 0:
            combined_measurements = new_measurement
        else:
            combined_measurements = np.vstack([previous_measurements, new_measurement])
            
        return self.compute(target_coords, combined_measurements)
    
    @staticmethod
    def _build_geometry_matrix(target_coords: np.ndarray, 
                               measurements: np.ndarray) -> np.ndarray:
        """Build the geometry matrix for GDOP computation.
        
        Args:
            target_coords: Estimated target coordinates [x, y, z]
            measurements: Array of measurement positions, shape (n, 3)
            
        Returns:
            Geometry matrix A
        """
        # Calculate unit vectors from target to each measurement point
        differences = measurements - target_coords
        distances = np.linalg.norm(differences, axis=1)
        
        # Avoid division by zero
        valid_indices = distances > 1e-10
        if not np.all(valid_indices):
            logger.warning(f"Found {np.sum(~valid_indices)} measurement points too close to target")
            
        unit_vectors = np.zeros_like(differences)
        unit_vectors[valid_indices] = differences[valid_indices] / distances[valid_indices, np.newaxis]
        
        # The geometry matrix includes the unit vectors and a column of ones
        return np.column_stack([unit_vectors, np.ones((len(measurements), 1))])


class FIMMetric(OptimizationMetric):
    """Fisher Information Matrix (FIM) based optimization metric.
    
    FIM captures how informative measurements are about the target position,
    considering the measurement noise model.
    """
    
    def __init__(self, noise_variance: float = 0.2):
        """Initialize the FIM metric.
        
        Args:
            noise_variance: Variance of measurement noise
        """
        self.noise_variance = noise_variance
        
    def compute(self, target_coords: np.ndarray, measurements: np.ndarray) -> float:
        """Compute the inverse determinant of the FIM.
        
        Lower values indicate better information content.
        
        Args:
            target_coords: Estimated target coordinates [x, y, z]
            measurements: Array of measurement positions, shape (n, 3)
            
        Returns:
            Inverse determinant of FIM (lower is better)
        """
        if len(measurements) < 3:
            return float('inf')
            
        try:
            fim = self._compute_fim_matrix(target_coords, measurements)
            det_fim = np.linalg.det(fim)
            
            # Check for near-singular FIM
            if abs(det_fim) < 1e-10:
                logger.warning("Near-singular FIM detected, determinant close to zero")
                return float('inf')
                
            return 1.0 / det_fim
            
        except np.linalg.LinAlgError as e:
            logger.warning(f"Linear algebra error in FIM computation: {e}")
            return float('inf')
    
    def evaluate_gain(self, new_measurement: np.ndarray, target_coords: np.ndarray, 
                      previous_measurements: np.ndarray) -> float:
        """Evaluate FIM metric with the addition of a new measurement.
        
        Args:
            new_measurement: Potential new measurement position [x, y, z]
            target_coords: Estimated target coordinates [x, y, z]
            previous_measurements: Existing measurement positions, shape (n, 3)
            
        Returns:
            FIM metric value with the new measurement
        """
        # Ensure new_measurement is properly shaped
        new_measurement = np.array(new_measurement).reshape(1, -1)
        
        # Combine with previous measurements
        if len(previous_measurements) == 0:
            combined_measurements = new_measurement
        else:
            combined_measurements = np.vstack([previous_measurements, new_measurement])
            
        return self.compute(target_coords, combined_measurements)
    
    def _compute_fim_matrix(self, target_coords: np.ndarray, 
                           measurements: np.ndarray, noise_variance: Optional[float] = None) -> np.ndarray:
        """Compute the Fisher Information Matrix.
        
        Args:
            target_coords: Estimated target coordinates [x, y, z]
            measurements: Array of measurement positions, shape (n, 3)
            noise_variance: Optional override for noise variance
            
        Returns:
            3x3 Fisher Information Matrix
        """
        x0, y0, z0 = target_coords
        measurements = np.array(measurements)
        noise_var = noise_variance if noise_variance is not None else self.noise_variance
        
        # Compute distances between measurements and target
        z_m = np.linalg.norm(measurements - np.array([x0, y0, z0]), axis=1)
        
        # Handle potential zero distances
        z_m = np.maximum(z_m, 1e-10)
        
        # Differences in x, y, z coordinates
        x_differences = x0 - measurements[:, 0]
        y_differences = y0 - measurements[:, 1]
        z_differences = z0 - measurements[:, 2]

        # Compute derivatives dzm_dx, dzm_dy, dzm_dz
        dzm_dx = x_differences / z_m
        dzm_dy = y_differences / z_m
        dzm_dz = z_differences / z_m

        # Create the noise covariance matrix - more realistic model
        C_q = noise_var * np.diag((1 + z_m)**2)
        
        # Safely invert C_q using SVD for numerical stability
        try:
            u, s, vh = np.linalg.svd(C_q)
            s_inv = 1.0 / s
            inv_C_q = vh.T @ np.diag(s_inv) @ u.T
        except np.linalg.LinAlgError:
            # Fallback to regularized inverse if SVD fails
            logger.warning("SVD failed in C_q inversion, using regularized inverse")
            C_q_reg = C_q + np.eye(len(C_q)) * 1e-6
            inv_C_q = np.linalg.inv(C_q_reg)

        # Compute derivatives of C with respect to x, y, and z
        dC_dx = noise_var * np.diag((1 + z_m) / z_m * x_differences)
        dC_dy = noise_var * np.diag((1 + z_m) / z_m * y_differences)
        dC_dz = noise_var * np.diag((1 + z_m) / z_m * z_differences)

        # Initialize Fisher Information Matrix (FIM)
        FIM = np.zeros((3, 3))

        # Compute FIM elements with numerical protections
        def compute_fim_element(dzm_a, dzm_b, dC_a, dC_b):
            term1 = dzm_a.T @ inv_C_q @ dzm_b
            term2 = 0.5 * np.trace(inv_C_q @ dC_a @ inv_C_q @ dC_b)
            return term1 + term2

        # Compute the diagonal terms of FIM
        FIM[0, 0] = compute_fim_element(dzm_dx, dzm_dx, dC_dx, dC_dx)
        FIM[1, 1] = compute_fim_element(dzm_dy, dzm_dy, dC_dy, dC_dy)
        FIM[2, 2] = compute_fim_element(dzm_dz, dzm_dz, dC_dz, dC_dz)

        # Compute the off-diagonal terms
        FIM[0, 1] = compute_fim_element(dzm_dx, dzm_dy, dC_dx, dC_dy)
        FIM[0, 2] = compute_fim_element(dzm_dx, dzm_dz, dC_dx, dC_dz)
        FIM[1, 2] = compute_fim_element(dzm_dy, dzm_dz, dC_dy, dC_dz)

        # Fill the symmetric terms
        FIM[1, 0] = FIM[0, 1]
        FIM[2, 0] = FIM[0, 2]
        FIM[2, 1] = FIM[1, 2]

        # Check for NaN or Inf values
        if np.any(np.isnan(FIM)) or np.any(np.isinf(FIM)):
            logger.warning("NaN or Inf values detected in FIM")
            # Replace with large finite values
            FIM = np.nan_to_num(FIM, nan=1e10, posinf=1e10, neginf=-1e10)

        return FIM


class ReturnTrajectoryMethod(Enum):
    """Methods for computing return trajectories after optimization."""
    STRICT_RETURN = "strict_return"
    RETURN_TO_INITIAL = "return_to_initial"
    STRAIGHT_TO_WAYPOINT = "straight_to_wapoint"  # Original typo preserved
    RETURN_TO_CLOSEST = "return_to_closest"
    HYBRID_RETURN = "hybrid_return"
    OPTIMAL = "optimal"


@dataclass
class OptimizationResult:
    """Container for trajectory optimization results.
    
    Attributes:
        optimal_waypoints: List of optimized waypoints
        return_waypoints: Optional list of return path waypoints
        link_waypoints: Any connecting waypoints between segments
        metrics: Dictionary of metric values at each step
        success: Whether optimization completed successfully
        message: Additional information about the result
    """
    optimal_waypoints: List[np.ndarray] = field(default_factory=list)
    return_waypoints: Optional[List[np.ndarray]] = None
    link_waypoints: List[np.ndarray] = field(default_factory=list)
    metrics: Dict[int, float] = field(default_factory=dict)
    success: bool = True
    message: str = ""


class TrajectoryOptimizer:
    """Optimizes drone trajectories for better target localization.
    
    This class implements algorithms to find optimal waypoints for a drone
    to improve localization of a UWB anchor, using various optimization metrics.
    """
    
    def __init__(self, metric_type: Union[str, MetricType] = "FIM", 
                 bounds: Optional[List[Tuple[float, float]]] = None,
                 params: Optional[OptimizationParams] = None):
        """Initialize the trajectory optimizer.
        
        Args:
            metric_type: Type of optimization metric ('GDOP' or 'FIM')
            bounds: Optional Cartesian bounds for the optimization space
            params: Optional optimization parameters
        """
        # Check if bounds is None instead of using it directly in boolean context
        self.bounds = bounds if bounds is not None else [(-float('inf'), float('inf'))] * 3
        
        # Convert string to enum if needed
        if isinstance(metric_type, str):
            try:
                metric_type = MetricType(metric_type)
            except ValueError:
                logger.warning(f"Invalid metric type '{metric_type}', defaulting to FIM")
                metric_type = MetricType.FIM
        
        # Initialize the appropriate metric
        if metric_type == MetricType.GDOP:
            self.metric = GDOPMetric()
        else:
            self.metric = FIMMetric()
            
        # Set other parameters
        self.bounds = bounds if bounds is not None else [(-float('inf'), float('inf'))] * 3
        self.params = params or OptimizationParams()
        self.transformer = CoordinateTransformer()
    
    def optimize_trajectory(self, initial_position: np.ndarray, 
                           anchor_estimate: np.ndarray,
                           previous_measurements: np.ndarray,
                           target_point: Optional[np.ndarray] = None) -> OptimizationResult:
        """Optimize the drone trajectory for better target localization.
        
        Args:
            initial_position: Starting position of the drone [x, y, z]
            anchor_estimate: Estimated position of the anchor [x, y, z]
            previous_measurements: Previous measurement positions, shape (n, 3)
            target_point: Optional target point for return trajectory [x, y, z]
            
        Returns:
            OptimizationResult containing the optimal waypoints and metrics
        """
        logger.info(f"Starting trajectory optimization from {initial_position}")
        
        
        # Ensure inputs are numpy arrays
        initial_position = np.array(initial_position).reshape(1, 3)
        anchor_estimate = np.array(anchor_estimate)
        previous_measurements = np.array(previous_measurements)
        
        # Check if previous_measurements is empty
        if len(previous_measurements) == 0:
            previous_measurements = initial_position
            
        # Optimize forward trajectory
        forward_result = self._optimize_forward_trajectory(
            initial_position[0], anchor_estimate, previous_measurements)
            
        result = OptimizationResult(
            optimal_waypoints=forward_result["waypoints"],
            metrics=forward_result["metrics"],
            success=forward_result["success"],
            message=forward_result["message"]
        )
            
        # Add return trajectory if target point is specified
        if target_point is not None and result.success and result.optimal_waypoints:
            target_point = np.array(target_point)
            return_result = self._optimize_return_trajectory(
                result.optimal_waypoints[-1], anchor_estimate, 
                previous_measurements, target_point)
                
            result.return_waypoints = return_result["waypoints"]
            
        logger.info(f"Optimization completed with {len(result.optimal_waypoints)} waypoints")
        return result

    def _optimize_forward_trajectory(self, initial_position: np.ndarray,
                                    anchor_estimate: np.ndarray,
                                    previous_measurements: np.ndarray) -> Dict[str, Any]:
        """Optimize the forward trajectory for measurements."""
        # logger.debug("\n=== Starting New Optimization ===")
        # logger.debug(f"Initial position: {initial_position}")
        # logger.debug(f"Anchor estimate: {anchor_estimate}")
        # logger.debug(f"Previous measurements:")
        for i, meas in enumerate(previous_measurements):
            logger.debug(f"  Measurement {i}: {meas}")
        
        # Get baseline metric value
        current_metrics = self.metric.compute(anchor_estimate, previous_measurements)
        # logger.debug(f"Initial metric value: {current_metrics}")
        
        max_waypoints = self.params.max_waypoints
        marginal_gain_threshold = self.params.marginal_gain_threshold
        radius_of_search = self.params.radius_of_search

        # logger.debug(f"Starting forward trajectory optimization with parameters:")
        # logger.debug(f"  max_waypoints: {max_waypoints}")
        # logger.debug(f"  marginal_gain_threshold: {marginal_gain_threshold}")
        # logger.debug(f"  radius_of_search: {radius_of_search}")
        # logger.debug(f"  initial_position: {initial_position}")
        # logger.debug(f"  anchor_estimate: {anchor_estimate}")
        # logger.debug(f"  number of previous measurements: {len(previous_measurements)}")

        best_waypoints = []
        metrics = {}
        
        last_measurement = initial_position
        
        # Create initial direction vector toward anchor
        vector = anchor_estimate - initial_position
        # logger.debug(f"Direction vector to anchor: {vector}")
        
        # Compute spherical coordinates of the direction vector
        r, theta, phi = self.transformer.cartesian_to_spherical(vector, np.zeros(3))
        initial_guess = np.array([theta, phi])
        # logger.debug(f"Initial spherical coordinates - r: {r}, theta: {theta}, phi: {phi}")
        # logger.debug(f"Initial guess for optimization: {initial_guess}")
        
        for i in range(max_waypoints):
            # logger.debug(f"\nStarting iteration {i+1}/{max_waypoints}")
            
            # Use larger radius for first step
            current_radius = 2 * radius_of_search if i == 0 else radius_of_search
            # logger.debug(f"Current search radius: {current_radius}")
            
            # Define the objective function for optimization
            def objective(spherical_coords: np.ndarray) -> float:
                """Objective function to minimize."""
                theta, phi = spherical_coords
                # logger.debug(f"Evaluating objective at theta: {theta}, phi: {phi}")
                
                # Convert spherical coordinates to Cartesian
                new_point = self.transformer.spherical_to_cartesian(
                    current_radius, theta, phi, last_measurement)
                # logger.debug(f"Converted to Cartesian point: {new_point}")
                
                # Reshape for evaluation
                new_point = np.array(new_point).reshape(1, 3)
                
                # Compute metric value with this new point
                all_measurements = np.vstack([previous_measurements, new_point])
                metric_value = self.metric.compute(anchor_estimate, all_measurements)
                # logger.debug(f"Computed metric value: {metric_value}")
                return metric_value
            
            # Get bounds for spherical coordinates based on Cartesian constraints
            theta_bounds, phi_bounds = self.transformer.get_spherical_bounds(
                last_measurement, current_radius, self.bounds)
            # logger.debug(f"Optimization bounds:")
            # logger.debug(f"  theta_bounds: {theta_bounds}")
            # logger.debug(f"  phi_bounds: {phi_bounds}")
                
            # Check if optimization is possible within bounds
            if None in theta_bounds or None in phi_bounds:
                # logger.warning("Invalid bounds detected, optimization not possible")
                return {
                    "waypoints": best_waypoints,
                    "metrics": metrics,
                    "success": False,
                    "message": "Optimization not possible within specified bounds"
                }
                
            # Perform bounded optimization
            bounds = [theta_bounds, phi_bounds]
            # logger.debug(f"Starting optimization with bounds: {bounds}")
            optimization_result = minimize(
                objective, 
                initial_guess, 
                method='Powell',
                bounds=bounds
            )
            
            # logger.debug(f"Optimization result:")
            # logger.debug(f"  success: {optimization_result.success}")
            # logger.debug(f"  message: {optimization_result.message}")
            # logger.debug(f"  final x: {optimization_result.x}")
            # logger.debug(f"  final fun: {optimization_result.fun}")
            # logger.debug(f"  nfev: {optimization_result.nfev}")
            
            if optimization_result.success:
                # Extract the optimal spherical coordinates
                optimal_spherical = optimization_result.x
                # logger.debug(f"Optimal spherical coordinates: {optimal_spherical}")
                
                # Convert to Cartesian
                new_waypoint = self.transformer.spherical_to_cartesian(
                    current_radius, optimal_spherical[0], optimal_spherical[1], last_measurement)
                # logger.debug(f"New waypoint in Cartesian coordinates: {new_waypoint}")
                
                # Compute new metric value
                all_measurements = np.vstack([previous_measurements, new_waypoint.reshape(1, 3)])
                new_metric = self.metric.compute(anchor_estimate, all_measurements)
                metrics[i+1] = new_metric
                
                # Check if the improvement is significant
                metric_gain = current_metrics - new_metric  # Note: lower is better for our metrics
                if metric_gain < marginal_gain_threshold:
                    logger.info(f"Stopping optimization: marginal gain {metric_gain} below threshold")
                    break
                    
                # Update for next iteration
                best_waypoints.append(new_waypoint)
                previous_measurements = np.vstack([previous_measurements, new_waypoint.reshape(1, 3)])
                current_metrics = new_metric
                last_measurement = new_waypoint
                
                # Check if close enough to anchor
                if np.linalg.norm(new_waypoint - anchor_estimate) < radius_of_search:
                    logger.info("Optimization reached vicinity of anchor")
                    break
                    
                # Update initial guess for next iteration
                initial_guess = optimal_spherical
                
            else:
                logger.warning(f"Optimization failed at waypoint {i+1}: {optimization_result.message}")
                if i == 0:  # If first optimization fails, return failure
                    return {
                        "waypoints": best_waypoints,
                        "metrics": metrics,
                        "success": False,
                        "message": f"Initial optimization failed: {optimization_result.message}"
                    }
                break
        
        return {
            "waypoints": best_waypoints,
            "metrics": metrics,
            "success": True,
            "message": f"Optimization completed with {len(best_waypoints)} waypoints"
        }
    
    def _optimize_return_trajectory(self, start_position: np.ndarray,
                                   anchor_estimate: np.ndarray,
                                   previous_measurements: np.ndarray,
                                   target_point: np.ndarray) -> Dict[str, Any]:
        """Optimize the return trajectory.
        
        Args:
            start_position: Starting position for return [x, y, z]
            anchor_estimate: Estimated anchor position [x, y, z]
            previous_measurements: All previous measurements [x, y, z]
            target_point: Target point to return to [x, y, z]
            
        Returns:
            Dictionary with optimization results
        """
        # Implement a direct path with intermediate waypoints
        # that maintain information value about the anchor
        
        # For simplicity, create a straight-line path with a few waypoints
        # that balance information gain and direct return
        
        # Vector from start to target
        direction = target_point - start_position
        distance = np.linalg.norm(direction)
        unit_vector = direction / (distance + 1e-10)  # Avoid division by zero
        
        # Determine number of waypoints based on distance
        num_waypoints = min(3, max(1, int(distance / self.params.radius_of_search)))
        
        waypoints = []
        radius = self.params.radius_of_search
        
        for i in range(num_waypoints):
            # Linear interpolation between start and target
            t = (i + 1) / (num_waypoints + 1)
            base_point = start_position + t * direction
            
            # Add some variation to maintain information value
            # Compute a direction that maintains visibility of the anchor
            to_anchor = anchor_estimate - base_point
            to_anchor_unit = to_anchor / (np.linalg.norm(to_anchor) + 1e-10)
            
            # Create a vector perpendicular to both the return path and the anchor direction
            perpendicular = np.cross(unit_vector, to_anchor_unit)
            perpendicular = perpendicular / (np.linalg.norm(perpendicular) + 1e-10)
            
            # Add a small offset in this perpendicular direction
            offset = 0.3 * radius * perpendicular
            
            # Final waypoint with offset
            waypoint = base_point + offset
            
            # Check if this waypoint improves information
            new_measurements = np.vstack([previous_measurements, waypoint.reshape(1, 3)])
            new_metric = self.metric.compute(anchor_estimate, new_measurements)
            current_metric = self.metric.compute(anchor_estimate, previous_measurements)
            
            # Only add if it improves information (or at least doesn't degrade too much)
            if new_metric <= current_metric * 1.1:  # Allow up to 10% degradation
                waypoints.append(waypoint)
                previous_measurements = new_measurements
        
        return {
            "waypoints": waypoints,
            "success": True,
            "message": f"Generated {len(waypoints)} return waypoints"
        }
    
    def compute_new_mission_waypoints(self, 
                                    initial_position: np.ndarray, 
                                    initial_remaining_waypoints: List[np.ndarray], 
                                    optimal_waypoints: List[np.ndarray], 
                                    method: Union[str, ReturnTrajectoryMethod] = ReturnTrajectoryMethod.RETURN_TO_CLOSEST,
                                    return_waypoints: Optional[List[np.ndarray]] = None) -> Tuple[List[np.ndarray], List[np.ndarray], List[np.ndarray], List[np.ndarray]]:
        """Compute the new mission waypoints based on optimal trajectory.
        
        This method integrates the optimized trajectory with the original mission plan,
        using different strategies for returning to the planned path.
        
        Args:
            initial_position: The previous waypoint of the drone [x, y, z]
            initial_remaining_waypoints: The remaining waypoints from the original plan
            optimal_waypoints: The optimal waypoints from trajectory optimization
            method: Method to use for returning to the original plan
            return_waypoints: Optional pre-computed return waypoints
            
        Returns:
            Tuple of (new_mission_waypoints, optimal_waypoints, link_waypoints, remaining_waypoints)
        """
        new_mission_waypoints = []
        link_waypoints = []
        
        # Convert string to enum if needed
        if isinstance(method, str):
            try:
                method = ReturnTrajectoryMethod(method)
            except ValueError:
                logger.warning(f"Invalid return method '{method}', defaulting to RETURN_TO_CLOSEST")
                method = ReturnTrajectoryMethod.RETURN_TO_CLOSEST
        
        # If no optimal waypoints, just continue with the original plan
        if not optimal_waypoints:
            logger.info("No optimal waypoints generated, continuing with original plan")
            new_mission_waypoints.extend(initial_remaining_waypoints)
            return new_mission_waypoints, optimal_waypoints, link_waypoints, initial_remaining_waypoints
        
        # If no remaining waypoints, just follow the optimal path
        if not initial_remaining_waypoints:
            logger.info("No remaining waypoints in original plan, following optimal path only")
            new_mission_waypoints.extend(optimal_waypoints)
            return new_mission_waypoints, optimal_waypoints, link_waypoints, []
            
        # Process according to the selected method
        if method == ReturnTrajectoryMethod.STRICT_RETURN:
            # Find point on next segment closest to last optimal waypoint
            closest_point = self._closest_point_on_line(
                initial_position, initial_remaining_waypoints[0], optimal_waypoints[-1])
                
            # Follow optimal path, then go to closest point, then resume original plan
            new_mission_waypoints.extend(optimal_waypoints)
            new_mission_waypoints.append(closest_point)
            new_mission_waypoints.extend(initial_remaining_waypoints)
            
            # Add closest point to optimal waypoints for continuity
            optimal_waypoints.append(closest_point)
            
        elif method == ReturnTrajectoryMethod.RETURN_TO_INITIAL:
            # Follow optimal path, then return to initial position, then resume plan
            new_mission_waypoints.extend(optimal_waypoints)
            new_mission_waypoints.append(initial_position)
            new_mission_waypoints.extend(initial_remaining_waypoints)
            
            link_waypoints = [initial_position]
            
        elif method == ReturnTrajectoryMethod.STRAIGHT_TO_WAYPOINT:
            # Follow optimal path, then directly to next planned waypoint
            new_mission_waypoints.extend(optimal_waypoints)
            new_mission_waypoints.extend(initial_remaining_waypoints)
            
            if initial_remaining_waypoints:
                link_waypoints = [initial_remaining_waypoints[0]]
                
        elif method == ReturnTrajectoryMethod.RETURN_TO_CLOSEST:
            # Find point on next segment closest to last optimal waypoint
            closest_point = self._closest_point_on_line(
                initial_position, initial_remaining_waypoints[0], optimal_waypoints[-1])
                
            # Follow optimal path, then to closest point, then resume original plan
            new_mission_waypoints.extend(optimal_waypoints)
            new_mission_waypoints.append(closest_point)
            new_mission_waypoints.extend(initial_remaining_waypoints)
            
            link_waypoints = [closest_point]
            
        elif method == ReturnTrajectoryMethod.HYBRID_RETURN:
            # Get closest point, then compute a hybrid point that's offset from it
            closest_point = self._closest_point_on_line(
                initial_position, initial_remaining_waypoints[0], optimal_waypoints[-1])
                
            # Distance scaled by tan(60°)
            distance = np.tan(np.pi/3) * np.linalg.norm(closest_point - optimal_waypoints[-1])
            
            # Get a point that's at scaled distance from closest point along the original path
            hybrid_point = self._distance_on_segment(
                initial_position, initial_remaining_waypoints[0], closest_point, distance)
                
            # Follow optimal path, then hybrid point, then resume original plan  
            new_mission_waypoints.extend(optimal_waypoints)
            new_mission_waypoints.append(hybrid_point)
            new_mission_waypoints.extend(initial_remaining_waypoints)
            
            # Add closest point to optimal waypoints for visualization
            optimal_waypoints.append(closest_point)
            
        elif method == ReturnTrajectoryMethod.OPTIMAL:
            # Use pre-computed return waypoints if available
            new_mission_waypoints.extend(optimal_waypoints)
            
            if return_waypoints:
                link_waypoints = return_waypoints
                new_mission_waypoints.extend(link_waypoints)
                
            new_mission_waypoints.extend(initial_remaining_waypoints)
        
        return new_mission_waypoints, optimal_waypoints, link_waypoints, initial_remaining_waypoints
    
    @staticmethod
    def _closest_point_on_line(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> np.ndarray:
        """Find the closest point on line segment AB from point C.
        
        Args:
            A: First point defining the line segment [x, y, z]
            B: Second point defining the line segment [x, y, z]
            C: Point to find closest point from [x, y, z]
            
        Returns:
            Closest point on line segment AB from C
        """
        # Convert to numpy arrays
        A = np.array(A)
        B = np.array(B)
        C = np.array(C)
        
        # Vector AB and AC
        AB = B - A
        AC = C - A
        
        # Project AC onto AB to get parameter t
        AB_squared = np.dot(AB, AB)
        
        # Handle degenerate case (points A and B are the same)
        if np.isclose(AB_squared, 0):
            return A
            
        t = np.dot(AC, AB) / AB_squared
        
        # Clamp t to [0,1] for closest point on segment
        t = max(0, min(1, t))
        
        # Find the point on line segment
        P = A + t * AB
        
        return P
    
    @staticmethod
    def _distance_on_segment(A: np.ndarray, B: np.ndarray, C: np.ndarray, d: float) -> np.ndarray:
        """Find a point at distance d from C towards B along the segment.
        
        Args:
            A: First point defining original line segment [x, y, z]
            B: Second point defining original line segment [x, y, z]
            C: Starting point (usually on the segment) [x, y, z]
            d: Distance to travel from C towards B
            
        Returns:
            Point at distance d from C towards B
        """
        # Convert to numpy arrays
        A = np.array(A)
        B = np.array(B)
        C = np.array(C)
        
        # Compute vector CB
        CB = B - C
        distance_CB = np.linalg.norm(CB)
        
        # If distance is greater than length of CB, return B
        if d >= distance_CB:
            return B
        
        # Compute unit vector from C to B
        CB_unit = CB / (distance_CB + 1e-10)  # Avoid division by zero
        
        # Compute point at distance d from C towards B
        P = C + d * CB_unit
        
        return P


class TrajectoryVisualizer:
    """Handles visualization of trajectories and measurements.
    
    This class provides tools for visualizing the results of trajectory optimization,
    including the original measurements, optimized waypoints, and return trajectories.
    """
    
    @staticmethod
    def plot_trajectory(previous_measurements: np.ndarray,
                       anchor_position: np.ndarray,
                       optimal_waypoints: List[np.ndarray],
                       return_waypoints: Optional[List[np.ndarray]] = None,
                       link_waypoints: Optional[List[np.ndarray]] = None,
                       remaining_waypoints: Optional[List[np.ndarray]] = None,
                       title: str = "Trajectory Optimization Results",
                       show_plot: bool = True,
                       save_path: Optional[str] = None):
        """Plot the trajectory optimization results.
        
        Args:
            previous_measurements: Previous measurement positions, shape (n, 3)
            anchor_position: Anchor position [x, y, z]
            optimal_waypoints: List of optimal waypoints
            return_waypoints: Optional list of return waypoints
            link_waypoints: Optional list of linking waypoints
            remaining_waypoints: Optional list of remaining original waypoints
            title: Plot title
            show_plot: Whether to display the plot
            save_path: Optional path to save the plot
        """
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Convert lists to numpy arrays if needed
        previous_measurements = np.array(previous_measurements)
        anchor_position = np.array(anchor_position)
        optimal_waypoints = np.array(optimal_waypoints)
        
        # Plot anchor position
        ax.scatter(anchor_position[0], anchor_position[1], anchor_position[2],
                  color='red', s=150, marker='*', label='Anchor Position', zorder=10)
        
        # Plot previous measurements
        if len(previous_measurements) > 0:
            ax.scatter(previous_measurements[:, 0], previous_measurements[:, 1], 
                      previous_measurements[:, 2], color='blue', alpha=0.6, 
                      label='Previous Measurements')
            
            # Plot trajectory lines for previous measurements
            if len(previous_measurements) > 1:
                ax.plot(previous_measurements[:, 0], previous_measurements[:, 1], 
                       previous_measurements[:, 2], 'b-', alpha=0.3)
        
        # Plot optimal waypoints
        if len(optimal_waypoints) > 0:
            ax.scatter(optimal_waypoints[:, 0], optimal_waypoints[:, 1], 
                      optimal_waypoints[:, 2], color='green', s=80, 
                      label='Optimal Waypoints')
            
            # Plot trajectory lines for optimal waypoints
            ax.plot(optimal_waypoints[:, 0], optimal_waypoints[:, 1], 
                   optimal_waypoints[:, 2], 'g-', linewidth=2)
        
        # Plot return waypoints if available
        if return_waypoints is not None and len(return_waypoints) > 0:
            return_waypoints = np.array(return_waypoints)
            ax.scatter(return_waypoints[:, 0], return_waypoints[:, 1], 
                      return_waypoints[:, 2], color='purple', 
                      label='Return Waypoints')
            
            # Connect the last optimal waypoint to first return waypoint
            if len(optimal_waypoints) > 0 and len(return_waypoints) > 0:
                connect_points = np.vstack([optimal_waypoints[-1], return_waypoints[0]])
                ax.plot(connect_points[:, 0], connect_points[:, 1], 
                       connect_points[:, 2], 'g--')
            
            # Plot trajectory lines for return waypoints
            ax.plot(return_waypoints[:, 0], return_waypoints[:, 1], 
                   return_waypoints[:, 2], 'purple', linestyle='--')
        
        # Plot link waypoints if available
        if link_waypoints is not None and len(link_waypoints) > 0:
            link_waypoints = np.array(link_waypoints)
            ax.scatter(link_waypoints[:, 0], link_waypoints[:, 1], 
                      link_waypoints[:, 2], color='cyan', marker='d', 
                      label='Link Waypoints')
            
            # Connect the last optimal waypoint to first link waypoint
            if len(optimal_waypoints) > 0 and len(link_waypoints) > 0:
                connect_points = np.vstack([optimal_waypoints[-1], link_waypoints[0]])
                ax.plot(connect_points[:, 0], connect_points[:, 1], 
                       connect_points[:, 2], 'c--')
            
            # Connect last link waypoint to first remaining waypoint
            if (remaining_waypoints is not None and len(remaining_waypoints) > 0 
                and len(link_waypoints) > 0):
                remaining_waypoints = np.array(remaining_waypoints)
                connect_points = np.vstack([link_waypoints[-1], remaining_waypoints[0]])
                ax.plot(connect_points[:, 0], connect_points[:, 1], 
                       connect_points[:, 2], 'c--')
        
        # Plot remaining waypoints if available
        if remaining_waypoints is not None and len(remaining_waypoints) > 0:
            remaining_waypoints = np.array(remaining_waypoints)
            ax.scatter(remaining_waypoints[:, 0], remaining_waypoints[:, 1], 
                      remaining_waypoints[:, 2], color='orange', 
                      label='Remaining Waypoints')
            
            # Plot trajectory lines for remaining waypoints
            ax.plot(remaining_waypoints[:, 0], remaining_waypoints[:, 1], 
                   remaining_waypoints[:, 2], 'orange', linestyle='-.')
        
        # Add labels and title
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        ax.set_title(title)
        
        # Set equal aspect ratio for the 3D plot
        # Get data limits
        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()
        
        # Calculate range
        x_range = abs(x_limits[1] - x_limits[0])
        y_range = abs(y_limits[1] - y_limits[0])
        z_range = abs(z_limits[1] - z_limits[0])
        
        # Find the maximum range for normalization
        max_range = max(x_range, y_range, z_range)
        
        # Set limits to ensure equal scaling
        x_center = (x_limits[1] + x_limits[0]) / 2
        y_center = (y_limits[1] + y_limits[0]) / 2
        z_center = (z_limits[1] + z_limits[0]) / 2
        
        ax.set_xlim([x_center - max_range/2, x_center + max_range/2])
        ax.set_ylim([y_center - max_range/2, y_center + max_range/2])
        ax.set_zlim([z_center - max_range/2, z_center + max_range/2])
        
        # Add legend
        ax.legend(loc='upper right')
        
        # Add grid
        ax.grid(True)
        
        # Save plot if a path is provided
        if save_path is not None:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        # Show plot if requested
        if show_plot:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, ax
    
    @staticmethod
    def plot_metric_history(metrics: Dict[int, float], 
                           metric_name: str = "Optimization Metric",
                           show_plot: bool = True,
                           save_path: Optional[str] = None):
        """Plot the history of the optimization metric.
        
        Args:
            metrics: Dictionary mapping iteration number to metric value
            metric_name: Name of the metric being plotted
            show_plot: Whether to display the plot
            save_path: Optional path to save the plot
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Extract iterations and metric values
        iterations = list(metrics.keys())
        values = list(metrics.values())
        
        # Create the plot
        ax.plot(iterations, values, 'o-', color='blue', linewidth=2)
        
        # Add annotations for each point
        for i, v in metrics.items():
            ax.annotate(f"{v:.4f}", (i, v), textcoords="offset points", 
                       xytext=(0, 10), ha='center')
        
        # Set labels and title
        ax.set_xlabel('Iteration')
        ax.set_ylabel(f'{metric_name} Value')
        ax.set_title(f'{metric_name} History')
        
        # Add grid
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Set integer ticks for iterations
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
        
        # Save plot if a path is provided
        if save_path is not None:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        # Show plot if requested
        if show_plot:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, ax


class DataLoader:
    """Handles loading and preprocessing of measurement data."""
    
    @staticmethod
    def load_measurement_data_from_csv(path: Union[str, Path]) -> pd.DataFrame:
        """Load measurement data from a CSV file.
        
        Args:
            path: Path to the CSV file
            
        Returns:
            DataFrame with loaded data
        """
        def convert_str_to_list(s: str) -> List:
            """Convert string representation of list to actual list."""
            # Replace 'nan', 'inf', and '-inf' with their numpy constants
            s = s.replace('nan', 'np.nan').replace('inf', 'np.inf').replace('-inf', '-np.inf')
            
            # Evaluate the string as a Python expression
            try:
                return eval(s)
            except Exception as e:
                logger.warning(f"Failed to convert string to list: {e}")
                return s
        
        try:
            data = pd.read_csv(path, header=None, 
                             converters={i: convert_str_to_list for i in range(3)})
            data.columns = ['anchor_position_gt', 'measured_positions', 'measured_ranges']
            return data
        except Exception as e:
            logger.error(f"Error loading data from {path}: {e}")
            raise
    
    @staticmethod
    def sample_measurements(measurements: np.ndarray, 
                         sample_size: Optional[int] = None,
                         random_seed: Optional[int] = None) -> np.ndarray:
        """Sample a subset of measurements.
        
        Args:
            measurements: Array of measurement positions
            sample_size: Number of measurements to sample (None for all)
            random_seed: Optional random seed for reproducibility
            
        Returns:
            Array of sampled measurements
        """
        # If sample_size is None or equal to/greater than available measurements,
        # return all measurements
        if sample_size is None or sample_size >= len(measurements):
            return np.array(measurements)
        
        # Set random seed if provided
        if random_seed is not None:
            np.random.seed(random_seed)
        
        # Sample random indices
        indices = np.random.choice(len(measurements), size=sample_size, replace=False)
        indices.sort()  # Sort for deterministic ordering
        
        return np.array(measurements)[indices]


def main():
    """Main function demonstrating usage of the trajectory optimization system."""
    # Setup logging
    logger.setLevel(logging.INFO)
    
    # Create file handler for logging to file
    log_path = PACKAGE_PATH / 'trajectory_optimization.log'
    file_handler = logging.FileHandler(log_path, mode='w')
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    logger.info("Starting trajectory optimization demonstration")
    
    # Load and prepare data
    try:
        data_loader = DataLoader()
        csv_path = CSV_DIR / 'measurements.csv'
        df = data_loader.load_measurement_data_from_csv(csv_path)
        
        csv_index = 0  # Index of the data row to use
        
        # Get ground truth anchor position and all measurements
        anchor_gt = np.array(df.iloc[csv_index]['anchor_position_gt'])
        all_measurements = np.array(df.iloc[csv_index]['measured_positions'])
        
        # Use 5/6 of measurements to simulate a partially completed mission
        half_length = len(all_measurements) * 5 // 6
        previous_measurements = all_measurements[:half_length]
        
        # Sample a subset of measurements to work with
        sample_size = max(1, len(previous_measurements) // 10)  # Use 10% of measurements
        sampled_measurements = data_loader.sample_measurements(
            previous_measurements, sample_size=sample_size, random_seed=42)
        
        logger.info(f"Loaded {len(all_measurements)} total measurements")
        logger.info(f"Using {len(previous_measurements)} previous measurements")
        logger.info(f"Sampled {len(sampled_measurements)} measurements for optimization")
        
        # Set up optimization parameters
        params = OptimizationParams(
            max_waypoints=8,
            marginal_gain_threshold=0.01,
            radius_of_search=1.0,
            lambda_penalty=10.0
        )
        
        # Set Cartesian bounds for the environment (if applicable)
        # Derive bounds from the range of the data
        min_coords = np.min(all_measurements, axis=0) - 5.0  # Add some margin
        max_coords = np.max(all_measurements, axis=0) + 5.0
        bounds = [
            (min_coords[0], max_coords[0]), 
            (min_coords[1], max_coords[1]), 
            (min_coords[2], max_coords[2])
        ]
        
        # Initialize optimizer
        optimizer = TrajectoryOptimizer(
            metric_type=MetricType.FIM,
            bounds=bounds,
            params=params
        )
        
        # Prepare data for optimization
        initial_position = sampled_measurements[-1]
        target_point = np.array([0, 0, 0])  # Example target return point
        
        # Run optimization
        logger.info("Starting trajectory optimization")
        result = optimizer.optimize_trajectory(
            initial_position=initial_position,
            anchor_estimate=anchor_gt,
            previous_measurements=sampled_measurements,
            target_point=target_point
        )
        
        logger.info(f"Optimization completed: {result.message}")
        logger.info(f"Generated {len(result.optimal_waypoints)} optimal waypoints")
        if result.return_waypoints:
            logger.info(f"Generated {len(result.return_waypoints)} return waypoints")
        
        # Example of computing new mission waypoints
        # Simulate some remaining waypoints from the original mission
        remaining_mission_waypoints = all_measurements[half_length:half_length+5]
        
        # Compute the new mission plan using the HYBRID_RETURN method
        new_mission, optimal_waypoints, link_waypoints, remaining_waypoints = optimizer.compute_new_mission_waypoints(
            initial_position=initial_position,
            initial_remaining_waypoints=remaining_mission_waypoints,
            optimal_waypoints=result.optimal_waypoints,
            method=ReturnTrajectoryMethod.HYBRID_RETURN,
            return_waypoints=result.return_waypoints
        )
        
        logger.info(f"Generated new mission plan with {len(new_mission)} waypoints")
        
        # Visualize results
        visualizer = TrajectoryVisualizer()
        
        # Plot trajectory
        visualizer.plot_trajectory(
            previous_measurements=sampled_measurements,
            anchor_position=anchor_gt,
            optimal_waypoints=optimal_waypoints,
            return_waypoints=result.return_waypoints,
            link_waypoints=link_waypoints,
            remaining_waypoints=remaining_waypoints,
            title="Drone Trajectory Optimization",
            save_path=PACKAGE_PATH / "trajectory_visualization.png"
        )
        
        # Plot metric history
        if result.metrics:
            visualizer.plot_metric_history(
                metrics=result.metrics,
                metric_name="FIM Metric",
                save_path=PACKAGE_PATH / "metric_history.png"
            )
        
        logger.info("Visualization completed")
        logger.info(f"Results saved to {PACKAGE_PATH}")
        
    except Exception as e:
        logger.error(f"Error in trajectory optimization: {e}", exc_info=True)
        raise


if __name__ == '__main__':
    main()