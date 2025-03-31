"""
Drone Dynamics and Trajectory Implementation

This module provides comprehensive tools for constructing drone trajectories
and simulating drone dynamics. It supports various trajectory interpolation
methods and dynamics simulation with realistic physics.

Classes:
    Point3D: Immutable 3D point representation
    Waypoint: Represents a waypoint for the drone to fly through
    Trajectory: Constructs smooth trajectories through waypoints
    TrajectoryStats: Statistics about a constructed trajectory
    DroneDynamics: Simulates drone physics and control

Example:
    # Create waypoints
    waypoints = [
        Waypoint(0, 0, 0),
        Waypoint(5, 5, 5),
        Waypoint(10, 0, 2)
    ]
    
    # Create and construct a trajectory
    trajectory = Trajectory(speed=2.0)
    trajectory.construct_trajectory(waypoints, method='spline')
    
    # Use trajectory for drone control
    dynamics = DroneDynamics()
    positions, velocities = dynamics.follow_trajectory(trajectory)
"""

from __future__ import annotations

import numpy as np
from enum import Enum, auto
from dataclasses import dataclass, field
from scipy.interpolate import CubicSpline
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import splprep, splev
from typing import (
    List, Tuple, Optional, Dict, Union, Any,
    Callable, TypeVar, Generic, Iterable, Sequence
)


# Type aliases for improved readability
Position3D = Union[np.ndarray, List[float], Tuple[float, float, float]]
Vector3D = Union[np.ndarray, List[float], Tuple[float, float, float]]


class InterpolationMethod(Enum):
    """Enumeration of trajectory interpolation methods."""
    LINEAR = auto()
    SPLINE = auto()
    
    @classmethod
    def from_string(cls, method_str: str) -> 'InterpolationMethod':
        """Convert a string to an InterpolationMethod enum."""
        method_map = {
            'linear': cls.LINEAR,
            'spline': cls.SPLINE
        }
        
        method_lower = method_str.lower()
        if method_lower not in method_map:
            valid_methods = ', '.join(method_map.keys())
            raise ValueError(f"Unknown interpolation method: {method_str}. "
                             f"Valid methods are: {valid_methods}")
        
        return method_map[method_lower]


@dataclass(frozen=True)
class Point3D:
    """
    Immutable 3D point representation.
    
    This dataclass provides a lightweight, immutable representation of a 3D point
    with convenient conversion methods.
    
    Attributes:
    -----------
    x : float
        X-coordinate of the point.
    y : float
        Y-coordinate of the point.
    z : float
        Z-coordinate of the point.
    """
    x: float
    y: float
    z: float
    
    def as_array(self) -> np.ndarray:
        """Convert to numpy array."""
        return np.array([self.x, self.y, self.z])
    
    def distance_to(self, other: Point3D) -> float:
        """Calculate Euclidean distance to another point."""
        return np.linalg.norm(self.as_array() - other.as_array())
    
    def __repr__(self) -> str:
        """String representation of the point."""
        return f"Point3D({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


@dataclass
class Waypoint:
    """
    Represents a waypoint for the drone to fly through in 3D space.
    
    This class encapsulates a 3D position that the drone should pass through
    during its flight. Additional waypoint properties such as heading constraints
    or time constraints can be added as needed.
    
    Attributes:
    -----------
    x : float
        X-coordinate of the waypoint.
    y : float
        Y-coordinate of the waypoint.
    z : float
        Z-coordinate of the waypoint.
    """
    x: float
    y: float
    z: float
    
    def __post_init__(self) -> None:
        """Ensure coordinates are floats."""
        self.x = float(self.x)
        self.y = float(self.y)
        self.z = float(self.z)
    
    @classmethod
    def from_point(cls, point: Point3D) -> 'Waypoint':
        """
        Create a waypoint from a Point3D object.
        
        Parameters:
        -----------
        point : Point3D
            Source point to convert to a waypoint.
            
        Returns:
        --------
        Waypoint
            New waypoint with the same coordinates as the input point.
        """
        return cls(point.x, point.y, point.z)
    
    @classmethod
    def from_array(cls, array: Position3D) -> 'Waypoint':
        """
        Create a waypoint from a numpy array or list/tuple.
        
        Parameters:
        -----------
        array : Position3D
            3D coordinates as a numpy array, list, or tuple.
            
        Returns:
        --------
        Waypoint
            New waypoint with the coordinates from the input array.
            
        Raises:
        -------
        ValueError
            If the input is not a valid 3D position.
        """
        arr = np.asarray(array, dtype=float)
        if arr.shape != (3,):
            raise ValueError(f"Expected 3D array, got shape {arr.shape}")
        return cls(float(arr[0]), float(arr[1]), float(arr[2]))

    def to_point3d(self) -> Point3D:
        """
        Convert to an immutable Point3D.
        
        Returns:
        --------
        Point3D
            Immutable point with the same coordinates as this waypoint.
        """
        return Point3D(self.x, self.y, self.z)
    
    def get_coordinates(self) -> np.ndarray:
        """
        Return the coordinates as a numpy array.
        
        Returns:
        --------
        np.ndarray
            3D coordinates as a numpy array [x, y, z].
        """
        return np.array([self.x, self.y, self.z], dtype=float)
    
    def distance_to(self, other: Union['Waypoint', Position3D]) -> float:
        """
        Calculate Euclidean distance to another waypoint or position.
        
        Parameters:
        -----------
        other : Union[Waypoint, Position3D]
            Another waypoint or a 3D position to calculate distance to.
            
        Returns:
        --------
        float
            Euclidean distance between this waypoint and the other position.
        """
        if isinstance(other, Waypoint):
            other_coords = other.get_coordinates()
        else:
            other_coords = np.asarray(other, dtype=float)
            if other_coords.shape != (3,):
                raise ValueError(f"Expected 3D position, got shape {other_coords.shape}")
                
        return np.linalg.norm(self.get_coordinates() - other_coords)
    
    def __repr__(self) -> str:
        """
        String representation of the waypoint.
        
        Returns:
        --------
        str
            A string in the format "Waypoint(x, y, z)" with coordinates rounded to 2 decimal places.
        """
        return f"Waypoint({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    
    def __eq__(self, other: object) -> bool:
        """
        Check if this waypoint is equal to another waypoint.
        
        Two waypoints are considered equal if their x, y, and z coordinates are equal.
        
        Parameters:
        -----------
        other : object
            Object to compare with this waypoint.
            
        Returns:
        --------
        bool
            True if the waypoints are equal, False otherwise.
        """
        if not isinstance(other, Waypoint):
            return False
        return (self.x == other.x and self.y == other.y and self.z == other.z)

@dataclass
class TrajectoryStats:
    """
    Statistics about a constructed trajectory.
    
    This class encapsulates various metrics that describe the quality
    and characteristics of a trajectory.
    
    Attributes:
    -----------
    max_deviation : float
        Maximum deviation from expected distance between consecutive points.
    mean_deviation : float
        Mean deviation from expected distance.
    expected_distance : float
        Expected distance between consecutive points.
    constant_speed : bool
        Whether the trajectory maintains approximately constant speed.
    total_length : float
        Total length of the trajectory.
    duration : float
        Expected duration to traverse the trajectory at the specified speed.
    """
    max_deviation: float
    mean_deviation: float
    expected_distance: float
    constant_speed: bool
    total_length: float
    duration: float
    
    @property
    def max_deviation_percentage(self) -> float:
        """Maximum deviation as a percentage of expected distance."""
        if self.expected_distance == 0:
            return float('inf')
        return (self.max_deviation / self.expected_distance) * 100.0
    
    @property
    def mean_deviation_percentage(self) -> float:
        """Mean deviation as a percentage of expected distance."""
        if self.expected_distance == 0:
            return float('inf')
        return (self.mean_deviation / self.expected_distance) * 100.0


class Trajectory:
    """
    Represents a trajectory through a series of waypoints in 3D space.
    
    The trajectory can be constructed using either linear interpolation or
    cubic spline interpolation between waypoints, ensuring constant speed
    movement along the path.
    
    Attributes:
    -----------
    speed : float
        Desired speed of the drone in units per second.
    dt : float
        Time interval at which to sample the trajectory in seconds.
    points_x : np.ndarray
        X-coordinates of all points along the trajectory.
    points_y : np.ndarray
        Y-coordinates of all points along the trajectory.
    points_z : np.ndarray
        Z-coordinates of all points along the trajectory.
    waypoints : List[Waypoint]
        List of waypoints defining the path.
    num_points : int
        Number of points in the trajectory.
    interpolation_method : InterpolationMethod
        Method used for interpolation between waypoints.
    """

    def __init__(self, speed: float = 3.0, dt: float = 0.05, wait_time: float = 0.0) -> None:
        """
        Initialize the drone trajectory with specified speed and time interval.

        Parameters:
        -----------
        speed : float
            Desired speed of the drone in units per second. Default is 3.0.
        dt : float
            Time interval at which to sample the trajectory in seconds. Default is 0.05.
        """
        self.speed = float(speed)
        self.dt = float(dt)
        self.wait_time = float(wait_time)
        self.points_x = np.array([], dtype=float)
        self.points_y = np.array([], dtype=float)
        self.points_z = np.array([], dtype=float)
        self.waypoints: List[Waypoint] = []
        self.num_points = 0
        self.interpolation_method: Optional[InterpolationMethod] = None
        self._total_length: Optional[float] = None

    def construct_trajectory(
        self, 
        waypoints: List[Waypoint], 
        method: Union[str, InterpolationMethod] = 'spline'
    ) -> bool:
        """
        Construct a trajectory through the provided waypoints.
        
        Parameters:
        -----------
        waypoints : List[Waypoint]
            A list of Waypoint objects defining the path.
        method : Union[str, InterpolationMethod]
            Interpolation method to use: 'linear' or 'spline', or
            an InterpolationMethod enum value. Default is 'spline'.
            
        Returns:
        --------
        bool
            True if trajectory was successfully constructed, False otherwise.
        """
        if not waypoints or len(waypoints) < 2:
            self._reset_trajectory()
            return False
        
        # Store waypoints and convert method to enum if it's a string
        self.waypoints = waypoints.copy()
        if isinstance(method, str):
            self.interpolation_method = InterpolationMethod.from_string(method)
        else:
            self.interpolation_method = method
        
        # Construct trajectory using specified method
        if self.interpolation_method == InterpolationMethod.LINEAR:
            self._construct_linear_trajectory()
        elif self.interpolation_method == InterpolationMethod.SPLINE:
            self._construct_spline_trajectory()
        else:
            raise ValueError(f"Unsupported interpolation method: {method}")
            
        return True

    def _reset_trajectory(self) -> None:
        """Reset trajectory data."""
        self.points_x = np.array([], dtype=float)
        self.points_y = np.array([], dtype=float)
        self.points_z = np.array([], dtype=float)
        self.waypoints = []
        self.num_points = 0
        self.interpolation_method = None
        self._total_length = None

    def _construct_linear_trajectory(self) -> None:
        """
        Create a linear trajectory between waypoints with constant speed movement.
        
        This method distributes points along each segment proportionally to segment length
        and performs linear interpolation between waypoints. Additionally, it adds
        wait points at each waypoint position based on the specified wait time.
        """
        # Extract segments and calculate their lengths
        segments, total_length = self._calculate_segments()
        self._total_length = total_length
        
        # Calculate points needed for movement and waiting
        points_for_movement = max(int(total_length / (self.speed * self.dt)), 2)
        wait_points_per_waypoint = int(self.wait_time / self.dt)
        total_wait_points = wait_points_per_waypoint * len(self.waypoints)
        total_points_needed = points_for_movement + total_wait_points

        # Initialize output arrays
        self.points_x = np.zeros(total_points_needed, dtype=float)
        self.points_y = np.zeros(total_points_needed, dtype=float)
        self.points_z = np.zeros(total_points_needed, dtype=float)
        
        # Add initial wait points at the first waypoint
        current_point = 0
        if wait_points_per_waypoint > 0:
            self.points_x[0:wait_points_per_waypoint] = self.waypoints[0].x
            self.points_y[0:wait_points_per_waypoint] = self.waypoints[0].y
            self.points_z[0:wait_points_per_waypoint] = self.waypoints[0].z
            current_point = wait_points_per_waypoint

        # Distribute movement points across segments
        movement_point = 0
        for i, segment in enumerate(segments):
            # Calculate number of points for this segment proportional to its length
            segment_points = int(round((segment['length'] / total_length) * 
                                     (points_for_movement - 1)))
            
            # Ensure last segment contains remaining movement points
            if i == len(segments) - 1:  
                segment_points = points_for_movement - movement_point
            
            if segment_points > 0:
                # Generate interpolation parameters
                t = np.linspace(0, 1, segment_points)
                
                # Interpolate points
                segment_x = segment['start'].x + t * segment['vector'][0]
                segment_y = segment['start'].y + t * segment['vector'][1]
                segment_z = segment['start'].z + t * segment['vector'][2]
                
                # Store movement points
                self.points_x[current_point:current_point + segment_points] = segment_x
                self.points_y[current_point:current_point + segment_points] = segment_y
                self.points_z[current_point:current_point + segment_points] = segment_z
                
                current_point += segment_points
                movement_point += segment_points

                # Add wait points at the end of each segment (except the first waypoint)
                if wait_points_per_waypoint > 0 and i < len(segments) - 1:
                    self.points_x[current_point:current_point + wait_points_per_waypoint] = segment['end'].x
                    self.points_y[current_point:current_point + wait_points_per_waypoint] = segment['end'].y
                    self.points_z[current_point:current_point + wait_points_per_waypoint] = segment['end'].z
                    current_point += wait_points_per_waypoint

        # Add final wait points
        if wait_points_per_waypoint > 0:
            self.points_x[current_point:] = self.waypoints[-1].x
            self.points_y[current_point:] = self.waypoints[-1].y
            self.points_z[current_point:] = self.waypoints[-1].z
        
        # Ensure last point matches final waypoint
        self.points_x[-1] = self.waypoints[-1].x
        self.points_y[-1] = self.waypoints[-1].y
        self.points_z[-1] = self.waypoints[-1].z
        
        self.num_points = total_points_needed

    def _calculate_segments(self) -> Tuple[List[Dict[str, Any]], float]:
        """
        Calculate segment vectors and lengths between consecutive waypoints.
        
        Returns:
        --------
        Tuple[List[Dict[str, Any]], float]
            A tuple containing a list of segment dictionaries and the total path length.
            Each segment dictionary contains:
            - 'start': Starting waypoint
            - 'end': Ending waypoint
            - 'length': Segment length
            - 'vector': Vector from start to end
        """
        segments = []
        total_length = 0.0
        
        for i in range(len(self.waypoints) - 1):
            wp_start = self.waypoints[i]
            wp_end = self.waypoints[i + 1]
            
            # Calculate segment vector and length
            segment_vector = np.array([
                wp_end.x - wp_start.x, 
                wp_end.y - wp_start.y, 
                wp_end.z - wp_start.z
            ])
            segment_length = np.linalg.norm(segment_vector)
            
            segments.append({
                'start': wp_start,
                'end': wp_end,
                'length': segment_length,
                'vector': segment_vector
            })
            total_length += segment_length
            
        return segments, total_length

    def _calculate_arc_length(
        self, 
        spline_x: CubicSpline, 
        spline_y: CubicSpline, 
        spline_z: CubicSpline, 
        t_values: np.ndarray
    ) -> np.ndarray:
        """
        Calculate the arc length of a spline using analytical derivatives.
        
        Parameters:
        -----------
        spline_x : scipy.interpolate.CubicSpline
            Cubic spline for x-coordinate.
        spline_y : scipy.interpolate.CubicSpline
            Cubic spline for y-coordinate.
        spline_z : scipy.interpolate.CubicSpline
            Cubic spline for z-coordinate.
        t_values : np.ndarray
            Parameter values at which to evaluate the arc length.

        Returns:
        --------
        np.ndarray
            Cumulative arc length at each parameter value.
        """
        # Get derivatives of the splines
        dx_dt = spline_x.derivative()(t_values)
        dy_dt = spline_y.derivative()(t_values)
        dz_dt = spline_z.derivative()(t_values)
        
        # Calculate speed at each point
        speeds = np.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
        
        # Integrate speed to get arc length
        return cumulative_trapezoid(speeds, t_values, initial=0)

    def _construct_spline_trajectory(self, num_samples: int = 1000) -> None:
        """
        Construct a spline trajectory with constant speed movement.
        This method creates cubic splines through the waypoints and then
        reparameterizes the spline to achieve constant speed movement.
        
        Parameters:
        -----------
        num_samples : int
            Number of samples to use for arc length calculation. Default is 1000.
        """
        # Check if we have enough waypoints
        if len(self.waypoints) < 2:
            raise ValueError("At least two waypoints are required to construct a spline.")
        
        # Extract coordinates
        x_coords, y_coords, z_coords = zip(*[
            (wp.x, wp.y, wp.z) for wp in self.waypoints
        ])
        
        # Initial parameter space (chord-length parameterization for better results)
        distances = np.zeros(len(self.waypoints))
        for i in range(1, len(self.waypoints)):
            distances[i] = distances[i-1] + self.waypoints[i].distance_to(self.waypoints[i-1])
        
        if distances[-1] > 0:
            t_params = distances / distances[-1]
        else:
            # Fallback to uniform parameterization if all points are coincident
            t_params = np.linspace(0, 1, len(self.waypoints))
        
        # Ensure t_params are strictly increasing
        t_params = np.unique(t_params)
        
        # If we've lost waypoints due to duplicate parameters, we need to adjust the coordinate arrays
        if len(t_params) < len(self.waypoints):
            # Recalculate coordinate arrays with unique parameters
            unique_indices = []
            for i in range(len(distances)):
                if i == 0 or distances[i] > distances[i-1]:
                    unique_indices.append(i)
            
            x_coords = np.array(x_coords)[unique_indices]
            y_coords = np.array(y_coords)[unique_indices]
            z_coords = np.array(z_coords)[unique_indices]
        
        # Check if we still have enough points
        if len(t_params) < 2:
            raise ValueError("After removing duplicates, not enough unique waypoints remain.")
        
        try:
            # Create initial splines with natural boundary conditions
            spline_x = CubicSpline(t_params, x_coords, bc_type='natural')
            spline_y = CubicSpline(t_params, y_coords, bc_type='natural')
            spline_z = CubicSpline(t_params, z_coords, bc_type='natural')
        except ValueError as e:
            print(f"Error creating spline: {e}")
            print(f"t_params: {t_params}")
            print(f"x_coords: {x_coords}")
            print(f"y_coords: {y_coords}")
            print(f"z_coords: {z_coords}")
            
            # Alternative approach using scipy's splprep for parametric splines
            tck, u = splprep([x_coords, y_coords, z_coords], s=0)
            self._spline_tck = tck
            
            # Calculate total arc length using fine sampling
            u_fine = np.linspace(0, 1, num_samples)
            points = splev(u_fine, tck)
            
            # Calculate distances between consecutive points
            diffs = np.diff(points, axis=1)
            point_distances = np.sqrt(np.sum(diffs**2, axis=0))
            arc_lengths = np.concatenate(([0], np.cumsum(point_distances)))
            
            total_length = float(arc_lengths[-1])
            self._total_length = total_length
            
            # Calculate number of points needed for desired speed
            self.num_points = max(int(total_length / (self.speed * self.dt)), 2)
            
            # Create new parameter values that give equal arc length segments
            desired_distances = np.linspace(0, total_length, self.num_points)
            new_u_params = np.interp(desired_distances, arc_lengths, u_fine)
            
            # Sample the splines at the new parameter values
            points = splev(new_u_params, tck)
            self.points_x, self.points_y, self.points_z = points
            return
        
        # Calculate total arc length using fine sampling
        t_fine = np.linspace(0, 1, num_samples)
        arc_lengths = self._calculate_arc_length(spline_x, spline_y, spline_z, t_fine)
        total_length = float(arc_lengths[-1])
        self._total_length = total_length
        
        # Calculate number of points needed for desired speed
        self.num_points = max(int(total_length / (self.speed * self.dt)), 2)
        
        # Create new parameter values that give equal arc length segments
        desired_distances = np.linspace(0, total_length, self.num_points)
        new_t_params = np.interp(desired_distances, arc_lengths, t_fine)
        
        # Sample the splines at the new parameter values
        self.points_x = spline_x(new_t_params)
        self.points_y = spline_y(new_t_params)
        self.points_z = spline_z(new_t_params)

    def get_point_at_index(self, index: int) -> Optional[Waypoint]:
        """
        Get the trajectory point at the specified index.

        Parameters:
        -----------
        index : int
            Index of the point to retrieve.

        Returns:
        --------
        Optional[Waypoint]
            Waypoint object representing the point at the specified index,
            or None if the index is out of range.
        """
        if not (0 <= index < self.num_points):
            return None
            
        return Waypoint(
            self.points_x[index],
            self.points_y[index], 
            self.points_z[index]
        )

    def get_all_points(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get all trajectory points.

        Returns:
        --------
        Tuple[np.ndarray, np.ndarray, np.ndarray]
            A tuple containing three numpy arrays (x_points, y_points, z_points).
        """
        return self.points_x, self.points_y, self.points_z

    def get_points_as_array(self) -> np.ndarray:
        """
        Get all trajectory points as a Nx3 array.
        
        Returns:
        --------
        np.ndarray
            Array of shape (num_points, 3) containing all trajectory points.
        """
        return np.column_stack((self.points_x, self.points_y, self.points_z))

    def find_closest_point_index(self, position: Position3D) -> int:
        """
        Find the index of the closest trajectory point to the given position.

        Parameters:
        -----------
        position : Position3D
            A 3-element array-like object [x, y, z] representing a position.

        Returns:
        --------
        int
            Index of the closest point in the trajectory, or -1 if the trajectory is empty.
        """
        if self.num_points == 0:
            return -1
            
        pos_array = np.asarray(position, dtype=float)
        if pos_array.shape != (3,):
            raise ValueError(f"Expected 3D position, got shape {pos_array.shape}")
            
        x, y, z = pos_array
        distances = np.sqrt(
            (self.points_x - x)**2 + 
            (self.points_y - y)**2 + 
            (self.points_z - z)**2
        )
        
        return np.argmin(distances)
    
    def get_lookahead_point(
        self, 
        current_position: Position3D, 
        lookahead_distance: float,
        bounded: bool = True
    ) -> Optional[Waypoint]:
        """
        Find a point at the specified lookahead distance from the current position.

        Parameters:
        -----------
        current_position : Position3D
            A 3-element array [x, y, z] representing the current position.
        lookahead_distance : float
            The distance to look ahead along the path.
        bounded : bool
            If True, return the last waypoint if the lookahead distance exceeds
            the remaining path length. If False, return None in that case.

        Returns:
        --------
        Optional[Waypoint]
            Waypoint at the specified lookahead distance or None if the trajectory
            is empty or if the lookahead point is beyond the end of the trajectory
            and bounded is False.
        """
        if self.num_points == 0:
            return None
        
        closest_index = self.find_closest_point_index(current_position)
        if closest_index < 0:
            return None
            
        # If we're already at the last point and bounded is True, return it
        if closest_index >= self.num_points - 1:
            return self.get_point_at_index(self.num_points - 1) if bounded else None
            
        accumulated_distance = 0.0
        
        # Traverse the trajectory from the closest point
        for i in range(closest_index, self.num_points - 1):
            segment_distance = np.sqrt(
                (self.points_x[i+1] - self.points_x[i])**2 + 
                (self.points_y[i+1] - self.points_y[i])**2 + 
                (self.points_z[i+1] - self.points_z[i])**2
            )
            
            if accumulated_distance + segment_distance >= lookahead_distance:
                # Interpolate within this segment
                fraction = (lookahead_distance - accumulated_distance) / segment_distance
                
                x = self.points_x[i] + fraction * (self.points_x[i+1] - self.points_x[i])
                y = self.points_y[i] + fraction * (self.points_y[i+1] - self.points_y[i])
                z = self.points_z[i] + fraction * (self.points_z[i+1] - self.points_z[i])
                
                return Waypoint(x, y, z)
                
            accumulated_distance += segment_distance
        
        # If we've reached the end of the trajectory, return the last point if bounded
        return self.get_point_at_index(self.num_points - 1) if bounded else None

    def get_trajectory_stats(self) -> TrajectoryStats:
        """
        Compute statistics about the trajectory.
        
        Returns:
        --------
        TrajectoryStats
            Object containing various statistics about the trajectory.
        """
        if self.num_points < 2:
            return TrajectoryStats(
                max_deviation=0.0,
                mean_deviation=0.0,
                expected_distance=self.speed * self.dt,
                constant_speed=True,
                total_length=0.0,
                duration=0.0
            )
            
        dx = np.diff(self.points_x)
        dy = np.diff(self.points_y)
        dz = np.diff(self.points_z)
        
        distances = np.sqrt(dx**2 + dy**2 + dz**2)
        expected_distance = self.speed * self.dt
        
        deviations = np.abs(distances - expected_distance)
        max_deviation = float(np.max(deviations))
        mean_deviation = float(np.mean(deviations))
        
        # Calculate total length and duration
        total_length = float(np.sum(distances))
        duration = total_length / self.speed
        
        # Consider speed constant if max deviation is less than 5% of expected distance
        is_constant = max_deviation < 0.05 * expected_distance
        
        return TrajectoryStats(
            max_deviation=max_deviation,
            mean_deviation=mean_deviation,
            expected_distance=expected_distance,
            constant_speed=is_constant,
            total_length=total_length,
            duration=duration
        )
    
    def get_total_length(self) -> float:
        """
        Get the total length of the trajectory.
        
        Returns:
        --------
        float
            Total length of the trajectory in distance units.
        """
        if self._total_length is not None:
            return self._total_length
            
        if self.num_points < 2:
            return 0.0
            
        dx = np.diff(self.points_x)
        dy = np.diff(self.points_y)
        dz = np.diff(self.points_z)
        
        distances = np.sqrt(dx**2 + dy**2 + dz**2)
        self._total_length = float(np.sum(distances))
        return self._total_length
    
    def get_expected_duration(self) -> float:
        """
        Get the expected duration to traverse the trajectory at the specified speed.
        
        Returns:
        --------
        float
            Expected duration in seconds.
        """
        return self.get_total_length() / self.speed

    def __len__(self) -> int:
        """Return the number of points in the trajectory."""
        return self.num_points
    
    def __bool__(self) -> bool:
        """Return True if the trajectory has points, False otherwise."""
        return self.num_points > 0
    
    def __repr__(self) -> str:
        """Return string representation of the trajectory."""
        return (f"Trajectory(num_points={self.num_points}, "
                f"length={self.get_total_length():.2f}, "
                f"speed={self.speed:.2f}, "
                f"method={self.interpolation_method})")


class DroneDynamics:
    """
    Simulates the dynamics of a drone following a trajectory.
    
    This class implements a drone dynamics model that can simulate
    the drone's movement, accounting for physical constraints like maximum 
    acceleration and velocity. It includes a PD controller for trajectory following.
    
    Attributes:
    -----------
    mass : float
        Mass of the drone in kg.
    max_thrust : float
        Maximum thrust force in Newtons.
    drag_coefficient : float
        Coefficient of drag.
    position : np.ndarray
        Current position of the drone [x, y, z].
    velocity : np.ndarray
        Current velocity of the drone [vx, vy, vz].
    acceleration : np.ndarray
        Current acceleration of the drone [ax, ay, az].
    gravity : np.ndarray
        Gravity vector [0, 0, -9.81].
    """
    
    def __init__(
        self, 
        mass: float = 1.0, 
        max_thrust: float = 15.0, 
        drag_coefficient: float = 0.1
    ) -> None:
        """
        Initialize the drone dynamics model.
        
        Parameters:
        -----------
        mass : float
            Mass of the drone in kg. Default is 1.0.
        max_thrust : float
            Maximum thrust force in Newtons. Default is 15.0.
        drag_coefficient : float
            Coefficient of drag. Default is 0.1.
        """
        self.mass = float(mass)
        self.max_thrust = float(max_thrust)
        self.drag_coefficient = float(drag_coefficient)
        
        # State variables
        self.position = np.zeros(3, dtype=float)  # [x, y, z]
        self.velocity = np.zeros(3, dtype=float)  # [vx, vy, vz]
        self.acceleration = np.zeros(3, dtype=float)  # [ax, ay, az]
        
        # Gravity
        self.gravity = np.array([0, 0, -9.81], dtype=float)
        
        # Controller gains
        self.kp = 2.0  # Proportional gain
        self.kd = 1.0  # Derivative gain
    
    def set_controller_gains(self, kp: float, kd: float) -> None:
        """
        Set the PD controller gains.
        
        Parameters:
        -----------
        kp : float
            Proportional gain.
        kd : float
            Derivative gain.
        """
        self.kp = float(kp)
        self.kd = float(kd)
    
    def update(
        self, 
        target_position: Position3D, 
        dt: float
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Update the drone's state based on a target position.
        
        Parameters:
        -----------
        target_position : Position3D
            Target position [x, y, z] for the drone to move toward.
        dt : float
            Time step in seconds for the simulation.
            
        Returns:
        --------
        Tuple[np.ndarray, np.ndarray, np.ndarray]
            Updated position, velocity, and acceleration vectors.
        """
        # Ensure target position is a numpy array
        target_pos = np.asarray(target_position, dtype=float)
        if target_pos.shape != (3,):
            raise ValueError(f"Expected 3D target position, got shape {target_pos.shape}")
        
        # Calculate position error
        position_error = target_pos - self.position
        
        # Calculate desired acceleration using PD control
        desired_acceleration = self.kp * position_error - self.kd * self.velocity
        
        # Add gravity compensation
        desired_acceleration -= self.gravity
        
        # Apply thrust limits
        thrust_magnitude = np.linalg.norm(desired_acceleration)
        max_acceleration = self.max_thrust / self.mass
        
        if thrust_magnitude > max_acceleration:
            # Scale down acceleration to respect thrust limit
            desired_acceleration = desired_acceleration * (max_acceleration / thrust_magnitude)
        
        # Apply drag force (quadratic drag model)
        velocity_magnitude = np.linalg.norm(self.velocity)
        if velocity_magnitude > 0:
            drag = -self.drag_coefficient * self.velocity * velocity_magnitude
            drag_acceleration = drag / self.mass
        else:
            drag_acceleration = np.zeros(3, dtype=float)
        
        # Calculate final acceleration
        self.acceleration = desired_acceleration + drag_acceleration + self.gravity
        
        # Update velocity and position using semi-implicit Euler integration
        # (more stable than explicit Euler)
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        
        return self.position.copy(), self.velocity.copy(), self.acceleration.copy()
    
    def follow_trajectory(
        self, 
        trajectory: Trajectory, 
        dt: float = 0.01,
        lookahead_distance: float = 1.0,
        timeout_seconds: float = 60.0,
        position_threshold: float = 0.1
    ) -> Dict[str, List[np.ndarray]]:
        """
        Simulate the drone following a trajectory.
        
        Parameters:
        -----------
        trajectory : Trajectory
            Trajectory object defining the path to follow.
        dt : float
            Time step in seconds for the simulation. Default is 0.01.
        lookahead_distance : float
            Distance ahead of current position to aim for. Default is 1.0.
        timeout_seconds : float
            Maximum simulation time in seconds. Default is 60.0.
        position_threshold : float
            Distance threshold to consider the final waypoint reached. Default is 0.1.
            
        Returns:
        --------
        Dict[str, List[np.ndarray]]
            Dictionary containing lists of positions, velocities, accelerations,
            and target points over time.
        """
        if len(trajectory) == 0:
            return {
                'positions': [self.position.copy()],
                'velocities': [self.velocity.copy()],
                'accelerations': [self.acceleration.copy()],
                'targets': []
            }
            
        # Initialize result containers
        positions = [self.position.copy()]
        velocities = [self.velocity.copy()]
        accelerations = [self.acceleration.copy()]
        targets = []
        
        # Get final waypoint
        final_waypoint = trajectory.get_point_at_index(trajectory.num_points - 1)
        if final_waypoint is None:
            # This shouldn't happen if len(trajectory) > 0, but just in case
            return {
                'positions': positions,
                'velocities': velocities,
                'accelerations': accelerations,
                'targets': targets
            }
            
        final_position = final_waypoint.get_coordinates()
        
        # Simulation loop parameters
        simulation_time = 0.0
        target_reached = False
        
        # Continue until we reach the target or timeout
        while not target_reached and simulation_time < timeout_seconds:
            # Get target point ahead on trajectory
            target_point = trajectory.get_lookahead_point(
                self.position, lookahead_distance
            )
            
            if target_point is None:
                # This shouldn't happen with bounded=True (default), but just in case
                break
                
            target_position = target_point.get_coordinates()
            targets.append(target_position.copy())
            
            # Update drone state
            self.update(target_position, dt)
            
            # Store state
            positions.append(self.position.copy())
            velocities.append(self.velocity.copy())
            accelerations.append(self.acceleration.copy())
            
            # Check if we've reached the final position
            distance_to_final = np.linalg.norm(self.position - final_position)
            if distance_to_final <= position_threshold:
                target_reached = True
                
            # Update simulation time
            simulation_time += dt
        
        return {
            'positions': positions,
            'velocities': velocities,
            'accelerations': accelerations,
            'targets': targets,
            'target_reached': target_reached,
            'simulation_time': simulation_time
        }
    
    def reset_state(
        self,
        position: Optional[Position3D] = None,
        velocity: Optional[Vector3D] = None,
        acceleration: Optional[Vector3D] = None
    ) -> None:
        """
        Reset the drone's state.
        
        Parameters:
        -----------
        position : Position3D, optional
            New position for the drone. If None, reset to origin.
        velocity : Vector3D, optional
            New velocity for the drone. If None, reset to zero.
        acceleration : Vector3D, optional
            New acceleration for the drone. If None, reset to zero.
        """
        self.position = np.zeros(3, dtype=float) if position is None else np.asarray(position, dtype=float)
        self.velocity = np.zeros(3, dtype=float) if velocity is None else np.asarray(velocity, dtype=float)
        self.acceleration = np.zeros(3, dtype=float) if acceleration is None else np.asarray(acceleration, dtype=float)
