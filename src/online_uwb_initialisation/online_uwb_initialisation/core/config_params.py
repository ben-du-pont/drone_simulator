from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Union, Any, Set
import logging
from enum import Enum, auto

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
        if 'distance_to_anchor_ratio_threshold' in config_dict:
            config.measurement.distance_to_anchor_ratio_threshold = config_dict['distance_to_anchor_ratio_threshold']
        if 'number_of_redundant_measurements' in config_dict:
            config.measurement.number_of_redundant_measurements = config_dict['number_of_redundant_measurements']
        if 'distance_rejection_threshold' in config_dict:
            config.measurement.distance_rejection_threshold = config_dict['distance_rejection_threshold']
        
        # Least squares parameters
        if 'use_linear_bias' in config_dict:
            config.least_squares.use_linear_bias = config_dict['use_linear_bias']
        if 'use_constant_bias' in config_dict:
            config.least_squares.use_constant_bias = config_dict['use_constant_bias']
        if 'normalised' in config_dict:
            config.least_squares.normalised = config_dict['normalised']
        if 'regularise' in config_dict:
            config.least_squares.regularise = config_dict['regularise']
        if 'rough_estimate_method' in config_dict:
            config.least_squares.rough_estimate_method = RoughEstimateMethod.from_string(
                config_dict['rough_estimate_method']
            )
        if 'outlier_removing' in config_dict:
            config.least_squares.outlier_removing = OutlierRemovalMethod.from_string(
                config_dict['outlier_removing']
            )
        if 'reweighting_iterations' in config_dict:
            config.least_squares.reweighting_iterations = config_dict['reweighting_iterations']
        if 'use_trimmed_reweighted' in config_dict:
            config.least_squares.use_trimmed_reweighted = config_dict['use_trimmed_reweighted']
        if 'weighting_function' in config_dict:
            config.least_squares.weighting_function = config_dict['weighting_function']
        if 'huber_delta' in config_dict:
            config.least_squares.huber_delta = config_dict['huber_delta']
        if 'tukey_c' in config_dict:
            config.least_squares.tukey_c = config_dict['tukey_c']
        if 'welsch_c' in config_dict:
            config.least_squares.welsch_c = config_dict['welsch_c']
        if 'non_linear_optimisation_type' in config_dict:
            config.least_squares.non_linear_optimisation_type = NonLinearOptimizationType.from_string(
                config_dict['non_linear_optimisation_type']
            )
        
        # Stopping criteria parameters
        if 'stopping_criteria' in config_dict:
            config.stopping_criteria.stopping_criteria = config_dict['stopping_criteria']
        if 'FIM_thresh' in config_dict:
            config.stopping_criteria.FIM_thresh = config_dict['FIM_thresh']
        if 'GDOP_thresh' in config_dict:
            config.stopping_criteria.GDOP_thresh = config_dict['GDOP_thresh']
        if 'residuals_thresh' in config_dict:
            config.stopping_criteria.residuals_thresh = config_dict['residuals_thresh']
        if 'condition_number_thresh' in config_dict:
            config.stopping_criteria.condition_number_thresh = config_dict['condition_number_thresh']
        if 'covariance_thresh' in config_dict:
            config.stopping_criteria.covariance_thresh = config_dict['covariance_thresh']
        if 'internal_constraint_thresh' in config_dict:
            config.stopping_criteria.internal_constraint_thresh = config_dict['internal_constraint_thresh']
        if 'number_of_measurements_thresh' in config_dict:
            config.stopping_criteria.number_of_measurements_thresh = config_dict['number_of_measurements_thresh']
        if 'FIM_ratio_thresh' in config_dict:
            config.stopping_criteria.FIM_ratio_thresh = config_dict['FIM_ratio_thresh']
        if 'GDOP_ratio_thresh' in config_dict:
            config.stopping_criteria.GDOP_ratio_thresh = config_dict['GDOP_ratio_thresh']
        if 'residuals_ratio_thresh' in config_dict:
            config.stopping_criteria.residuals_ratio_thresh = config_dict['residuals_ratio_thresh']
        if 'condition_number_ratio_thresh' in config_dict:
            config.stopping_criteria.condition_number_ratio_thresh = config_dict['condition_number_ratio_thresh']
        if 'covariance_ratio_thresh' in config_dict:
            config.stopping_criteria.covariance_ratio_thresh = config_dict['covariance_ratio_thresh']
        if 'convergence_postion_thresh' in config_dict:
            config.stopping_criteria.convergence_postion_thresh = config_dict['convergence_postion_thresh']
        if 'internal_constraint_ratio_thresh' in config_dict:
            config.stopping_criteria.internal_constraint_ratio_thresh = config_dict['internal_constraint_ratio_thresh']
        if 'convergence_counter_threshold' in config_dict:
            config.stopping_criteria.convergence_counter_threshold = config_dict['convergence_counter_threshold']
        
        # Outlier rejection parameters
        if 'z_score_threshold' in config_dict:
            config.outlier.z_score_threshold = config_dict['z_score_threshold']
        if 'outlier_count_threshold' in config_dict:
            config.outlier.outlier_count_threshold = config_dict['outlier_count_threshold']
        
        # Trajectory parameters
        if 'trajectory_optimisation_method' in config_dict:
            config.trajectory.trajectory_optimisation_method = TrajectoryOptimizationMethod.from_string(
                config_dict['trajectory_optimisation_method']
            )
        if 'link_method' in config_dict:
            config.trajectory.link_method = LinkMethod.from_string(config_dict['link_method'])
        
        return config
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the configuration to a flat dictionary.
        
        Returns:
            Dictionary of configuration parameters in a flat structure
        """
        return {
            # Measurement gathering parameters
            'distance_to_anchor_ratio_threshold': self.measurement.distance_to_anchor_ratio_threshold,
            'number_of_redundant_measurements': self.measurement.number_of_redundant_measurements,
            'distance_rejection_threshold': self.measurement.distance_rejection_threshold,
            
            # Least squares parameters
            'use_linear_bias': self.least_squares.use_linear_bias,
            'use_constant_bias': self.least_squares.use_constant_bias,
            'normalised': self.least_squares.normalised,
            'regularise': self.least_squares.regularise,
            'rough_estimate_method': self.least_squares.rough_estimate_method.name.lower(),
            'outlier_removing': self.least_squares.outlier_removing.name.lower(),
            'reweighting_iterations': self.least_squares.reweighting_iterations,
            'use_trimmed_reweighted': self.least_squares.use_trimmed_reweighted,
            'weighting_function': self.least_squares.weighting_function,
            'huber_delta': self.least_squares.huber_delta,
            'tukey_c': self.least_squares.tukey_c,
            'welsch_c': self.least_squares.welsch_c,
            'non_linear_optimisation_type': self.least_squares.non_linear_optimisation_type.name,
            
            # Stopping criteria parameters
            'stopping_criteria': self.stopping_criteria.stopping_criteria,
            'FIM_thresh': self.stopping_criteria.FIM_thresh,
            'GDOP_thresh': self.stopping_criteria.GDOP_thresh,
            'residuals_thresh': self.stopping_criteria.residuals_thresh,
            'condition_number_thresh': self.stopping_criteria.condition_number_thresh,
            'covariance_thresh': self.stopping_criteria.covariance_thresh,
            'internal_constraint_thresh': self.stopping_criteria.internal_constraint_thresh,
            'number_of_measurements_thresh': self.stopping_criteria.number_of_measurements_thresh,
            'FIM_ratio_thresh': self.stopping_criteria.FIM_ratio_thresh,
            'GDOP_ratio_thresh': self.stopping_criteria.GDOP_ratio_thresh,
            'residuals_ratio_thresh': self.stopping_criteria.residuals_ratio_thresh,
            'condition_number_ratio_thresh': self.stopping_criteria.condition_number_ratio_thresh,
            'covariance_ratio_thresh': self.stopping_criteria.covariance_ratio_thresh,
            'convergence_postion_thresh': self.stopping_criteria.convergence_postion_thresh,
            'internal_constraint_ratio_thresh': self.stopping_criteria.internal_constraint_ratio_thresh,
            'convergence_counter_threshold': self.stopping_criteria.convergence_counter_threshold,
            
            # Outlier rejection parameters
            'z_score_threshold': self.outlier.z_score_threshold,
            'outlier_count_threshold': self.outlier.outlier_count_threshold,
            
            # Trajectory parameters
            'trajectory_optimisation_method': self.trajectory.trajectory_optimisation_method.name,
            'link_method': self.trajectory.link_method.name.lower(),
        }