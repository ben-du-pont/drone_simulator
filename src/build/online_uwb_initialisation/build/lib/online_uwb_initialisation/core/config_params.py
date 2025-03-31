from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Union, Any, Set
import logging
from enum import Enum, auto
import numpy as np

# Set up logging
logger = logging.getLogger(__name__)


class OutlierRemovalMethod(Enum):
    """Enumeration of outlier removal methods."""
    NONE = auto()
    COUNTER = auto()
    IMMEDIATE = auto()
    
    @classmethod
    def from_string(cls, method_str: str) -> 'OutlierRemovalMethod':
        """Convert a string to an OutlierRemovalMethod enum.
        
        Args:
            method_str: String representation of the method
            
        Returns:
            Corresponding OutlierRemovalMethod enum value
        """
        method_upper = method_str.upper()
        if method_upper == "NONE":
            return cls.NONE
        elif method_upper == "COUNTER":
            return cls.COUNTER
        elif method_upper == "IMMEDIATE":
            return cls.IMMEDIATE
        else:
            logger.warning(f"Unknown outlier removal method: {method_str}, using NONE")
            return cls.NONE


class RoughEstimateMethod(Enum):
    """Enumeration of methods for rough estimation."""
    SIMPLE_LINEAR = auto()
    LINEAR_REWEIGHTED = auto()
    EM_ALGORITHM = auto()
    
    @classmethod
    def from_string(cls, method_str: str) -> 'RoughEstimateMethod':
        """Convert a string to a RoughEstimateMethod enum.
        
        Args:
            method_str: String representation of the method
            
        Returns:
            Corresponding RoughEstimateMethod enum value
        """
        method_upper = method_str.upper()
        if method_upper == "SIMPLE_LINEAR":
            return cls.SIMPLE_LINEAR
        elif method_upper == "LINEAR_REWEIGHTED":
            return cls.LINEAR_REWEIGHTED
        else:
            logger.warning(f"Unknown rough estimate method: {method_str}, using LINEAR_REWEIGHTED")
            return cls.LINEAR_REWEIGHTED


class NonLinearOptimizationType(Enum):
    """Enumeration of nonlinear optimization methods."""
    LM = auto()
    IRLS = auto()
    KRR = auto()  # Kernel Ridge Regression (Was quite bad, not used)
    GMM = auto()   # Gaussian Mixture Model
    EM = auto()   # Expectation-Maximization
    
    @classmethod
    def from_string(cls, method_str: str) -> 'NonLinearOptimizationType':
        """Convert a string to a NonLinearOptimizationType enum.
        
        Args:
            method_str: String representation of the method
            
        Returns:
            Corresponding NonLinearOptimizationType enum value
        """
        method_upper = method_str.upper()
        if method_upper == "IRLS":
            return cls.IRLS
        elif method_upper == "LM":
            return cls.LM
        elif method_upper == "KRR":
            return cls.KRR
        elif method_upper == "GMM" or method_upper == "GAUSSIAN_MIXTURE_MODEL":
            return cls.GMM
        elif method_upper == "EM" or method_upper == "EM_NEW":
            return cls.EM
        else:
            logger.warning(f"Unknown nonlinear optimization type: {method_str}, using GMM")
            return cls.GMM


class TrajectoryOptimizationMethod(Enum):
    """Enumeration of trajectory optimization methods."""
    GDOP = auto()
    FIM = auto()
    
    @classmethod
    def from_string(cls, method_str: str) -> 'TrajectoryOptimizationMethod':
        """Convert a string to a TrajectoryOptimizationMethod enum.
        
        Args:
            method_str: String representation of the method
            
        Returns:
            Corresponding TrajectoryOptimizationMethod enum value
        """
        method_upper = method_str.upper()
        if method_upper == "GDOP":
            return cls.GDOP
        elif method_upper == "FIM":
            return cls.FIM
        else:
            logger.warning(f"Unknown trajectory optimization method: {method_str}, using GDOP")
            return cls.GDOP


class LinkMethod(Enum):
    """Enumeration of methods for linking trajectory segments."""
    STRICT_RETURN = auto() 
    RETURN_TO_INITIAL = auto()
    STRAIGHT_TO_WAYPOINT = auto()
    RETURN_TO_CLOSEST = auto()
    HYBRID_RETURN = auto()
    OPTIMAL = auto()
    
    @classmethod
    def from_string(cls, method_str: str) -> 'LinkMethod':
        """Convert a string to a LinkMethod enum.
        
        Args:
            method_str: String representation of the method
            
        Returns:
            Corresponding LinkMethod enum value
        """
        method_upper = method_str.upper()
        if method_upper == "STRICT_RETURN":
            return cls.STRICT_RETURN
        elif method_upper == "RETURN_TO_INITIAL":
            return cls.RETURN_TO_INITIAL
        elif method_upper == "STRAIGHT_TO_WAYPOINT":
            return cls.STRAIGHT_TO_WAYPOINT
        elif method_upper == "RETURN_TO_CLOSEST":
            return cls.RETURN_TO_CLOSEST
        elif method_upper == "HYBRID_RETURN":
            return cls.HYBRID_RETURN
        elif method_upper == "OPTIMAL":
            return cls.OPTIMAL
        else:
            logger.warning(f"Unknown link method: {method_str}, using STRICT_RETURN")
            return cls.STRICT_RETURN


@dataclass
class MeasurementConfig:
    """Configuration for measurement gathering."""
    distance_to_anchor_ratio_threshold: float = 0.03
    """Tangent ratio between consecutive measurements; smaller means more measurements."""
    
    number_of_redundant_measurements: int = 1
    """Number of measurements to take at the same place, ignoring the angle condition."""
    
    distance_rejection_threshold: float = 20.0
    """Maximum distance to the anchor to accept the measurement."""


@dataclass
class LeastSquaresConfig:
    """Configuration for least squares estimation."""
    use_linear_bias: bool = False
    """Use linear bias in the linear least squares."""
    
    use_constant_bias: bool = True
    """Use constant bias in the linear least squares."""
    
    normalised: bool = False
    """Use the normalised formulation for the linear least squares."""
    
    regularise: bool = True
    """Regularize the least squares problem to keep the biases small."""
    
    rough_estimate_method: RoughEstimateMethod = field(default_factory=lambda: RoughEstimateMethod.LINEAR_REWEIGHTED)
    """Method to use for the rough estimate."""
    
    outlier_removing: OutlierRemovalMethod = field(default_factory=lambda: OutlierRemovalMethod.NONE)
    """Method to use for outlier removal."""
    
    reweighting_iterations: int = 4
    """Number of reweighting iterations for the reweighted least squares."""
    
    use_trimmed_reweighted: bool = True
    """Use trimmed reweighted least squares for the rough estimate."""
    
    weighting_function: str = "mad"
    """Method for the reweighting of the linear least squares problem."""
    
    huber_delta: float = 0.01
    """Parameter for Huber weighting function."""
    
    tukey_c: float = 4.685
    """Parameter for Tukey weighting function."""
    
    welsch_c: float = 2.0
    """Parameter for Welsch weighting function."""
    
    non_linear_optimisation_type: NonLinearOptimizationType = field(
        default_factory=lambda: NonLinearOptimizationType.GMM
    )
    """Type of non-linear optimization to use."""


@dataclass
class StoppingCriteriaConfig:
    """Configuration for stopping criteria."""
    stopping_criteria: List[str] = field(default_factory=lambda: ["nb_measurements"])
    """List of criteria to use for determining when to stop collecting measurements."""
    
    # Absolute thresholds
    FIM_thresh: float = 1e5
    """Threshold for the Fisher Information Matrix."""
    
    GDOP_thresh: float = 3.0
    """Threshold for the Geometric Dilution of Precision."""
    
    residuals_thresh: float = 100.0
    """Threshold for the residuals."""
    
    condition_number_thresh: float = 5e5
    """Threshold for the condition number."""
    
    covariance_thresh: float = 10.0
    """Threshold for the covariance."""
    
    internal_constraint_thresh: float = 10.0
    """Threshold for the internal constraint."""
    
    number_of_measurements_thresh: int = 30
    """Threshold for the number of measurements."""
    
    # Relative thresholds
    FIM_ratio_thresh: float = 1.0
    """Threshold for the ratio of consecutive FIM values."""
    
    GDOP_ratio_thresh: float = 0.2
    """Threshold for the ratio of consecutive GDOP values."""
    
    residuals_ratio_thresh: float = 1.0
    """Threshold for the ratio of consecutive residuals values."""
    
    condition_number_ratio_thresh: float = 0.1
    """Threshold for the ratio of consecutive condition number values."""
    
    covariance_ratio_thresh: float = 1.0
    """Threshold for the ratio of consecutive covariance values."""
    
    convergence_postion_thresh: float = 1.0
    """Threshold for the change in position estimate."""
    
    internal_constraint_ratio_thresh: float = 0.1
    """Threshold for the ratio of consecutive internal constraint values."""
    
    # Convergence counters
    convergence_counter_threshold: int = 3
    """Number of consecutive times a criterion must be met to trigger convergence."""


@dataclass
class OutlierConfig:
    """Configuration for outlier rejection."""
    z_score_threshold: float = 2.0
    """Z-score threshold for outlier detection."""
    
    outlier_count_threshold: int = 3
    """Number of consecutive outlier classifications to remove a measurement when using the counter method."""


@dataclass
class TrajectoryConfig:
    """Configuration for trajectory optimization."""
    trajectory_optimisation_method: TrajectoryOptimizationMethod = field(
        default_factory=lambda: TrajectoryOptimizationMethod.FIM
    )
    """Method to use for trajectory optimization."""
    
    link_method: LinkMethod = field(default_factory=lambda: LinkMethod.STRICT_RETURN)
    """Method to use for linking trajectory segments."""

    bounds: np.ndarray = field(default_factory=lambda: np.array([
        [-float('inf'), float('inf')],  # x bounds
        [-float('inf'), float('inf')],  # y bounds
        [-float('inf'), float('inf')]   # z bounds
    ]))
    """3x2 matrix of bounds for [x,y,z] coordinates, where each row is [min, max]"""

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'TrajectoryConfig':
        """Create a TrajectoryConfig from a dictionary."""
        # Handle trajectory optimization method
        method_str = config_dict.get('trajectory_optimisation_method', 'GDOP').upper()
        try:
            method = TrajectoryOptimizationMethod[method_str]
        except KeyError:
            logger.warning(f"Invalid trajectory optimization method: {method_str}. Using GDOP.")
            method = TrajectoryOptimizationMethod.GDOP

        # Handle link method
        link_str = config_dict.get('link_method', 'STRAIGHT').upper()
        try:
            link = LinkMethod[link_str]
        except KeyError:
            logger.warning(f"Invalid link method: {link_str}. Using STRAIGHT.")
            link = LinkMethod.STRAIGHT

        # Handle bounds
        default_bounds = np.array([
            [-5.0, 5.0],  # x bounds
            [-5.0, 5.0],  # y bounds
            [0.0, 2.0]    # z bounds
        ])

        bounds = config_dict.get('bounds', default_bounds)
        try:
            bounds = np.array(bounds, dtype=float)
            if bounds.shape != (3, 2):
                logger.warning(f"Invalid bounds shape {bounds.shape}. Expected (3, 2). Using default bounds.")
                bounds = default_bounds
        except (ValueError, TypeError):
            logger.warning("Invalid bounds format. Using default bounds.")
            bounds = default_bounds

        return cls(
            trajectory_optimisation_method=method,
            link_method=link,
            bounds=bounds
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the config to a dictionary."""
        return {
            'trajectory_optimisation_method': self.trajectory_optimisation_method.name,
            'link_method': self.link_method.name,
            'bounds': self.bounds.tolist()  # Convert numpy array to nested list for JSON serialization
        }


@dataclass
class UwbInitializationConfig:
    """Master configuration class for UWB initialization pipeline."""
    measurement: MeasurementConfig = field(default_factory=MeasurementConfig)
    """Configuration for measurement gathering."""
    
    least_squares: LeastSquaresConfig = field(default_factory=LeastSquaresConfig)
    """Configuration for least squares estimation."""
    
    stopping_criteria: StoppingCriteriaConfig = field(default_factory=StoppingCriteriaConfig)
    """Configuration for stopping criteria."""
    
    outlier: OutlierConfig = field(default_factory=OutlierConfig)
    """Configuration for outlier rejection."""
    
    trajectory: TrajectoryConfig = field(default_factory=TrajectoryConfig)
    """Configuration for trajectory optimization."""
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'UwbInitializationConfig':
        """Create a UwbInitializationConfig from a flat dictionary of parameters.
        
        This method converts a flat dictionary as used in the original code to
        the structured configuration objects.
        
        Args:
            config_dict: Dictionary of configuration parameters
            
        Returns:
            Initialized UwbInitializationConfig
        """
        # Create default configuration
        config = cls()
        
        # Measurement gathering parameters
        if 'measurement.distance_to_anchor_ratio_threshold' in config_dict:
            config.measurement.distance_to_anchor_ratio_threshold = config_dict['measurement.distance_to_anchor_ratio_threshold']
        if 'measurement.number_of_redundant_measurements' in config_dict:
            config.measurement.number_of_redundant_measurements = config_dict['measurement.number_of_redundant_measurements']
        if 'measurement.distance_rejection_threshold' in config_dict:
            config.measurement.distance_rejection_threshold = config_dict['measurement.distance_rejection_threshold']
        
        # Least squares parameters
        if 'least_squares.use_linear_bias' in config_dict:
            config.least_squares.use_linear_bias = config_dict['least_squares.use_linear_bias']
        if 'least_squares.use_constant_bias' in config_dict:
            config.least_squares.use_constant_bias = config_dict['least_squares.use_constant_bias']
        if 'least_squares.normalised' in config_dict:
            config.least_squares.normalised = config_dict['least_squares.normalised']
        if 'least_squares.regularise' in config_dict:
            config.least_squares.regularise = config_dict['least_squares.regularise']
        if 'least_squares.rough_estimate_method' in config_dict:
            config.least_squares.rough_estimate_method = RoughEstimateMethod.from_string(
                config_dict['least_squares.rough_estimate_method']
            )
        if 'least_squares.outlier_removing' in config_dict:
            config.least_squares.outlier_removing = OutlierRemovalMethod.from_string(
                config_dict['least_squares.outlier_removing']
            )
        if 'least_squares.reweighting_iterations' in config_dict:
            config.least_squares.reweighting_iterations = config_dict['least_squares.reweighting_iterations']
        if 'least_squares.use_trimmed_reweighted' in config_dict:
            config.least_squares.use_trimmed_reweighted = config_dict['least_squares.use_trimmed_reweighted']
        if 'least_squares.weighting_function' in config_dict:
            config.least_squares.weighting_function = config_dict['least_squares.weighting_function']
        if 'least_squares.huber_delta' in config_dict:
            config.least_squares.huber_delta = config_dict['least_squares.huber_delta']
        if 'least_squares.tukey_c' in config_dict:
            config.least_squares.tukey_c = config_dict['least_squares.tukey_c']
        if 'least_squares.welsch_c' in config_dict:
            config.least_squares.welsch_c = config_dict['least_squares.welsch_c']
        if 'least_squares.non_linear_optimisation_type' in config_dict:
            config.least_squares.non_linear_optimisation_type = NonLinearOptimizationType.from_string(
                config_dict['least_squares.non_linear_optimisation_type']
            )
        
        # Stopping criteria parameters
        if 'stopping_criteria.stopping_criteria' in config_dict:
            config.stopping_criteria.stopping_criteria = config_dict['stopping_criteria.stopping_criteria']
        if 'stopping_criteria.FIM_thresh' in config_dict:
            config.stopping_criteria.FIM_thresh = config_dict['stopping_criteria.FIM_thresh']
        if 'stopping_criteria.GDOP_thresh' in config_dict:
            config.stopping_criteria.GDOP_thresh = config_dict['stopping_criteria.GDOP_thresh']
        if 'stopping_criteria.residuals_thresh' in config_dict:
            config.stopping_criteria.residuals_thresh = config_dict['stopping_criteria.residuals_thresh']
        if 'stopping_criteria.condition_number_thresh' in config_dict:
            config.stopping_criteria.condition_number_thresh = config_dict['stopping_criteria.condition_number_thresh']
        if 'stopping_criteria.covariance_thresh' in config_dict:
            config.stopping_criteria.covariance_thresh = config_dict['stopping_criteria.covariance_thresh']
        if 'stopping_criteria.internal_constraint_thresh' in config_dict:
            config.stopping_criteria.internal_constraint_thresh = config_dict['stopping_criteria.internal_constraint_thresh']
        if 'stopping_criteria.number_of_measurements_thresh' in config_dict:
            config.stopping_criteria.number_of_measurements_thresh = config_dict['stopping_criteria.number_of_measurements_thresh']
        if 'stopping_criteria.FIM_ratio_thresh' in config_dict:
            config.stopping_criteria.FIM_ratio_thresh = config_dict['stopping_criteria.FIM_ratio_thresh']
        if 'stopping_criteria.GDOP_ratio_thresh' in config_dict:
            config.stopping_criteria.GDOP_ratio_thresh = config_dict['stopping_criteria.GDOP_ratio_thresh']
        if 'stopping_criteria.residuals_ratio_thresh' in config_dict:
            config.stopping_criteria.residuals_ratio_thresh = config_dict['stopping_criteria.residuals_ratio_thresh']
        if 'stopping_criteria.condition_number_ratio_thresh' in config_dict:
            config.stopping_criteria.condition_number_ratio_thresh = config_dict['stopping_criteria.condition_number_ratio_thresh']
        if 'stopping_criteria.covariance_ratio_thresh' in config_dict:
            config.stopping_criteria.covariance_ratio_thresh = config_dict['stopping_criteria.covariance_ratio_thresh']
        if 'stopping_criteria.convergence_postion_thresh' in config_dict:
            config.stopping_criteria.convergence_postion_thresh = config_dict['stopping_criteria.convergence_postion_thresh']
        if 'stopping_criteria.internal_constraint_ratio_thresh' in config_dict:
            config.stopping_criteria.internal_constraint_ratio_thresh = config_dict['stopping_criteria.internal_constraint_ratio_thresh']
        if 'stopping_criteria.convergence_counter_threshold' in config_dict:
            config.stopping_criteria.convergence_counter_threshold = config_dict['stopping_criteria.convergence_counter_threshold']
        
        # Outlier rejection parameters
        if 'outlier.z_score_threshold' in config_dict:
            config.outlier.z_score_threshold = config_dict['outlier.z_score_threshold']
        if 'outlier.outlier_count_threshold' in config_dict:
            config.outlier.outlier_count_threshold = config_dict['outlier.outlier_count_threshold']
        
        # Trajectory parameters
        if 'trajectory.trajectory_optimisation_method' in config_dict:
            config.trajectory.trajectory_optimisation_method = TrajectoryOptimizationMethod.from_string(
                config_dict['trajectory.trajectory_optimisation_method']
            )
        if 'trajectory.link_method' in config_dict:
            config.trajectory.link_method = LinkMethod.from_string(
                config_dict['trajectory.link_method']
            )
        if 'trajectory.bounds' in config_dict:
            config.trajectory.bounds = np.array(config_dict['trajectory.bounds'])
        
        return config
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the configuration to a flat dictionary.
        
        Returns:
            Dictionary of configuration parameters in a flat structure with namespaces
        """
        return {
            # Measurement gathering parameters
            'measurement.distance_to_anchor_ratio_threshold': self.measurement.distance_to_anchor_ratio_threshold,
            'measurement.number_of_redundant_measurements': self.measurement.number_of_redundant_measurements,
            'measurement.distance_rejection_threshold': self.measurement.distance_rejection_threshold,
            
            # Least squares parameters
            'least_squares.use_linear_bias': self.least_squares.use_linear_bias,
            'least_squares.use_constant_bias': self.least_squares.use_constant_bias,
            'least_squares.normalised': self.least_squares.normalised,
            'least_squares.regularise': self.least_squares.regularise,
            'least_squares.rough_estimate_method': self.least_squares.rough_estimate_method.name.lower(),
            'least_squares.outlier_removing': self.least_squares.outlier_removing.name.lower(),
            'least_squares.reweighting_iterations': self.least_squares.reweighting_iterations,
            'least_squares.use_trimmed_reweighted': self.least_squares.use_trimmed_reweighted,
            'least_squares.weighting_function': self.least_squares.weighting_function,
            'least_squares.huber_delta': self.least_squares.huber_delta,
            'least_squares.tukey_c': self.least_squares.tukey_c,
            'least_squares.welsch_c': self.least_squares.welsch_c,
            'least_squares.non_linear_optimisation_type': self.least_squares.non_linear_optimisation_type.name,
            
            # Stopping criteria parameters
            'stopping_criteria.stopping_criteria': self.stopping_criteria.stopping_criteria,
            'stopping_criteria.FIM_thresh': self.stopping_criteria.FIM_thresh,
            'stopping_criteria.GDOP_thresh': self.stopping_criteria.GDOP_thresh,
            'stopping_criteria.residuals_thresh': self.stopping_criteria.residuals_thresh,
            'stopping_criteria.condition_number_thresh': self.stopping_criteria.condition_number_thresh,
            'stopping_criteria.covariance_thresh': self.stopping_criteria.covariance_thresh,
            'stopping_criteria.internal_constraint_thresh': self.stopping_criteria.internal_constraint_thresh,
            'stopping_criteria.number_of_measurements_thresh': self.stopping_criteria.number_of_measurements_thresh,
            'stopping_criteria.FIM_ratio_thresh': self.stopping_criteria.FIM_ratio_thresh,
            'stopping_criteria.GDOP_ratio_thresh': self.stopping_criteria.GDOP_ratio_thresh,
            'stopping_criteria.residuals_ratio_thresh': self.stopping_criteria.residuals_ratio_thresh,
            'stopping_criteria.condition_number_ratio_thresh': self.stopping_criteria.condition_number_ratio_thresh,
            'stopping_criteria.covariance_ratio_thresh': self.stopping_criteria.covariance_ratio_thresh,
            'stopping_criteria.convergence_postion_thresh': self.stopping_criteria.convergence_postion_thresh,
            'stopping_criteria.internal_constraint_ratio_thresh': self.stopping_criteria.internal_constraint_ratio_thresh,
            'stopping_criteria.convergence_counter_threshold': self.stopping_criteria.convergence_counter_threshold,
            
            # Outlier rejection parameters
            'outlier.z_score_threshold': self.outlier.z_score_threshold,
            'outlier.outlier_count_threshold': self.outlier.outlier_count_threshold,
            
            # Trajectory parameters
            'trajectory.trajectory_optimisation_method': self.trajectory.trajectory_optimisation_method.name,
            'trajectory.link_method': self.trajectory.link_method.name.lower(),
            'trajectory.bounds': self.trajectory.bounds.tolist(),
        }