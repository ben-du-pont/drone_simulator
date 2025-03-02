import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum, auto

from drone_uwb_simulator.UWB_protocol import Anchor, BiasModel, NoiseModel
from drone_uwb_simulator.drone_dynamics import Waypoint, Trajectory


@dataclass
class SimulationConfig:
    """
    Configuration parameters for the drone simulation environment.
    
    Attributes:
        dt: Time step for simulation in seconds.
        drone_speed: Speed of the drone in meters per second.
        num_waypoints: Number of waypoints to generate for random trajectories.
        bounds: Environment boundaries as (x_bound, y_bound, z_bound) in meters.
    """
    dt: float = 0.05
    drone_speed: float = 1.0
    num_waypoints: int = 15
    bounds: Tuple[float, float, float] = (5.0, 5.0, 5.0)


class WaypointMode(Enum):
    """Enumeration of available waypoint generation modes."""
    MANUAL = auto()
    RANDOM = auto()
    OPPOSITE_EDGES = auto()


class DroneSimulation:
    """
    Simulates a drone moving through an environment with UWB anchors.
    
    This class manages the complete simulation environment including:
    - Waypoint generation and trajectory planning
    - Base and unknown UWB anchor placement
    - Drone movement and position updates
    """
    
    def __init__(self, config: Optional[SimulationConfig] = None):
        """
        Initialize the drone simulation environment.
        
        Args:
            config: Configuration parameters for the simulation.
                   If None, default configuration is used.
        """
        self.config = config or SimulationConfig()
        
        # Initialize simulation components
        self.waypoints = []
        self.base_anchors = []
        self.unknown_anchors = []
        self.drone_trajectory = None
        
        # Initialize drone state
        self.drone_progress = 0
        self.drone_position = np.zeros(3)
        
        # Set up the environment
        self.initialize_environment()
    
    def generate_waypoints(self, mode: WaypointMode = WaypointMode.OPPOSITE_EDGES) -> List[Waypoint]:
        """
        Generate waypoints according to the specified mode.
        
        Args:
            mode: Method to use for generating waypoints.
            
        Returns:
            Generated list of waypoints.
        """
        waypoint_generators = {
            WaypointMode.RANDOM: self._generate_random_waypoints,
            WaypointMode.OPPOSITE_EDGES: self._generate_opposite_edges_waypoints,
            WaypointMode.MANUAL: self._generate_manual_waypoints
        }
        
        return waypoint_generators[mode]()
    
    def _generate_random_waypoints(self) -> List[Waypoint]:
        """Generate random waypoints within environment bounds."""
        bounds_x, bounds_y, bounds_z = self.config.bounds
        
        # Start at origin
        waypoints = [Waypoint(0, 0, 0)]
        
        # Generate remaining random waypoints
        random_points = np.random.uniform(
            low=[-bounds_x, -bounds_y, 0],
            high=[bounds_x, bounds_y, bounds_z],
            size=(self.config.num_waypoints - 1, 3)
        )
        
        for x, y, z in random_points:
            waypoints.append(Waypoint(x, y, z))
            
        return waypoints
    
    def _generate_opposite_edges_waypoints(self) -> List[Waypoint]:
        """Generate waypoints on opposite edges of the environment."""
        bounds_x, bounds_y, bounds_z = self.config.bounds
        
        # Generate first point on edge
        x1 = np.random.choice([-bounds_x, bounds_x])
        y1 = np.random.uniform(-bounds_y, bounds_y)
        z1 = np.random.uniform(0, bounds_z)
        
        # Generate opposite point
        x2 = -x1
        y2 = np.random.choice([-bounds_y, bounds_y]) if abs(x1) == bounds_x else np.random.uniform(-bounds_y, bounds_y)
        z2 = bounds_z - z1
        
        # Generate intermediate points
        middle_points = np.random.uniform(
            low=[-bounds_x/2, -bounds_y/2, 0],
            high=[bounds_x/2, bounds_y/2, bounds_z/2],
            size=(3, 3)
        )
        
        return [
            Waypoint(x1, y1, z1),
            *[Waypoint(x, y, z) for x, y, z in middle_points],
            Waypoint(x2, y2, z2)
        ]
    
    def _generate_manual_waypoints(self) -> List[Waypoint]:
        """Generate a predefined set of waypoints."""
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
    
    def initialize_anchors(self) -> Tuple[List[Anchor], List[Anchor]]:
        """
        Initialize both base (known) and unknown UWB anchors.
        
        Returns:
            Tuple of (base_anchors, unknown_anchors).
        """
        # Common bias and noise models for all anchors
        bias_model = BiasModel(0.0951, 1.0049)
        noise_model = NoiseModel(0.2, 0.05, (0.2, 0.3))

        # Base anchors with fixed positions
        base_anchors = [
            Anchor("0", [-1, -1, 0], bias_model, noise_model),
            Anchor("1", [1, 0, 0], bias_model, noise_model),
            Anchor("2", [0, 3, 0], bias_model, noise_model),
            Anchor("3", [0, 6, 0], bias_model, noise_model)
        ]
        
        # Unknown anchors with random placement
        bounds_x, bounds_y, _ = self.config.bounds
        unknown_position = np.random.uniform(
            low=[-bounds_x, -bounds_y, 0],
            high=[bounds_x, bounds_y, 0]
        )
        
        unknown_anchors = [
            Anchor("4", unknown_position, bias_model, noise_model),
        ]
        
        return base_anchors, unknown_anchors
    
    def initialize_environment(self, waypoint_mode: WaypointMode = WaypointMode.OPPOSITE_EDGES):
        """
        Initialize the complete simulation environment.
        
        Args:
            waypoint_mode: Method to use for generating waypoints.
        """
        # Generate waypoints
        self.waypoints = self.generate_waypoints(waypoint_mode)
        
        # Initialize anchors
        self.base_anchors, self.unknown_anchors = self.initialize_anchors()
        
        # Create trajectory
        self.drone_trajectory = Trajectory(
            speed=self.config.drone_speed,
            dt=self.config.dt
        )
        self.drone_trajectory.construct_trajectory(self.waypoints)
        
        # Set initial drone position
        self.drone_position = np.array(self.waypoints[0].get_coordinates())
        self.drone_progress = 0
    
    def update_drone_position(self) -> np.ndarray:
        """
        Update the drone position according to the trajectory.
        
        Returns:
            New drone position [x, y, z].
        """
        trajectory_length = len(self.drone_trajectory.points_x)
        
        if self.drone_progress < trajectory_length:
            new_position = np.array([
                self.drone_trajectory.points_x[self.drone_progress],
                self.drone_trajectory.points_y[self.drone_progress],
                self.drone_trajectory.points_z[self.drone_progress]
            ])
            self.drone_progress += 1
        else:
            # Reset to start if end is reached
            new_position = np.array([
                self.drone_trajectory.points_x[0],
                self.drone_trajectory.points_y[0],
                self.drone_trajectory.points_z[0]
            ])
            self.drone_progress = 1  # Set to 1 to advance on next update
        
        self.drone_position = new_position
        return new_position
    
    def get_remaining_waypoints(self) -> List[Waypoint]:
        """
        Get waypoints that haven't been visited yet.
        
        Returns:
            List of unvisited waypoints.
        """
        if not self.drone_trajectory:
            return self.waypoints
            
        # Find closest point on trajectory to current position
        trajectory_points = np.column_stack((
            self.drone_trajectory.points_x,
            self.drone_trajectory.points_y,
            self.drone_trajectory.points_z
        ))
        
        distances = np.linalg.norm(trajectory_points - self.drone_position, axis=1)
        current_index = np.argmin(distances)
        
        # Map each waypoint to its closest point on the trajectory
        waypoint_indices = []
        for wp in self.waypoints:
            wp_coords = np.array(wp.get_coordinates())
            wp_distances = np.linalg.norm(trajectory_points - wp_coords, axis=1)
            waypoint_indices.append(np.argmin(wp_distances))
        
        # Return waypoints that are ahead on the trajectory
        return [
            wp for wp, idx in zip(self.waypoints, waypoint_indices)
            if idx > current_index
        ]

    def reset_simulation(self, waypoint_mode: Optional[WaypointMode] = None):
        """
        Reset the simulation with optionally new waypoint generation mode.
        
        Args:
            waypoint_mode: If provided, use this mode to generate new waypoints.
                          If None, keep the same waypoints.
        """
        if waypoint_mode is not None:
            self.initialize_environment(waypoint_mode)
        else:
            # Just reset position to beginning
            self.drone_position = np.array(self.waypoints[0].get_coordinates())
            self.drone_progress = 0