from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Union, Any, ClassVar
import numpy as np
from enum import Enum, auto
import numpy.typing as npt


class AnchorStatus(Enum):
    """Enumeration of possible anchor initialization states."""
    UNSEEN = auto()           # Anchor has not been detected yet
    SEEN = auto()             # Anchor has been detected but not enough measurements
    OPTIMISED_TRAJECTORY = auto()  # Optimal trajectory being executed for this anchor
    STOPPING_CRITERION_TRIGGERED = auto()  # Stopping criterion met, ready for optimization
    INITIALISED = auto()      # Anchor fully initialized


@dataclass
class AnchorData:
    """Structured representation of anchor data during the initialization process.
    
    This dataclass replaces the dictionary structure previously used to store 
    anchor measurements and estimation results, providing type safety and better
    code organization.
    """
    # Identity and status
    anchor_id: str
    status: AnchorStatus = AnchorStatus.UNSEEN
    
    # Measurements before rough estimation
    distances_pre_rough_estimate: List[float] = field(default_factory=list)
    positions_pre_rough_estimate: List[Tuple[float, float, float]] = field(default_factory=list)
    
    # Measurements after rough estimation (during optimal trajectory)
    distances_post_rough_estimate: List[float] = field(default_factory=list)
    positions_post_rough_estimate: List[Tuple[float, float, float]] = field(default_factory=list)
    
    # Linear estimator results
    estimator_rough_linear: np.ndarray = field(default_factory=lambda: np.array([0.0, 0.0, 0.0, 0.0, 1.0]))
    covariance_matrix_rough_linear: np.ndarray = field(default_factory=lambda: np.array([]))
    linear_ls_weights: List[List[float]] = field(default_factory=lambda: [[]])
    linear_ls_outlier_counter: List[float] = field(default_factory=list)
    
    # Non-linear estimator results
    estimator_rough_non_linear: np.ndarray = field(default_factory=lambda: np.array([0.0, 0.0, 0.0, 0.0, 0.0]))
    covariance_matrix_rough_non_linear: np.ndarray = field(default_factory=lambda: np.array([]))
    
    # Final estimator (continuously updated)
    estimator: np.ndarray = field(default_factory=lambda: np.array([0.0, 0.0, 0.0, 0.0, 0.0]))
    covariance_matrix: np.ndarray = field(default_factory=lambda: np.array([]))
    
    # Quality metrics for stopping criteria
    FIM: List[np.ndarray] = field(default_factory=list)
    GDOP: List[float] = field(default_factory=list)
    residuals: List[float] = field(default_factory=list)
    condition_number: List[float] = field(default_factory=list)
    covariances: List[np.ndarray] = field(default_factory=list)
    verification_vector: List[float] = field(default_factory=list)
    residual_vector: List[np.ndarray] = field(default_factory=list)
    consecutive_distances_vector: List[float] = field(default_factory=list)
    
    # Convergence counters for stopping criteria
    FIM_convergence_counter: int = 0
    GDOP_convergence_counter: int = 0
    residuals_convergence_counter: int = 0
    condition_number_convergence_counter: int = 0
    covariances_convergence_counter: int = 0
    verification_vector_convergence_counter: int = 0
    consecutive_distances_vector_convergence_counter: int = 0
    
    # Gaussian Mixture Model results
    GMM: List[Any] = field(default_factory=list)
    
    # Optimal trajectory data
    optimal_waypoints: List[Tuple[float, float, float]] = field(default_factory=list)
    
    @property
    def position(self) -> np.ndarray:
        """Get the current estimated position of the anchor."""
        return self.estimator[:3]
    
    @property
    def bias(self) -> float:
        """Get the current estimated constant bias."""
        return float(self.estimator[3])
    
    @property
    def linear_bias(self) -> float:
        """Get the current estimated linear bias."""
        return float(self.estimator[4])
    
    @property
    def num_measurements_pre_estimation(self) -> int:
        """Get the number of measurements collected before rough estimation."""
        return len(self.distances_pre_rough_estimate)
    
    @property
    def num_measurements_post_estimation(self) -> int:
        """Get the number of measurements collected after rough estimation."""
        return len(self.distances_post_rough_estimate)
    
    @property
    def total_measurements(self) -> int:
        """Get the total number of measurements collected for this anchor."""
        return self.num_measurements_pre_estimation + self.num_measurements_post_estimation
    
    def get_all_measurements(self) -> List[Tuple[float, float, float, float]]:
        """Get all measurements formatted as [x, y, z, distance] tuples."""
        measurements = []
        
        # Add pre-rough estimate measurements
        for dist, pos in zip(self.distances_pre_rough_estimate, self.positions_pre_rough_estimate):
            measurements.append((*pos, dist))
            
        # Add post-rough estimate measurements
        for dist, pos in zip(self.distances_post_rough_estimate, self.positions_post_rough_estimate):
            measurements.append((*pos, dist))
            
        return measurements
    
    def add_pre_estimate_measurement(self, position: Tuple[float, float, float], distance: float) -> None:
        """Add a measurement collected before rough estimation."""
        self.distances_pre_rough_estimate.append(distance)
        self.positions_pre_rough_estimate.append(position)
    
    def add_post_estimate_measurement(self, position: Tuple[float, float, float], distance: float) -> None:
        """Add a measurement collected after rough estimation (during optimal trajectory)."""
        self.distances_post_rough_estimate.append(distance)
        self.positions_post_rough_estimate.append(position)
    
    def append_quality_metrics(self, fim: np.ndarray, gdop: float, residual: float, 
                              cond_num: float, covar: np.ndarray, verification: float,
                              residuals: np.ndarray, distance_delta: float) -> None:
        """Append quality metrics used for stopping criteria."""
        self.FIM.append(fim)
        self.GDOP.append(gdop)
        self.residuals.append(residual)
        self.condition_number.append(cond_num)
        self.covariances.append(covar)
        self.verification_vector.append(verification)
        self.residual_vector.append(residuals)
        self.consecutive_distances_vector.append(distance_delta)
    
    def append_placeholder_metrics(self) -> None:
        """Append placeholder metrics when not enough measurements are available."""
        self.FIM.append(np.zeros((5, 5)))
        self.GDOP.append(float('inf'))
        self.residuals.append(float('inf'))
        self.condition_number.append(float('inf'))
        self.covariances.append(np.array([float('inf')] * 3))
        self.verification_vector.append(float('inf'))
        self.residual_vector.append(np.array([]))
        self.consecutive_distances_vector.append(float('inf'))
        self.linear_ls_weights.append([])
    
    def update_estimator(self, new_estimator: np.ndarray, new_covariance: np.ndarray, is_non_linear: bool = False) -> None:
        """Update the estimator with new values."""
        self.estimator = new_estimator.copy()
        self.covariance_matrix = new_covariance.copy()
        
        if not is_non_linear:
            self.estimator_rough_linear = new_estimator.copy()
            self.covariance_matrix_rough_linear = new_covariance.copy()
        else:
            self.estimator_rough_non_linear = new_estimator.copy()
            self.covariance_matrix_rough_non_linear = new_covariance.copy()
    
    def reset_post_estimate_measurements(self) -> None:
        """Reset measurements collected after rough estimation."""
        self.distances_post_rough_estimate = []
        self.positions_post_rough_estimate = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the anchor data to a dictionary format compatible with the original code."""
        return {
            "status": self.status.name.lower(),
            "distances_pre_rough_estimate": self.distances_pre_rough_estimate,
            "positions_pre_rough_estimate": self.positions_pre_rough_estimate,
            "distances_post_rough_estimate": self.distances_post_rough_estimate,
            "positions_post_rough_estimate": self.positions_post_rough_estimate,
            "estimator_rough_linear": self.estimator_rough_linear,
            "covariance_matrix_rough_linear": self.covariance_matrix_rough_linear,
            "linear_ls_weights": self.linear_ls_weights,
            "linear_ls_outlier_counter": self.linear_ls_outlier_counter,
            "estimator_rough_non_linear": self.estimator_rough_non_linear,
            "covariance_matrix_rough_non_linear": self.covariance_matrix_rough_non_linear,
            "estimator": self.estimator,
            "covariance_matrix": self.covariance_matrix,
            "FIM": self.FIM,
            "GDOP": self.GDOP,
            "residuals": self.residuals,
            "condition_number": self.condition_number,
            "covariances": self.covariances,
            "verification_vector": self.verification_vector,
            "residual_vector": self.residual_vector,
            "consecutive_distances_vector": self.consecutive_distances_vector,
            "FIM_convergence_counter": self.FIM_convergence_counter,
            "GDOP_convergence_counter": self.GDOP_convergence_counter,
            "residuals_convergence_counter": self.residuals_convergence_counter,
            "condition_number_convergence_counter": self.condition_number_convergence_counter,
            "covariances_convergence_counter": self.covariances_convergence_counter,
            "verification_vector_convergence_counter": self.verification_vector_convergence_counter,
            "consecutive_distances_vector_convergence_counter": self.consecutive_distances_vector_convergence_counter,
            "GMM": self.GMM,
            "optimal_waypoints": self.optimal_waypoints
        }
    
    @classmethod
    def from_dict(cls, anchor_id: str, data_dict: Dict[str, Any]) -> 'AnchorData':
        """Create an AnchorData instance from a dictionary, for compatibility with the original code."""
        status_str = data_dict.get("status", "unseen")
        try:
            status = AnchorStatus[status_str.upper()]
        except KeyError:
            status = AnchorStatus.UNSEEN
            
        anchor_data = cls(anchor_id=anchor_id, status=status)
        
        # Copy values from dictionary
        anchor_data.distances_pre_rough_estimate = data_dict.get("distances_pre_rough_estimate", [])
        anchor_data.positions_pre_rough_estimate = data_dict.get("positions_pre_rough_estimate", [])
        anchor_data.distances_post_rough_estimate = data_dict.get("distances_post_rough_estimate", [])
        anchor_data.positions_post_rough_estimate = data_dict.get("positions_post_rough_estimate", [])
        anchor_data.estimator_rough_linear = np.array(data_dict.get("estimator_rough_linear", [0.0, 0.0, 0.0, 0.0, 1.0]))
        anchor_data.covariance_matrix_rough_linear = np.array(data_dict.get("covariance_matrix_rough_linear", []))
        anchor_data.linear_ls_weights = data_dict.get("linear_ls_weights", [[]])
        anchor_data.linear_ls_outlier_counter = data_dict.get("linear_ls_outlier_counter", [])
        anchor_data.estimator_rough_non_linear = np.array(data_dict.get("estimator_rough_non_linear", [0.0, 0.0, 0.0, 0.0, 0.0]))
        anchor_data.covariance_matrix_rough_non_linear = np.array(data_dict.get("covariance_matrix_rough_non_linear", []))
        anchor_data.estimator = np.array(data_dict.get("estimator", [0.0, 0.0, 0.0, 0.0, 0.0]))
        anchor_data.covariance_matrix = np.array(data_dict.get("covariance_matrix", []))
        anchor_data.FIM = data_dict.get("FIM", [])
        anchor_data.GDOP = data_dict.get("GDOP", [])
        anchor_data.residuals = data_dict.get("residuals", [])
        anchor_data.condition_number = data_dict.get("condition_number", [])
        anchor_data.covariances = data_dict.get("covariances", [])
        anchor_data.verification_vector = data_dict.get("verification_vector", [])
        anchor_data.residual_vector = data_dict.get("residual_vector", [])
        anchor_data.consecutive_distances_vector = data_dict.get("consecutive_distances_vector", [])
        anchor_data.FIM_convergence_counter = data_dict.get("FIM_convergence_counter", 0)
        anchor_data.GDOP_convergence_counter = data_dict.get("GDOP_convergence_counter", 0)
        anchor_data.residuals_convergence_counter = data_dict.get("residuals_convergence_counter", 0)
        anchor_data.condition_number_convergence_counter = data_dict.get("condition_number_convergence_counter", 0)
        anchor_data.covariances_convergence_counter = data_dict.get("covariances_convergence_counter", 0)
        anchor_data.verification_vector_convergence_counter = data_dict.get("verification_vector_convergence_counter", 0)
        anchor_data.consecutive_distances_vector_convergence_counter = data_dict.get("consecutive_distances_vector_convergence_counter", 0)
        anchor_data.GMM = data_dict.get("GMM", [])
        anchor_data.optimal_waypoints = data_dict.get("optimal_waypoints", [])
        
        return anchor_data