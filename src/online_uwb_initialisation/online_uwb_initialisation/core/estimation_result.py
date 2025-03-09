from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Union, Any
import numpy as np


@dataclass
class EstimationResult:
    """Container for estimation results.
    
    This class encapsulates the results of an anchor position estimation, 
    including the estimated position, bias terms, covariance matrix, and
    performance metrics.
    """
    # Core estimation results
    estimator: np.ndarray
    """The estimated parameters: [x, y, z, constant_bias, linear_bias]"""
    
    covariance_matrix: np.ndarray
    """Covariance matrix for the estimated parameters"""
    
    residuals: np.ndarray
    """Residuals of the estimation"""
    
    raw_params: Optional[np.ndarray] = None
    """Raw parameters from the estimation method (if applicable)"""
    
    # Additional metrics
    condition_number: float = float('inf')
    """Condition number of the estimation matrix"""
    
    fim: Optional[np.ndarray] = None
    """Fisher Information Matrix"""
    
    gdop: float = float('inf')
    """Geometric Dilution of Precision"""
    
    verification_value: float = float('inf')
    """Internal verification metric for consistency"""
    
    outliers: List[int] = field(default_factory=list)
    """Indices of detected outliers"""
    
    iteration_count: int = 0
    """Number of iterations performed (for iterative methods)"""
    
    converged: bool = False
    """Whether the estimation converged (for iterative methods)"""
    
    is_nonlinear: bool = False
    """Whether this result is from a nonlinear estimation method"""
    
    @property
    def position(self) -> np.ndarray:
        """Get the estimated position [x, y, z]."""
        return self.estimator[:3]
    
    @property
    def constant_bias(self) -> float:
        """Get the estimated constant bias term."""
        return float(self.estimator[3])
    
    @property
    def linear_bias(self) -> float:
        """Get the estimated linear bias term."""
        return float(self.estimator[4])
    
    @property
    def mean_residual(self) -> float:
        """Get the mean of the absolute residuals."""
        return float(np.mean(np.abs(self.residuals)))
    
    @property
    def median_residual(self) -> float:
        """Get the median of the absolute residuals."""
        return float(np.median(np.abs(self.residuals)))
    
    @property
    def position_covariance(self) -> np.ndarray:
        """Get the position covariance submatrix."""
        if self.covariance_matrix.size > 0:
            return self.covariance_matrix[:3, :3]
        return np.array([])
    
    @property
    def position_uncertainty(self) -> np.ndarray:
        """Get the position uncertainty (standard deviations)."""
        if self.covariance_matrix.size > 0:
            return np.sqrt(np.diag(self.covariance_matrix)[:3])
        return np.array([])
    
    def distance_from(self, other_position: np.ndarray) -> float:
        """Calculate distance from the estimated position to another position.
        
        Args:
            other_position: Another position to compare with [x, y, z]
            
        Returns:
            Euclidean distance between the positions
        """
        return float(np.linalg.norm(self.position - np.array(other_position)))
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the estimation result to a dictionary.
        
        Returns:
            Dictionary representation of the estimation result
        """
        return {
            "estimator": self.estimator,
            "covariance_matrix": self.covariance_matrix,
            "residuals": self.residuals,
            "raw_params": self.raw_params,
            "condition_number": self.condition_number,
            "fim": self.fim,
            "gdop": self.gdop,
            "verification_value": self.verification_value,
            "outliers": self.outliers,
            "iteration_count": self.iteration_count,
            "converged": self.converged,
            "is_nonlinear": self.is_nonlinear
        }