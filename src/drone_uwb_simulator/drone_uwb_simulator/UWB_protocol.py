"""
Ultra-Wideband (UWB) Protocol Implementation

This module provides a comprehensive implementation of UWB anchor networks
for distance measurement and positioning applications. It includes realistic
error modeling with configurable bias and noise characteristics.

Classes:
    BiasModel: Models systematic errors in UWB measurements
    NoiseModel: Models random errors and outliers in UWB measurements
    Anchor: Represents a UWB anchor in 3D space
    UWBNetwork: Manages multiple UWB anchors for coordinated measurements
    MeasurementResult: Represents the result of a UWB measurement

Example:
    # Create a UWB network with anchors
    network = UWBNetwork()
    
    # Add anchors with realistic error models
    anchor1 = Anchor.from_coordinates(
        "A1", 0.0, 0.0, 2.5,
        bias_model=BiasModel(constant_bias=0.05, linear_bias=1.02),
        noise_model=NoiseModel(variance=0.01, outlier_probability=0.02)
    )
    network.add_anchor(anchor1)
    
    # Measure distance to a target position
    measurements = network.measure_distances([1.5, 2.0, 0.0])
"""

from __future__ import annotations

import numpy as np
import warnings
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import (
    Tuple, List, Optional, Dict, Union, Any, 
    Protocol, TypeVar, Generic, Callable, cast,
    Iterable, Sequence, Set, FrozenSet
)


# Type aliases for improved readability
Position3D = Union[np.ndarray, List[float], Tuple[float, float, float]]
AnchorID = str
MeasurementDict = Dict[AnchorID, float]
PositionDict = Dict[AnchorID, np.ndarray]


class MeasurementError(Exception):
    """Base exception for measurement-related errors."""
    pass


class ConfigurationError(Exception):
    """Exception raised for configuration errors."""
    pass


class PositionValidator:
    """Utility class for validating 3D positions."""
    
    @staticmethod
    def validate(position: Position3D) -> np.ndarray:
        """
        Validate and convert a position to a numpy array.
        
        Parameters:
        -----------
        position : Position3D
            3D position to validate.
            
        Returns:
        --------
        np.ndarray
            Validated position as a numpy array.
            
        Raises:
        -------
        ValueError
            If the position is not a valid 3D point.
        """
        pos_array = np.asarray(position, dtype=float)
        
        if pos_array.shape != (3,):
            raise ValueError(f"Position must be a 3D point, got shape {pos_array.shape}")
            
        return pos_array


@dataclass(frozen=True)
class MeasurementResult:
    """
    Represents the result of a distance measurement.
    
    This immutable dataclass encapsulates all relevant information about
    a distance measurement, including the true distance, measured distance,
    and error components.
    
    Attributes:
    -----------
    anchor_id : str
        ID of the anchor that performed the measurement.
    true_distance : float
        Actual distance without any errors applied.
    measured_distance : float
        Distance measured by the anchor (with errors if applicable).
    bias_applied : float
        Bias component applied to the measurement.
    noise_applied : float
        Noise component applied to the measurement.
    is_outlier : bool
        Whether this measurement is an outlier.
    """
    anchor_id: str
    true_distance: float
    measured_distance: float
    bias_applied: float = 0.0
    noise_applied: float = 0.0
    is_outlier: bool = False
    
    @property
    def total_error(self) -> float:
        """Calculate the total error in the measurement."""
        return self.measured_distance - self.true_distance
    
    @property
    def error_percentage(self) -> float:
        """Calculate the error as a percentage of true distance."""
        if self.true_distance == 0:
            return float('inf') if self.total_error > 0 else float('-inf')
        return (self.total_error / self.true_distance) * 100.0


@dataclass
class BiasModel:
    """
    Models systematic errors in UWB distance measurements.
    
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

    def apply(self, distance: float) -> Tuple[float, float]:
        """
        Apply the bias model to a distance measurement.
        
        Parameters:
        -----------
        distance : float
            True distance to be biased.
            
        Returns:
        --------
        Tuple[float, float]
            A tuple containing (biased_distance, bias_amount).
        """
        biased_distance = self.constant_bias + self.linear_bias * distance
        bias_amount = biased_distance - distance
        return biased_distance, bias_amount
    
    def __repr__(self) -> str:
        """Return string representation of the bias model."""
        return f"BiasModel(constant={self.constant_bias:.3f}m, linear={self.linear_bias:.3f})"


@dataclass
class NoiseModel:
    """
    Models random errors in UWB measurements.
    
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
    random_seed : Optional[int]
        Seed for the random number generator for reproducible results.
    """
    variance: float = 0.1
    outlier_probability: float = 0.0
    outlier_range: Tuple[float, float] = (0.2, 0.3)
    random_seed: Optional[int] = field(default=None, repr=False)
    _rng: np.random.Generator = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Validate parameters and initialize random number generator."""
        if self.variance < 0:
            raise ValueError("Variance must be non-negative")
        if not 0 <= self.outlier_probability <= 1:
            raise ValueError("Outlier probability must be between 0 and 1")
        if self.outlier_range[0] > self.outlier_range[1]:
            raise ValueError("Outlier range minimum must be less than maximum")
        
        # Initialize random number generator with optional seed
        if self.random_seed is not None or self.random_seed != 0:
            self._rng = np.random.default_rng(self.random_seed)
        else:
            self._rng = np.random.default_rng()

    def apply(self, distance: float) -> Tuple[float, float, bool]:
        """
        Apply noise model to a distance measurement.
        
        Parameters:
        -----------
        distance : float
            Distance to be corrupted with noise.
            
        Returns:
        --------
        Tuple[float, float, bool]
            A tuple containing (noisy_distance, noise_amount, is_outlier).
        """
        is_outlier = self._rng.random() < self.outlier_probability
        
        if is_outlier:
            # Generate outlier
            factor = self._rng.uniform(*self.outlier_range)
            noise = distance * factor
            return distance + noise, noise, True
        else:
            # Add Gaussian noise
            noise = self._rng.normal(0, np.sqrt(self.variance))
            return distance + noise, noise, False
    
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
        position: Position3D,
        bias_model: Optional[BiasModel] = None,
        noise_model: Optional[NoiseModel] = None
    ) -> None:
        """
        Initialize an UWB anchor.
        
        Parameters:
        -----------
        anchor_id : str
            Unique identifier for the anchor.
        position : Position3D
            3D coordinates of the anchor position [x, y, z].
        bias_model : BiasModel, optional
            Model for systematic measurement biases.
        noise_model : NoiseModel, optional
            Model for random measurement noise and outliers.
        """
        self.anchor_id = str(anchor_id)
        self.position = PositionValidator.validate(position)
        self.bias_model = bias_model or BiasModel()
        self.noise_model = noise_model or NoiseModel()
        self._last_measurement: Optional[MeasurementResult] = None

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
        target_position: Position3D, 
        include_errors: bool = True
    ) -> Union[float, MeasurementResult]:
        """
        Measure the distance to a target position with optional error simulation.
        
        Parameters:
        -----------
        target_position : Position3D
            3D coordinates of the target [x, y, z].
        include_errors : bool
            If True, apply bias and noise models to the measurement.
            
        Returns:
        --------
        Union[float, MeasurementResult]
            Either the measured distance (float) or a detailed MeasurementResult
            object containing true distance, measured distance, and error components.
            The return type depends on the value of return_details parameter.
        """
        target_pos = PositionValidator.validate(target_position)

        # Calculate true distance
        true_distance = np.linalg.norm(self.position - target_pos)
        
        if not include_errors:
            return true_distance
            
        # Apply bias model
        biased_distance, bias_applied = self.bias_model.apply(true_distance)
        
        # Apply noise model
        measured_distance, noise_applied, is_outlier = self.noise_model.apply(biased_distance)
        
        # Create measurement result
        result = MeasurementResult(
            anchor_id=self.anchor_id,
            true_distance=true_distance,
            measured_distance=measured_distance,
            bias_applied=bias_applied,
            noise_applied=noise_applied,
            is_outlier=is_outlier
        )
        
        # Store last measurement
        self._last_measurement = result
        
        return result
    
    def get_last_measurement(self) -> Optional[MeasurementResult]:
        """
        Get the most recent measurement result.
        
        Returns:
        --------
        Optional[MeasurementResult]
            The most recent measurement result or None if no measurement has been made.
        """
        return self._last_measurement
    
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
    Manages a network of UWB anchors for multi-anchor measurements.
    
    This class manages multiple UWB anchors and provides methods for
    conducting measurements from all anchors to a target position.

    Attributes:
    -----------
    anchors : List[Anchor]
        List of UWB anchors in the network.
    """
    
    def __init__(self, anchors: Optional[List[Anchor]] = None) -> None:
        """
        Initialize the UWB network.
        
        Parameters:
        -----------
        anchors : List[Anchor], optional
            List of UWB anchors to include in the network. Default is an empty list.
        """
        self.anchors: List[Anchor] = []
        self._anchor_dict: Dict[AnchorID, Anchor] = {}
        
        # Add any provided anchors
        if anchors:
            for anchor in anchors:
                self.add_anchor(anchor)

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
    
    def add_anchors(self, anchors: List[Anchor]) -> None:
        """
        Add multiple anchors to the network.
        
        Parameters:
        -----------
        anchors : List[Anchor]
            List of UWB anchors to add to the network.
            
        Raises:
        -------
        ValueError
            If an anchor with a duplicate ID exists.
        """
        for anchor in anchors:
            self.add_anchor(anchor)
    
    def remove_anchor(self, anchor_id: AnchorID) -> bool:
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

    def get_anchor(self, anchor_id: AnchorID) -> Optional[Anchor]:
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
        target_position: Position3D,
        include_errors: bool = True,
        anchor_ids: Optional[List[AnchorID]] = None,
        return_details: bool = False
    ) -> Union[MeasurementDict, Dict[AnchorID, MeasurementResult]]:
        """
        Measure distances from selected anchors to a target position.
        
        Parameters:
        -----------
        target_position : Position3D
            3D coordinates of the target [x, y, z].
        include_errors : bool
            If True, apply bias and noise models to the measurements.
        anchor_ids : List[str], optional
            List of anchor IDs to include in the measurement. If None,
            measurements from all anchors are returned.
        return_details : bool
            If True, return detailed measurement results instead of just distances.
            
        Returns:
        --------
        Union[Dict[str, float], Dict[str, MeasurementResult]]
            Dictionary mapping anchor IDs to either measured distances (float) or
            measurement result objects, depending on the return_details parameter.
        """
        if not self.anchors:
            return {}
            
        target_pos = PositionValidator.validate(target_position)
        
        # Get anchors to use for measurement
        if anchor_ids is not None:
            # Filter anchors by ID
            selected_anchors = [
                self._anchor_dict[aid] for aid in anchor_ids 
                if aid in self._anchor_dict
            ]
        else:
            selected_anchors = self.anchors
        
        # Perform measurements
        if return_details:
            # Return detailed measurement results
            return {
                anchor.anchor_id: cast(MeasurementResult, anchor.measure_distance(
                    target_pos, include_errors
                ))
                for anchor in selected_anchors
            }
        else:
            # Return just the distances
            results = {}
            for anchor in selected_anchors:
                result = anchor.measure_distance(target_pos, include_errors)
                if isinstance(result, MeasurementResult):
                    results[anchor.anchor_id] = result.measured_distance
                else:
                    results[anchor.anchor_id] = result
            return results
    
    def get_anchor_positions(self, anchor_ids: Optional[List[AnchorID]] = None) -> PositionDict:
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
            selected_anchors = [
                self._anchor_dict[aid] for aid in anchor_ids 
                if aid in self._anchor_dict
            ]
        else:
            selected_anchors = self.anchors
            
        return {
            anchor.anchor_id: anchor.position
            for anchor in selected_anchors
        }
    
    def update_anchor_position(self, anchor_id: AnchorID, position: Position3D) -> bool:
        """
        Update the position of an anchor.
        
        Parameters:
        -----------
        anchor_id : str
            ID of the anchor to update.
        position : Position3D
            New 3D position for the anchor.
            
        Returns:
        --------
        bool
            True if the anchor was updated, False if no anchor with the specified ID was found.
        """
        anchor = self.get_anchor(anchor_id)
        if not anchor:
            return False
            
        anchor.position = PositionValidator.validate(position)
        return True
    
    def reset_measurements(self) -> None:
        """Reset all stored measurements in the network's anchors."""
        for anchor in self.anchors:
            anchor._last_measurement = None
    
    def get_measurement_errors(self) -> Dict[AnchorID, float]:
        """
        Get errors for the most recent measurements.
        
        Returns:
        --------
        Dict[str, float]
            Dictionary mapping anchor IDs to measurement errors.
        """
        errors = {}
        for anchor in self.anchors:
            last_measurement = anchor.get_last_measurement()
            if last_measurement is not None:
                errors[anchor.anchor_id] = last_measurement.total_error
        return errors
    
    def __len__(self) -> int:
        """Return the number of anchors in the network."""
        return len(self.anchors)
    
    def __repr__(self) -> str:
        """Return string representation of the UWB network."""
        return f"UWBNetwork(num_anchors={len(self.anchors)})"