"""
Drone Simulation Environment

This module provides a comprehensive simulation environment for testing
UWB-based localization with drones. It supports various waypoint generation
modes, anchor placement strategies, and realistic trajectory simulation.

Classes:
    SimulationConfig: Configuration parameters for the simulation
    WaypointMode: Enumeration of waypoint generation modes
    AnchorPlacementStrategy: Enumeration of anchor placement strategies
    SimulationResult: Container for simulation results
    DroneSimulation: Main simulation environment controller

Example:
    # Create a simulation with custom configuration
    config = SimulationConfig(
        dt=0.05,
        drone_speed=1.5,
        wait_time=2.0,
        num_waypoints=10,
        bounds=(10.0, 10.0, 3.0)
    )
    
    # Initialize and run the simulation
    simulation = DroneSimulation(config)
    simulation.initialize_environment(WaypointMode.RANDOM)
    
    # Run the simulation for 100 steps
    for _ in range(100):
        position = simulation.update_drone_position()
        measurements = simulation.measure_distances()
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Union, Any, ClassVar
from enum import Enum, auto
from pathlib import Path
import json
import time

# Import from the improved modules
from drone_uwb_simulator.UWB_protocol import (
    Anchor, BiasModel, NoiseModel, UWBNetwork, 
    MeasurementResult, Position3D, AnchorID
)
from drone_uwb_simulator.drone_dynamics import (
    Waypoint, Trajectory, Point3D, TrajectoryStats,
    InterpolationMethod
)


@dataclass
class SimulationConfig:
    """
    Configuration parameters for the drone simulation environment.
    
    Attributes:
    -----------
    dt : float
        Time step for simulation in seconds.
    drone_speed : float
        Speed of the drone in meters per second.
    wait_time : float
        Time to wait for the drone to reach the waypoint in seconds.
    num_waypoints : int
        Number of waypoints to generate for random trajectories.
    bounds : Tuple[float, float, float]
        Environment boundaries as (x_bound, y_bound, z_bound) in meters.
    min_height : float
        Minimum height for waypoints in meters.
    max_height : float
        Maximum height for waypoints in meters.
    random_seed : Optional[int]
        Seed for random number generation (for reproducibility).
    bias_model_params : Dict[str, float]
        Parameters for UWB anchor bias models.
    noise_model_params : Dict[str, Any]
        Parameters for UWB anchor noise models.
    """
    dt: float = 0.05
    drone_speed: float = 1.0
    num_waypoints: int = 15
    num_base_anchors: int = 3
    num_unknown_anchors: int = 3
    bounds: Tuple[float, float, float] = (5.0, 5.0, 5.0)
    wait_time: float = 0.0
    min_height: float = 0.0
    max_height: float = field(default=None, init=False)
    random_seed: Optional[int] = None
    bias_model_params: Dict[str, float] = field(default_factory=lambda: {"constant_bias": 0.0951, "linear_bias": 1.0049})
    noise_model_params: Dict[str, Any] = field(default_factory=lambda: {
        "variance": 0.2, 
        "outlier_probability": 0.05, 
        "outlier_range": (0.2, 0.3)
    })
    
    def __post_init__(self) -> None:
        """Initialize derived attributes and validate configuration."""
        # Set max_height if not explicitly set
        if self.max_height is None:
            self.max_height = self.bounds[2]
            
        # Validate configuration
        if self.dt <= 0:
            raise ValueError("Time step (dt) must be positive")
        if self.drone_speed <= 0:
            raise ValueError("Drone speed must be positive")
        if self.wait_time < 0:
            raise ValueError("Wait time must be non-negative")
        if self.num_waypoints < 2:
            raise ValueError("Number of waypoints must be at least 2")
        if any(bound <= 0 for bound in self.bounds):
            raise ValueError("Environment bounds must be positive")
        if self.min_height < 0:
            raise ValueError("Minimum height cannot be negative")
        if self.max_height <= self.min_height:
            raise ValueError("Maximum height must be greater than minimum height")
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'SimulationConfig':
        """
        Create a SimulationConfig from a dictionary.
        
        Parameters:
        -----------
        config_dict : Dict[str, Any]
            Dictionary containing configuration parameters.
            
        Returns:
        --------
        SimulationConfig
            Configuration object.
        """
        # Filter out any keys that aren't valid parameters
        valid_keys = cls.__dataclass_fields__.keys()
        filtered_dict = {k: v for k, v in config_dict.items() if k in valid_keys}
        
        return cls(**filtered_dict)
    
    @classmethod
    def from_json(cls, json_path: Union[str, Path]) -> 'SimulationConfig':
        """
        Load configuration from a JSON file.
        
        Parameters:
        -----------
        json_path : Union[str, Path]
            Path to the JSON configuration file.
            
        Returns:
        --------
        SimulationConfig
            Configuration object.
        """
        with open(json_path, 'r') as f:
            config_dict = json.load(f)
        
        return cls.from_dict(config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert configuration to a dictionary.
        
        Returns:
        --------
        Dict[str, Any]
            Dictionary representation of the configuration.
        """
        return {
            "dt": self.dt,
            "drone_speed": self.drone_speed,
            "wait_time": self.wait_time,
            "num_waypoints": self.num_waypoints,
            "bounds": self.bounds,
            "min_height": self.min_height,
            "max_height": self.max_height,
            "random_seed": self.random_seed,
            "bias_model_params": self.bias_model_params,
            "noise_model_params": self.noise_model_params
        }
    
    def to_json(self, json_path: Union[str, Path]) -> None:
        """
        Save configuration to a JSON file.
        
        Parameters:
        -----------
        json_path : Union[str, Path]
            Path to save the JSON configuration file.
        """
        with open(json_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)


class WaypointMode(Enum):
    """
    Enumeration of available waypoint generation modes.
    
    Modes:
    ------
    MANUAL: Use manually specified waypoints.
    RANDOM: Generate random waypoints within the environment bounds.
    OPPOSITE_EDGES: Generate waypoints that cross from one edge to the opposite.
    GRID: Generate waypoints in a grid pattern.
    SPIRAL: Generate waypoints in a spiral pattern.
    """
    MANUAL = auto()
    RANDOM = auto()
    OPPOSITE_EDGES = auto()
    GRID = auto()
    SPIRAL = auto()


class AnchorPlacementStrategy(Enum):
    """
    Enumeration of anchor placement strategies.
    
    Strategies:
    -----------
    FIXED: Use fixed, predetermined anchor positions.
    RANDOM: Place anchors randomly within environment bounds.
    CORNERS: Place anchors in the corners of the environment.
    OPTIMIZED: Place anchors using an optimization algorithm.
    """
    FIXED = auto()
    RANDOM = auto()
    CORNERS = auto()
    OPTIMIZED = auto()


@dataclass
class SimulationResult:
    """
    Container for simulation results.
    
    Attributes:
    -----------
    drone_positions : List[np.ndarray]
        List of drone positions over time.
    anchor_measurements : List[Dict[str, float]]
        List of anchor distance measurements over time.
    timestamps : List[float]
        List of simulation timestamps.
    """
    drone_positions: List[np.ndarray] = field(default_factory=list)
    anchor_measurements: List[Dict[AnchorID, float]] = field(default_factory=list)
    timestamps: List[float] = field(default_factory=list)
    
    def add_step(
        self, 
        position: np.ndarray, 
        measurements: Dict[AnchorID, float], 
        timestamp: float
    ) -> None:
        """
        Add a simulation step to the results.
        
        Parameters:
        -----------
        position : np.ndarray
            Drone position at this step.
        measurements : Dict[str, float]
            Anchor distance measurements at this step.
        timestamp : float
            Timestamp for this step.
        """
        self.drone_positions.append(position.copy())
        self.anchor_measurements.append(measurements.copy())
        self.timestamps.append(timestamp)
    
    def clear(self) -> None:
        """Clear all simulation results."""
        self.drone_positions.clear()
        self.anchor_measurements.clear()
        self.timestamps.clear()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert simulation results to a dictionary.
        
        Returns:
        --------
        Dict[str, Any]
            Dictionary representation of the simulation results.
        """
        return {
            "drone_positions": [pos.tolist() for pos in self.drone_positions],
            "anchor_measurements": self.anchor_measurements,
            "timestamps": self.timestamps
        }
    
    def to_json(self, json_path: Union[str, Path]) -> None:
        """
        Save simulation results to a JSON file.
        
        Parameters:
        -----------
        json_path : Union[str, Path]
            Path to save the JSON results file.
        """
        with open(json_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
    
    @classmethod
    def from_json(cls, json_path: Union[str, Path]) -> 'SimulationResult':
        """
        Load simulation results from a JSON file.
        
        Parameters:
        -----------
        json_path : Union[str, Path]
            Path to the JSON results file.
            
        Returns:
        --------
        SimulationResult
            Simulation results object.
        """
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        result = cls()
        result.drone_positions = [np.array(pos) for pos in data.get("drone_positions", [])]
        result.anchor_measurements = data.get("anchor_measurements", [])
        result.timestamps = data.get("timestamps", [])
        
        return result


class DroneSimulation:
    """
    Simulates a drone moving through an environment with UWB anchors.
    
    This class manages the complete simulation environment including:
    - Waypoint generation and trajectory planning
    - Base and unknown UWB anchor placement
    - Drone movement and position updates
    - Distance measurements from UWB anchors
    
    Attributes:
    -----------
    config : SimulationConfig
        Configuration parameters for the simulation.
    waypoints : List[Waypoint]
        List of waypoints defining the drone's path.
    base_anchors : List[Anchor]
        List of known UWB anchors.
    unknown_anchors : List[Anchor]
        List of UWB anchors with unknown positions.
    uwb_network : UWBNetwork
        Network of all UWB anchors.
    drone_trajectory : Trajectory
        Trajectory through the waypoints.
    drone_progress : int
        Current progress along the trajectory (index).
    drone_position : np.ndarray
        Current drone position.
    results : SimulationResult
        Container for simulation results.
    """
    
    # Default anchor positions
    DEFAULT_BASE_ANCHORS: ClassVar[List[Tuple[str, List[float]]]] = [
        ("0", [-1, -1, 0]),
        ("1", [1, 0, 0]),
        ("2", [0, 3, 0]),
        ("3", [0, 6, 0])
    ]
    
    def __init__(self, config: Optional[SimulationConfig] = None):
        """
        Initialize the drone simulation environment.
        
        Parameters:
        -----------
        config : SimulationConfig, optional
            Configuration parameters for the simulation.
            If None, default configuration is used.
        """
        self.config = config or SimulationConfig()
        
        # Initialize random number generator
        if self.config.random_seed is not None:
            np.random.seed(self.config.random_seed)
        
        # Initialize simulation components
        self.waypoints: List[Waypoint] = []
        self.base_anchors: List[Anchor] = []
        self.unknown_anchors: List[Anchor] = []
        self.uwb_network: Optional[UWBNetwork] = None
        self.drone_trajectory: Optional[Trajectory] = None
        
        # Initialize drone state
        self.drone_progress: int = 0
        self.drone_position: np.ndarray = np.zeros(3)
        
        # Initialize results container
        self.results = SimulationResult()
        
        # Set up the environment
        self.initialize_environment()
    
    def generate_waypoints(
        self, 
        mode: WaypointMode = WaypointMode.OPPOSITE_EDGES
    ) -> List[Waypoint]:
        """
        Generate waypoints according to the specified mode.
        
        Parameters:
        -----------
        mode : WaypointMode
            Method to use for generating waypoints.
            
        Returns:
        --------
        List[Waypoint]
            Generated list of waypoints.
        """
        waypoint_generators = {
            WaypointMode.RANDOM: self._generate_random_waypoints,
            WaypointMode.OPPOSITE_EDGES: self._generate_opposite_edges_waypoints,
            WaypointMode.MANUAL: self._generate_manual_waypoints,
            WaypointMode.GRID: self._generate_grid_waypoints,
            WaypointMode.SPIRAL: self._generate_spiral_waypoints
        }
        
        if mode not in waypoint_generators:
            raise ValueError(f"Unsupported waypoint mode: {mode}")
        
        return waypoint_generators[mode]()
    
    def _generate_random_waypoints(self) -> List[Waypoint]:
        """
        Generate random waypoints within environment bounds.
        
        Returns:
        --------
        List[Waypoint]
            List of randomly generated waypoints.
        """
        bounds_x, bounds_y, _ = self.config.bounds
        
        # Start at origin
        waypoints = [Waypoint(0, 0, self.config.min_height)]
        
        # Generate remaining random waypoints
        random_points = np.random.uniform(
            low=[-bounds_x, -bounds_y, self.config.min_height],
            high=[bounds_x, bounds_y, self.config.max_height],
            size=(self.config.num_waypoints - 1, 3)
        )
        
        for x, y, z in random_points:
            waypoints.append(Waypoint(float(x), float(y), float(z)))
            
        return waypoints
    
    def _generate_opposite_edges_waypoints(self) -> List[Waypoint]:
        """
        Generate waypoints on opposite edges of the environment.
        
        Returns:
        --------
        List[Waypoint]
            List of waypoints starting at one edge and ending at the opposite.
        """
        bounds_x, bounds_y, _ = self.config.bounds
        
        # Generate first point on edge
        x1 = np.random.choice([-bounds_x, bounds_x])
        y1 = np.random.uniform(-bounds_y, bounds_y)
        z1 = np.random.uniform(self.config.min_height, self.config.max_height)
        
        # Generate opposite point
        x2 = -x1
        y2 = np.random.choice([-bounds_y, bounds_y]) if abs(x1) == bounds_x else np.random.uniform(-bounds_y, bounds_y)
        z2 = np.random.uniform(self.config.min_height, self.config.max_height)
        
        # Generate intermediate points
        num_middle_points = max(1, self.config.num_waypoints - 2)
        middle_points = np.random.uniform(
            low=[-bounds_x/2, -bounds_y/2, self.config.min_height],
            high=[bounds_x/2, bounds_y/2, self.config.max_height],
            size=(num_middle_points, 3)
        )
        
        return [
            Waypoint(float(x1), float(y1), float(z1)),
            *[Waypoint(float(x), float(y), float(z)) for x, y, z in middle_points],
            Waypoint(float(x2), float(y2), float(z2))
        ]
    
    def _generate_manual_waypoints(self) -> List[Waypoint]:
        """
        Generate a predefined set of waypoints.
        
        Returns:
        --------
        List[Waypoint]
            List of manually defined waypoints.
        """
        return [
            Waypoint(0, 0, 0),
            Waypoint(1, 1, 1),
            Waypoint(2, 2, 2),
            Waypoint(3, 1, 3),
            Waypoint(4, 0, 2),
            Waypoint(6, 6, 3),
            Waypoint(2, 5, 3),
            Waypoint(1, 3, 2),
            Waypoint(0, 2, 1),
            Waypoint(-1, 1, 0),
            Waypoint(-2, 0, 0)
        ]
    
    def _generate_grid_waypoints(self) -> List[Waypoint]:
        """
        Generate waypoints in a grid pattern.
        
        Returns:
        --------
        List[Waypoint]
            List of waypoints arranged in a grid pattern.
        """
        bounds_x, bounds_y, _ = self.config.bounds
        
        # Calculate grid dimensions
        grid_size = int(np.sqrt(self.config.num_waypoints))
        x_vals = np.linspace(-bounds_x, bounds_x, grid_size)
        y_vals = np.linspace(-bounds_y, bounds_y, grid_size)
        z_val = (self.config.min_height + self.config.max_height) / 2
        
        waypoints = []
        for i, x in enumerate(x_vals):
            # Alternate direction for each row (serpentine pattern)
            y_row = y_vals if i % 2 == 0 else reversed(y_vals)
            for y in y_row:
                waypoints.append(Waypoint(float(x), float(y), float(z_val)))
                if len(waypoints) >= self.config.num_waypoints:
                    return waypoints
        
        return waypoints
    
    def _generate_spiral_waypoints(self) -> List[Waypoint]:
        """
        Generate waypoints in a spiral pattern.
        
        Returns:
        --------
        List[Waypoint]
            List of waypoints arranged in a spiral pattern.
        """
        bounds_x, bounds_y, _ = self.config.bounds
        scale = min(bounds_x, bounds_y) / 2
        
        # Generate spiral
        t = np.linspace(0, 6*np.pi, self.config.num_waypoints)
        a = scale / t[-1]  # Scale factor to fit within bounds
        
        x_vals = a * t * np.cos(t)
        y_vals = a * t * np.sin(t)
        
        # Generate height profile (wave pattern)
        z_amplitude = (self.config.max_height - self.config.min_height) / 2
        z_center = (self.config.max_height + self.config.min_height) / 2
        z_vals = z_center + z_amplitude * np.sin(t)
        
        waypoints = [
            Waypoint(float(x), float(y), float(z))
            for x, y, z in zip(x_vals, y_vals, z_vals)
        ]
        
        return waypoints
    
    def initialize_anchors(
        self, 
        strategy: AnchorPlacementStrategy = AnchorPlacementStrategy.FIXED
    ) -> Tuple[List[Anchor], List[Anchor]]:
        """
        Initialize both base (known) and unknown UWB anchors.
        
        Parameters:
        -----------
        strategy : AnchorPlacementStrategy
            Strategy for placing the anchors.
        
        Returns:
        --------
        Tuple[List[Anchor], List[Anchor]]
            Tuple of (base_anchors, unknown_anchors).
        """
        # Create bias and noise models based on configuration
        bias_model = BiasModel(**self.config.bias_model_params)
        noise_model = NoiseModel(**self.config.noise_model_params)

        # Initialize base anchors according to the strategy
        if strategy == AnchorPlacementStrategy.FIXED:
            base_anchors = [
                Anchor(anchor_id, position, bias_model, noise_model)
                for anchor_id, position in self.DEFAULT_BASE_ANCHORS
            ]
        elif strategy == AnchorPlacementStrategy.RANDOM:
            base_anchors = self._generate_random_anchors(self.config.num_base_anchors, "base", bias_model, noise_model)
        elif strategy == AnchorPlacementStrategy.CORNERS:
            base_anchors = self._generate_corner_anchors(bias_model, noise_model)
        elif strategy == AnchorPlacementStrategy.OPTIMIZED:
            base_anchors = self._generate_optimized_anchors(bias_model, noise_model)
        else:
            raise ValueError(f"Unsupported anchor placement strategy: {strategy}")
        
        # Generate unknown anchors with random placement
        unknown_anchors = []
        if self.config.num_unknown_anchors > 0:
            for i in range(self.config.num_unknown_anchors):
                bounds_x, bounds_y, _ = self.config.bounds
                unknown_position = np.random.uniform(
                    low=[-bounds_x, -bounds_y, 0],
                    high=[bounds_x, bounds_y, 0]
                )
                unknown_anchors.append(Anchor(f"unknown_{i}", unknown_position, bias_model, noise_model))
        
        return base_anchors, unknown_anchors
    
    def _generate_random_anchors(
        self, 
        num_anchors: int, 
        prefix: str,
        bias_model: BiasModel,
        noise_model: NoiseModel
    ) -> List[Anchor]:
        """
        Generate random anchor placements.
        
        Parameters:
        -----------
        num_anchors : int
            Number of anchors to generate.
        prefix : str
            Prefix for anchor IDs.
        bias_model : BiasModel
            Bias model for the anchors.
        noise_model : NoiseModel
            Noise model for the anchors.
            
        Returns:
        --------
        List[Anchor]
            List of randomly placed anchors.
        """
        bounds_x, bounds_y, _ = self.config.bounds
        
        anchors = []
        for i in range(num_anchors):
            position = np.random.uniform(
                low=[-bounds_x, -bounds_y, 0],
                high=[bounds_x, bounds_y, 0]
            )
            anchors.append(Anchor(f"{prefix}_{i}", position, bias_model, noise_model))
        
        return anchors
    
    def _generate_corner_anchors(
        self, 
        bias_model: BiasModel,
        noise_model: NoiseModel
    ) -> List[Anchor]:
        """
        Generate anchors at the corners of the environment.
        
        Parameters:
        -----------
        bias_model : BiasModel
            Bias model for the anchors.
        noise_model : NoiseModel
            Noise model for the anchors.
            
        Returns:
        --------
        List[Anchor]
            List of anchors placed at corners.
        """
        bounds_x, bounds_y, _ = self.config.bounds
        
        corners = [
            (f"corner_0", [-bounds_x, -bounds_y, 0]),
            (f"corner_1", [bounds_x, -bounds_y, 0]),
            (f"corner_2", [bounds_x, bounds_y, 0]),
            (f"corner_3", [-bounds_x, bounds_y, 0])
        ]
        
        return [
            Anchor(anchor_id, position, bias_model, noise_model)
            for anchor_id, position in corners
        ]
    
    def _generate_optimized_anchors(
        self, 
        bias_model: BiasModel,
        noise_model: NoiseModel
    ) -> List[Anchor]:
        """
        Generate optimally placed anchors.
        
        In a real implementation, this would use an optimization algorithm
        to place anchors for optimal GDOP (Geometric Dilution of Precision).
        For now, it defaults to corners plus center.
        
        Parameters:
        -----------
        bias_model : BiasModel
            Bias model for the anchors.
        noise_model : NoiseModel
            Noise model for the anchors.
            
        Returns:
        --------
        List[Anchor]
            List of optimally placed anchors.
        """
        # For now, just use corners plus a center anchor
        corner_anchors = self._generate_corner_anchors(bias_model, noise_model)
        
        # Add a center anchor
        center_anchor = Anchor("center", [0, 0, 0], bias_model, noise_model)
        
        return corner_anchors + [center_anchor]
    
    def initialize_environment(
        self, 
        waypoint_mode: WaypointMode = WaypointMode.OPPOSITE_EDGES,
        anchor_strategy: AnchorPlacementStrategy = AnchorPlacementStrategy.FIXED,
        interpolation_method: Union[str, InterpolationMethod] = 'spline'
    ):
        """
        Initialize the complete simulation environment.
        
        Parameters:
        -----------
        waypoint_mode : WaypointMode
            Method to use for generating waypoints.
        anchor_strategy : AnchorPlacementStrategy
            Strategy for placing anchors.
        interpolation_method : Union[str, InterpolationMethod]
            Method for interpolating the trajectory.
        """
        # Generate waypoints
        self.waypoints = self.generate_waypoints(waypoint_mode)
        
        # Initialize anchors
        self.base_anchors, self.unknown_anchors = self.initialize_anchors(anchor_strategy)
        
        # Create UWB network
        self.uwb_network = UWBNetwork(self.base_anchors + self.unknown_anchors)
        
        # Create trajectory
        self.drone_trajectory = Trajectory(
            speed=self.config.drone_speed,
            dt=self.config.dt,
            wait_time=self.config.wait_time
        )
        self.drone_trajectory.construct_trajectory(self.waypoints, interpolation_method)
        
        # Set initial drone position
        if self.waypoints:
            self.drone_position = self.waypoints[0].get_coordinates()
        else:
            self.drone_position = np.zeros(3)
            
        self.drone_progress = 0
        
        # Clear any previous results
        self.results.clear()
    
    def update_drone_position(self) -> np.ndarray:
        """
        Update the drone position according to the trajectory.
        
        Returns:
        --------
        np.ndarray
            New drone position [x, y, z].
        """
        if not self.drone_trajectory or self.drone_trajectory.num_points == 0:
            return self.drone_position
            
        trajectory_length = self.drone_trajectory.num_points
        
        if self.drone_progress < trajectory_length:
            # Get the next point on the trajectory
            waypoint = self.drone_trajectory.get_point_at_index(self.drone_progress)
            if waypoint is not None:
                new_position = waypoint.get_coordinates()
                self.drone_progress += 1
            else:
                # Fallback to current position
                new_position = self.drone_position
        else:
            # Reset to start if end is reached
            waypoint = self.drone_trajectory.get_point_at_index(0)
            if waypoint is not None:
                new_position = waypoint.get_coordinates()
                self.drone_progress = 1  # Set to 1 to advance on next update
            else:
                # Fallback to current position
                new_position = self.drone_position
        
        self.drone_position = new_position
        return new_position
    
    def measure_distances(
        self, 
        include_errors: bool = True,
        return_details: bool = False
    ) -> Union[Dict[AnchorID, float], Dict[AnchorID, MeasurementResult]]:
        """
        Measure distances from all anchors to the current drone position.
        
        Parameters:
        -----------
        include_errors : bool
            If True, apply bias and noise models to the measurements.
        return_details : bool
            If True, return detailed measurement results instead of just distances.
            
        Returns:
        --------
        Union[Dict[str, float], Dict[str, MeasurementResult]]
            Dictionary of anchor IDs to distance measurements or detailed results.
        """
        if not self.uwb_network:
            return {}
            
        return self.uwb_network.measure_distances(
            self.drone_position, 
            include_errors=include_errors,
            return_details=return_details
        )
    
    def get_remaining_waypoints(self) -> Tuple[List[Waypoint], List[Waypoint]]:
        """
        Get both passed and remaining waypoints based on trajectory progress.
        Handles cases where trajectory loops back on itself.
        
        Returns:
        --------
        Tuple[List[Waypoint], List[Waypoint]]
            Tuple of (passed_waypoints, remaining_waypoints).
        """
        if not self.drone_trajectory or not self.waypoints:
            return [], []
        
        # Map each waypoint to its index on the trajectory
        trajectory_points = np.column_stack((
            self.drone_trajectory.points_x,
            self.drone_trajectory.points_y,
            self.drone_trajectory.points_z
        ))
        
        # Get trajectory parameter for each waypoint (distance along trajectory)
        waypoint_parameters = []
        
        # Calculate cumulative distance along trajectory
        trajectory_distances = [0]
        for i in range(1, len(trajectory_points)):
            distance = np.linalg.norm(trajectory_points[i] - trajectory_points[i-1])
            trajectory_distances.append(trajectory_distances[-1] + distance)
        
        # Find the closest point for each waypoint and its corresponding parameter
        for wp in self.waypoints:
            wp_coords = wp.get_coordinates()
            wp_distances = np.linalg.norm(trajectory_points - wp_coords, axis=1)
            closest_idx = np.argmin(wp_distances)
            waypoint_parameters.append({
                'waypoint': wp,
                'index': closest_idx,
                'distance': trajectory_distances[closest_idx],
                'passed': False  # Will be updated later
            })
        
        # Sort waypoints by distance along trajectory
        waypoint_parameters.sort(key=lambda x: x['distance'])
        
        # Get the current position's distance along trajectory
        current_distance = trajectory_distances[min(self.drone_progress, len(trajectory_distances)-1)]
        
        # Mark waypoints as passed or remaining
        passed_waypoints = []
        remaining_waypoints = []
        
        # First pass: Handle waypoints with monotonically increasing indices
        prev_passed = False
        for i, wp_param in enumerate(waypoint_parameters):
            # A waypoint is passed if:
            # 1. It's before the current progress point in terms of distance
            # 2. OR it's very close to current position (within a tolerance)
            # This handles most standard cases
            if wp_param['distance'] <= current_distance:
                wp_param['passed'] = True
                prev_passed = True
            elif prev_passed and i > 0:
                # If we're very close to the next waypoint, consider it as the current one
                # This helps with transitions between waypoints
                distance_to_next = wp_param['distance'] - current_distance
                if distance_to_next < 0.1:  # Define an appropriate tolerance
                    wp_param['passed'] = True
                else:
                    prev_passed = False
        
        # Second pass: Special handling for ordered sections (respecting the waypoint order)
        # This ensures waypoints are processed in their given order
        for i in range(1, len(self.waypoints)):
            # If waypoint i-1 is not passed but waypoint i is marked as passed,
            # then waypoint i should not be considered passed yet
            if not waypoint_parameters[i-1]['passed'] and waypoint_parameters[i]['passed']:
                waypoint_parameters[i]['passed'] = False
        
        # Build the final lists
        for wp_param in waypoint_parameters:
            if wp_param['passed']:
                passed_waypoints.append(wp_param['waypoint'])
            else:
                remaining_waypoints.append(wp_param['waypoint'])
        
        return passed_waypoints, remaining_waypoints

    def reset_simulation(
        self, 
        waypoint_mode: Optional[WaypointMode] = None,
        anchor_strategy: Optional[AnchorPlacementStrategy] = None,
        interpolation_method: Optional[Union[str, InterpolationMethod]] = None
    ) -> None:
        """
        Reset the simulation with optionally new parameters.
        
        Parameters:
        -----------
        waypoint_mode : Optional[WaypointMode]
            If provided, use this mode to generate new waypoints.
            If None, keep the same waypoints.
        anchor_strategy : Optional[AnchorPlacementStrategy]
            If provided, use this strategy for placing anchors.
            If None, keep the same anchors.
        interpolation_method : Optional[Union[str, InterpolationMethod]]
            If provided, use this method for trajectory interpolation.
            If None, use the default 'spline' method.
        """
        if waypoint_mode is not None or anchor_strategy is not None:
            # Reinitialize the entire environment
            actual_waypoint_mode = waypoint_mode or WaypointMode.OPPOSITE_EDGES
            actual_anchor_strategy = anchor_strategy or AnchorPlacementStrategy.FIXED
            actual_interp_method = interpolation_method or 'spline'
            
            self.initialize_environment(
                waypoint_mode=actual_waypoint_mode,
                anchor_strategy=actual_anchor_strategy,
                interpolation_method=actual_interp_method
            )
        elif interpolation_method is not None:
            # Just reconstruct the trajectory with the new interpolation method
            if self.drone_trajectory and self.waypoints:
                self.drone_trajectory.construct_trajectory(self.waypoints, interpolation_method)
                
            # Reset drone position
            if self.waypoints:
                self.drone_position = self.waypoints[0].get_coordinates()
            self.drone_progress = 0
        else:
            # Just reset position to beginning
            if self.waypoints:
                self.drone_position = self.waypoints[0].get_coordinates()
            else:
                self.drone_position = np.zeros(3)
                
            self.drone_progress = 0
        
        # Clear simulation results
        self.results.clear()
    
    def run_simulation(
        self, 
        num_steps: int = 100, 
        include_errors: bool = True,
        return_details: bool = False,
        record_results: bool = True
    ) -> SimulationResult:
        """
        Run the simulation for a specified number of steps.
        
        Parameters:
        -----------
        num_steps : int
            Number of simulation steps to run.
        include_errors : bool
            If True, apply bias and noise models to measurements.
        return_details : bool
            If True, collect detailed measurement results.
        record_results : bool
            If True, record simulation results.
            
        Returns:
        --------
        SimulationResult
            Container with simulation results.
        """
        if record_results:
            self.results.clear()
            
        for _ in range(num_steps):
            # Update drone position
            self.update_drone_position()
            
            # Measure distances
            measurements = self.measure_distances(
                include_errors=include_errors,
                return_details=return_details
            )
            
            # Record results
            if record_results:
                timestamp = time.time()
                
                # Extract just the distance values if using detailed results
                if return_details and isinstance(measurements, dict):
                    distance_dict = {
                        anchor_id: result.measured_distance 
                        for anchor_id, result in measurements.items()
                    }
                    self.results.add_step(self.drone_position, distance_dict, timestamp)
                else:
                    self.results.add_step(self.drone_position, measurements, timestamp)
        
        return self.results
    
    def get_trajectory_stats(self) -> Optional[TrajectoryStats]:
        """
        Get statistics about the current trajectory.
        
        Returns:
        --------
        Optional[TrajectoryStats]
            Statistics about the trajectory, or None if no trajectory exists.
        """
        if not self.drone_trajectory:
            return None
            
        return self.drone_trajectory.get_trajectory_stats()
    
    def get_anchor_positions(self, include_unknown: bool = False) -> Dict[AnchorID, np.ndarray]:
        """
        Get the positions of all anchors.
        
        Parameters:
        -----------
        include_unknown : bool
            If True, include unknown anchors in the result.
            
        Returns:
        --------
        Dict[str, np.ndarray]
            Dictionary mapping anchor IDs to positions.
        """
        if not self.uwb_network:
            return {}
            
        # Filter anchors based on whether to include unknowns
        if include_unknown:
            return self.uwb_network.get_anchor_positions()
        else:
            anchor_ids = [anchor.anchor_id for anchor in self.base_anchors]
            return self.uwb_network.get_anchor_positions(anchor_ids)
    
    def save_simulation_state(self, filepath: Union[str, Path]) -> None:
        """
        Save the current simulation state to a JSON file.
        
        Parameters:
        -----------
        filepath : Union[str, Path]
            Path to save the simulation state.
        """
        # Create a dictionary with the simulation state
        state = {
            "config": self.config.to_dict(),
            "drone_position": self.drone_position.tolist(),
            "drone_progress": self.drone_progress,
            "results": self.results.to_dict(),
            "base_anchors": [
                {
                    "id": anchor.anchor_id,
                    "position": anchor.position.tolist(),
                    "bias_model": {
                        "constant_bias": anchor.bias_model.constant_bias,
                        "linear_bias": anchor.bias_model.linear_bias
                    },
                    "noise_model": {
                        "variance": anchor.noise_model.variance,
                        "outlier_probability": anchor.noise_model.outlier_probability,
                        "outlier_range": anchor.noise_model.outlier_range
                    }
                }
                for anchor in self.base_anchors
            ],
            "unknown_anchors": [
                {
                    "id": anchor.anchor_id,
                    "position": anchor.position.tolist(),
                    "bias_model": {
                        "constant_bias": anchor.bias_model.constant_bias,
                        "linear_bias": anchor.bias_model.linear_bias
                    },
                    "noise_model": {
                        "variance": anchor.noise_model.variance,
                        "outlier_probability": anchor.noise_model.outlier_probability,
                        "outlier_range": anchor.noise_model.outlier_range
                    }
                }
                for anchor in self.unknown_anchors
            ],
            "waypoints": [
                {
                    "x": waypoint.x,
                    "y": waypoint.y,
                    "z": waypoint.z
                }
                for waypoint in self.waypoints
            ]
        }
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=4)
    
    @classmethod
    def load_simulation_state(cls, filepath: Union[str, Path]) -> 'DroneSimulation':
        """
        Load a simulation state from a JSON file.
        
        Parameters:
        -----------
        filepath : Union[str, Path]
            Path to the simulation state file.
            
        Returns:
        --------
        DroneSimulation
            Loaded simulation instance.
        """
        with open(filepath, 'r') as f:
            state = json.load(f)
        
        # Create configuration
        config = SimulationConfig.from_dict(state.get("config", {}))
        
        # Create simulation instance
        simulation = cls(config)
        
        # Load waypoints
        simulation.waypoints = [
            Waypoint(wp["x"], wp["y"], wp["z"])
            for wp in state.get("waypoints", [])
        ]
        
        # Load base anchors
        simulation.base_anchors = []
        for anchor_data in state.get("base_anchors", []):
            bias_model = BiasModel(
                constant_bias=anchor_data["bias_model"]["constant_bias"],
                linear_bias=anchor_data["bias_model"]["linear_bias"]
            )
            noise_model = NoiseModel(
                variance=anchor_data["noise_model"]["variance"],
                outlier_probability=anchor_data["noise_model"]["outlier_probability"],
                outlier_range=tuple(anchor_data["noise_model"]["outlier_range"])
            )
            anchor = Anchor(
                anchor_data["id"],
                anchor_data["position"],
                bias_model,
                noise_model
            )
            simulation.base_anchors.append(anchor)
        
        # Load unknown anchors
        simulation.unknown_anchors = []
        for anchor_data in state.get("unknown_anchors", []):
            bias_model = BiasModel(
                constant_bias=anchor_data["bias_model"]["constant_bias"],
                linear_bias=anchor_data["bias_model"]["linear_bias"]
            )
            noise_model = NoiseModel(
                variance=anchor_data["noise_model"]["variance"],
                outlier_probability=anchor_data["noise_model"]["outlier_probability"],
                outlier_range=tuple(anchor_data["noise_model"]["outlier_range"])
            )
            anchor = Anchor(
                anchor_data["id"],
                anchor_data["position"],
                bias_model,
                noise_model
            )
            simulation.unknown_anchors.append(anchor)
        
        # Create UWB network
        simulation.uwb_network = UWBNetwork(simulation.base_anchors + simulation.unknown_anchors)
        
        # Create trajectory
        simulation.drone_trajectory = Trajectory(
            speed=config.drone_speed,
            dt=config.dt,
            wait_time=config.wait_time
        )
        if simulation.waypoints:
            simulation.drone_trajectory.construct_trajectory(simulation.waypoints)
        
        # Load drone state
        simulation.drone_position = np.array(state.get("drone_position", [0, 0, 0]))
        simulation.drone_progress = state.get("drone_progress", 0)
        
        # Load results
        results_data = state.get("results", {})
        simulation.results = SimulationResult()
        simulation.results.drone_positions = [
            np.array(pos) for pos in results_data.get("drone_positions", [])
        ]
        simulation.results.anchor_measurements = results_data.get("anchor_measurements", [])
        simulation.results.timestamps = results_data.get("timestamps", [])
        
        return simulation