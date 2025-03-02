import numpy as np
from dataclasses import dataclass, field
from typing import Tuple, List, Optional, Dict, Union, Any


@dataclass
class BiasModel:
    """
    Represents the bias model for UWB distance measurements.
    
    This model simulates systematic errors in UWB measurements using
    a combination of constant and linear bias components.
    
    Attributes:
    -----------
    constant_bias : float
        Fixed offset added to all measurements (in meters).
    linear_bias : float
        Multiplicative factor applied to the true distance.
    """
    constant_bias: float = 0.0
    linear_bias: float = 1.0

    def apply(self, distance: float) -> float:
        """
        Apply the bias model to a distance measurement.
        
        Parameters:
        -----------
        distance : float
            True distance to be biased.
            
        Returns:
        --------
        float
            Biased distance measurement.
        """
        return self.constant_bias + self.linear_bias * distance
    
    def __repr__(self) -> str:
        """Return string representation of the bias model."""
        return f"BiasModel(constant={self.constant_bias:.3f}m, linear={self.linear_bias:.3f})"


@dataclass
class NoiseModel:
    """
    Represents the noise model for UWB measurements.
    
    This model adds random measurement errors through Gaussian noise
    and occasional outliers based on specified probabilities.

    Attributes:
    -----------
    variance : float
        Variance of the Gaussian noise (in meters squared).
    outlier_probability : float
        Probability of generating an outlier [0,1].
    outlier_range : Tuple[float, float]
        Range for outlier multiplication factor (min, max).
    """
    variance: float = 0.1
    outlier_probability: float = 0.0
    outlier_range: Tuple[float, float] = (0.2, 0.3)
    random_seed: Optional[int] = field(default=None, repr=False)
    _rng: np.random.Generator = field(init=False, repr=False)

    def __post_init__(self):
        """Validate parameters and initialize random number generator."""
        if self.variance < 0:
            raise ValueError("Variance must be non-negative")
        if not 0 <= self.outlier_probability <= 1:
            raise ValueError("Outlier probability must be between 0 and 1")
        if self.outlier_range[0] > self.outlier_range[1]:
            raise ValueError("Outlier range minimum must be less than maximum")
        
        # Initialize random number generator with optional seed
        self._rng = np.random.default_rng(self.random_seed)

    def apply(self, distance: float) -> float:
        """
        Apply noise model to a distance measurement.
        
        Parameters:
        -----------
        distance : float
            Distance to be corrupted with noise.
            
        Returns:
        --------
        float
            Noisy distance measurement.
        """
        if self._rng.random() < self.outlier_probability:
            # Generate outlier
            factor = self._rng.uniform(*self.outlier_range)
            return distance * (1 + factor)
        else:
            # Add Gaussian noise
            return distance + self._rng.normal(0, np.sqrt(self.variance))
    
    def __repr__(self) -> str:
        """Return string representation of the noise model."""
        return (f"NoiseModel(variance={self.variance:.4f}, "
                f"outlier_prob={self.outlier_probability:.2f}, "
                f"outlier_range={self.outlier_range})")


class Anchor:
    """
    Represents a UWB anchor in 3D space with realistic measurement simulation.
    
    This class simulates an Ultra-Wideband anchor that can measure distances
    to targets, including realistic error sources such as biases, noise,
    and outliers.

    Attributes:
    -----------
    anchor_id : str
        Unique identifier for the anchor.
    position : np.ndarray
        3D coordinates of the anchor [x, y, z].
    bias_model : BiasModel
        Model for systematic measurement biases.
    noise_model : NoiseModel
        Model for random measurement noise and outliers.
    """
    
    def __init__(
        self, 
        anchor_id: str,
        position: Union[np.ndarray, List[float], Tuple[float, float, float]],
        bias_model: Optional[BiasModel] = None,
        noise_model: Optional[NoiseModel] = None
    ):
        """
        Initialize an UWB anchor.
        
        Parameters:
        -----------
        anchor_id : str
            Unique identifier for the anchor.
        position : array-like
            3D coordinates of the anchor position [x, y, z].
        bias_model : BiasModel, optional
            Model for systematic measurement biases.
        noise_model : NoiseModel, optional
            Model for random measurement noise and outliers.
        """
        self.anchor_id = str(anchor_id)
        self.position = np.asarray(position, dtype=float)
        
        if self.position.shape != (3,):
            raise ValueError("Position must be a 3D point")
            
        self.bias_model = bias_model or BiasModel()
        self.noise_model = noise_model or NoiseModel()

    @classmethod
    def from_coordinates(
        cls,
        anchor_id: str,
        x: float, 
        y: float, 
        z: float,
        bias_model: Optional[BiasModel] = None,
        noise_model: Optional[NoiseModel] = None
    ) -> 'Anchor':
        """
        Create an anchor using explicit x, y, z coordinates.
        
        Parameters:
        -----------
        anchor_id : str
            Unique identifier for the anchor.
        x, y, z : float
            3D coordinates of the anchor position.
        bias_model : BiasModel, optional
            Model for systematic measurement biases.
        noise_model : NoiseModel, optional
            Model for random measurement noise and outliers.
            
        Returns:
        --------
        Anchor
            Initialized anchor instance.
        """
        return cls(
            anchor_id=anchor_id,
            position=[float(x), float(y), float(z)],
            bias_model=bias_model,
            noise_model=noise_model
        )

    def measure_distance(
        self, 
        target_position: Union[np.ndarray, List[float], Tuple[float, float, float]], 
        include_errors: bool = True
    ) -> float:
        """
        Measure the distance to a target position with optional error simulation.
        
        Parameters:
        -----------
        target_position : array-like
            3D coordinates of the target [x, y, z].
        include_errors : bool
            If True, apply bias and noise models to the measurement.
            
        Returns:
        --------
        float
            Measured distance (with or without simulated errors).
        """
        target_pos = np.asarray(target_position, dtype=float)
            
        if target_pos.shape != (3,):
            raise ValueError("Target position must be a 3D point")

        # Calculate true distance
        true_distance = np.linalg.norm(self.position - target_pos)
        
        if not include_errors:
            return true_distance
            
        # Apply bias model
        biased_distance = self.bias_model.apply(true_distance)
        
        # Apply noise model
        measured_distance = self.noise_model.apply(biased_distance)
        
        return measured_distance
    
    def update_bias_model(
        self,
        constant_bias: Optional[float] = None,
        linear_bias: Optional[float] = None
    ) -> None:
        """
        Update the bias model parameters.
        
        Parameters:
        -----------
        constant_bias : float, optional
            New constant bias offset. If None, current value is retained.
        linear_bias : float, optional
            New linear bias factor. If None, current value is retained.
        """
        # Keep existing values if new ones aren't provided
        new_constant_bias = (constant_bias if constant_bias is not None 
                            else self.bias_model.constant_bias)
        new_linear_bias = (linear_bias if linear_bias is not None 
                          else self.bias_model.linear_bias)
        
        self.bias_model = BiasModel(
            constant_bias=new_constant_bias,
            linear_bias=new_linear_bias
        )

    def update_noise_model(
        self, 
        variance: Optional[float] = None,
        outlier_probability: Optional[float] = None,
        outlier_range: Optional[Tuple[float, float]] = None,
        random_seed: Optional[int] = None
    ) -> None:
        """
        Update the noise model parameters.
        
        Parameters:
        -----------
        variance : float, optional
            New variance for Gaussian noise. If None, current value is retained.
        outlier_probability : float, optional
            New probability of generating outliers [0,1]. If None, current value is retained.
        outlier_range : Tuple[float, float], optional
            New range for outlier multiplication factor (min, max). If None, current value is retained.
        random_seed : int, optional
            New random seed for noise generation. If None, current seed (or no seed) is retained.
        """
        # Keep existing values if new ones aren't provided
        new_variance = (variance if variance is not None 
                       else self.noise_model.variance)
        new_outlier_prob = (outlier_probability if outlier_probability is not None 
                           else self.noise_model.outlier_probability)
        new_outlier_range = (outlier_range if outlier_range is not None 
                            else self.noise_model.outlier_range)
        new_random_seed = (random_seed if random_seed is not None 
                          else self.noise_model.random_seed)
        
        self.noise_model = NoiseModel(
            variance=new_variance,
            outlier_probability=new_outlier_prob,
            outlier_range=new_outlier_range,
            random_seed=new_random_seed
        )
        
    @property
    def ground_truth(self) -> Dict[str, Any]:
        """
        Get the ground truth parameters of the anchor.
        
        Returns:
        --------
        Dict[str, Any]
            Dictionary containing the anchor's ground truth parameters:
            - 'position': Anchor's 3D position
            - 'bias_model': BiasModel object
            - 'noise_model': NoiseModel object
        """
        return {
            'position': self.position,
            'bias_model': self.bias_model,
            'noise_model': self.noise_model
        }
    
    def __repr__(self) -> str:
        """Return string representation of the anchor."""
        return (f"Anchor(id='{self.anchor_id}', "
                f"position=[{self.position[0]:.2f}, {self.position[1]:.2f}, {self.position[2]:.2f}])")


class UWBNetwork:
    """
    Represents a network of UWB anchors for multi-anchor measurements.
    
    This class manages multiple UWB anchors and provides methods for
    conducting measurements from all anchors to a target position.

    Attributes:
    -----------
    anchors : List[Anchor]
        List of UWB anchors in the network.
    """
    
    def __init__(self, anchors: List[Anchor] = None):
        """
        Initialize the UWB network.
        
        Parameters:
        -----------
        anchors : List[Anchor], optional
            List of UWB anchors to include in the network. Default is an empty list.
        """
        self.anchors = anchors or []
        self._anchor_dict = {anchor.anchor_id: anchor for anchor in self.anchors}

    def add_anchor(self, anchor: Anchor) -> None:
        """
        Add an anchor to the network.
        
        Parameters:
        -----------
        anchor : Anchor
            UWB anchor to add to the network.
            
        Raises:
        -------
        ValueError
            If an anchor with the same ID already exists in the network.
        """
        if anchor.anchor_id in self._anchor_dict:
            raise ValueError(f"Anchor with ID '{anchor.anchor_id}' already exists in the network")
            
        self.anchors.append(anchor)
        self._anchor_dict[anchor.anchor_id] = anchor
    
    def remove_anchor(self, anchor_id: str) -> bool:
        """
        Remove an anchor from the network by ID.
        
        Parameters:
        -----------
        anchor_id : str
            ID of the anchor to remove.
            
        Returns:
        --------
        bool
            True if the anchor was removed, False if no anchor with the specified ID was found.
        """
        if anchor_id not in self._anchor_dict:
            return False
            
        anchor = self._anchor_dict.pop(anchor_id)
        self.anchors.remove(anchor)
        return True

    def get_anchor(self, anchor_id: str) -> Optional[Anchor]:
        """
        Get an anchor by ID.
        
        Parameters:
        -----------
        anchor_id : str
            ID of the anchor to retrieve.
            
        Returns:
        --------
        Optional[Anchor]
            The anchor with the specified ID, or None if no such anchor exists.
        """
        return self._anchor_dict.get(anchor_id)

    def measure_distances(
        self, 
        target_position: Union[np.ndarray, List[float], Tuple[float, float, float]],
        include_errors: bool = True,
        anchor_ids: Optional[List[str]] = None
    ) -> Dict[str, float]:
        """
        Measure distances from selected anchors to a target position.
        
        Parameters:
        -----------
        target_position : array-like
            3D coordinates of the target [x, y, z].
        include_errors : bool
            If True, apply bias and noise models to the measurements.
        anchor_ids : List[str], optional
            List of anchor IDs to include in the measurement. If None,
            measurements from all anchors are returned.
            
        Returns:
        --------
        Dict[str, float]
            Dictionary mapping anchor IDs to measured distances.
        """
        if not self.anchors:
            return {}
            
        target_pos = np.asarray(target_position, dtype=float)
        
        if anchor_ids is not None:
            # Filter anchors by ID
            selected_anchors = [self._anchor_dict[aid] for aid in anchor_ids 
                               if aid in self._anchor_dict]
        else:
            selected_anchors = self.anchors
            
        return {
            anchor.anchor_id: anchor.measure_distance(target_pos, include_errors)
            for anchor in selected_anchors
        }
    
    def get_anchor_positions(self, anchor_ids: Optional[List[str]] = None) -> Dict[str, np.ndarray]:
        """
        Get the positions of selected anchors.
        
        Parameters:
        -----------
        anchor_ids : List[str], optional
            List of anchor IDs to include. If None, positions of all anchors are returned.
            
        Returns:
        --------
        Dict[str, np.ndarray]
            Dictionary mapping anchor IDs to 3D positions.
        """
        if anchor_ids is not None:
            # Filter anchors by ID
            selected_anchors = [self._anchor_dict[aid] for aid in anchor_ids 
                               if aid in self._anchor_dict]
        else:
            selected_anchors = self.anchors
            
        return {
            anchor.anchor_id: anchor.position
            for anchor in selected_anchors
        }
    
    def __len__(self) -> int:
        """Return the number of anchors in the network."""
        return len(self.anchors)
    
    def __repr__(self) -> str:
        """Return string representation of the UWB network."""
        return f"UWBNetwork(num_anchors={len(self.anchors)})"