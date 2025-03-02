import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import cumulative_trapezoid


class Waypoint:
    """Represents a waypoint for the drone to fly through in 3D space."""

    def __init__(self, x, y, z):
        """
        Initialize a waypoint with 3D coordinates.

        Parameters:
        -----------
        x : float
            X-coordinate of the waypoint.
        y : float
            Y-coordinate of the waypoint.
        z : float
            Z-coordinate of the waypoint.
        """
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        """Return the coordinates as a numpy array."""
        return np.array([self.x, self.y, self.z])
    
    def __repr__(self):
        """String representation of the waypoint."""
        return f"Waypoint({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


class Trajectory:
    """
    Represents a trajectory through a series of waypoints in 3D space.
    
    The trajectory can be constructed using either linear interpolation or
    cubic spline interpolation between waypoints, ensuring constant speed
    movement along the path.
    """

    def __init__(self, speed=3.0, dt=0.05):
        """
        Initialize the drone trajectory with specified speed and time interval.

        Parameters:
        -----------
        speed : float
            Desired speed of the drone in units per second. Default is 3.0.
        dt : float
            Time interval at which to sample the trajectory in seconds. Default is 0.05.
        """
        self.speed = speed
        self.dt = dt
        self.points_x = np.array([])
        self.points_y = np.array([])
        self.points_z = np.array([])
        self.waypoints = []
        self.num_points = 0
        self.interpolation_method = None

    def construct_trajectory(self, waypoints, method='spline'):
        """
        Construct a trajectory through the provided waypoints.
        
        Parameters:
        -----------
        waypoints : list
            A list of Waypoint objects defining the path.
        method : str
            Interpolation method to use: 'linear' or 'spline'. Default is 'spline'.
            
        Returns:
        --------
        bool
            True if trajectory was successfully constructed, False otherwise.
        """
        if not waypoints or len(waypoints) < 2:
            self._reset_trajectory()
            return False
            
        self.waypoints = waypoints
        self.interpolation_method = method
        
        if method.lower() == 'linear':
            self._construct_linear_trajectory()
        elif method.lower() == 'spline':
            self._construct_spline_trajectory()
        else:
            raise ValueError(f"Unknown interpolation method: {method}. Use 'linear' or 'spline'.")
            
        return True

    def _reset_trajectory(self):
        """Reset trajectory data."""
        self.points_x = np.array([])
        self.points_y = np.array([])
        self.points_z = np.array([])
        self.waypoints = []
        self.num_points = 0
        self.interpolation_method = None

    def _construct_linear_trajectory(self):
        """
        Create a linear trajectory between waypoints with constant speed movement.
        
        This method distributes points along each segment proportionally to segment length
        and performs linear interpolation between waypoints.
        """
        # Calculate segment lengths and total path length
        segments = []
        total_length = 0
        
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

        # Calculate total number of points needed for desired speed
        total_points_needed = max(int(total_length / (self.speed * self.dt)), 2)
        
        # Initialize output arrays
        self.points_x = np.zeros(total_points_needed)
        self.points_y = np.zeros(total_points_needed)
        self.points_z = np.zeros(total_points_needed)
        
        # Distribute points across segments
        current_point = 0
        for segment in segments:
            # Calculate number of points for this segment proportional to its length
            segment_points = int(round((segment['length'] / total_length) * 
                                     (total_points_needed - 1)))
            
            # Ensure last segment contains remaining points
            if segment == segments[-1]:  
                segment_points = total_points_needed - current_point
            
            if segment_points > 0:
                # Generate interpolation parameters
                t = np.linspace(0, 1, segment_points)
                
                # Interpolate points
                segment_x = segment['start'].x + t * segment['vector'][0]
                segment_y = segment['start'].y + t * segment['vector'][1]
                segment_z = segment['start'].z + t * segment['vector'][2]
                
                # Store points
                self.points_x[current_point:current_point + segment_points] = segment_x
                self.points_y[current_point:current_point + segment_points] = segment_y
                self.points_z[current_point:current_point + segment_points] = segment_z
                
                current_point += segment_points
        
        # Ensure last point matches final waypoint
        self.points_x[-1] = self.waypoints[-1].x
        self.points_y[-1] = self.waypoints[-1].y
        self.points_z[-1] = self.waypoints[-1].z
        
        self.num_points = total_points_needed

    def _calculate_arc_length(self, spline_x, spline_y, spline_z, t_values):
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

    def _construct_spline_trajectory(self):
        """
        Construct a spline trajectory with constant speed movement.
        
        This method creates cubic splines through the waypoints and then 
        reparameterizes the spline to achieve constant speed movement.
        """
        # Extract coordinates
        x_coords, y_coords, z_coords = zip(*[
            (wp.x, wp.y, wp.z) for wp in self.waypoints
        ])
        
        # Initial parameter space
        t_params = np.linspace(0, 1, len(self.waypoints))
        
        # Create initial splines
        spline_x = CubicSpline(t_params, x_coords)
        spline_y = CubicSpline(t_params, y_coords)
        spline_z = CubicSpline(t_params, z_coords)
        
        # Calculate total arc length using fine sampling
        t_fine = np.linspace(0, 1, 1000)
        arc_lengths = self._calculate_arc_length(spline_x, spline_y, spline_z, t_fine)
        total_length = arc_lengths[-1]
        
        # Calculate number of points needed for desired speed
        self.num_points = max(int(total_length / (self.speed * self.dt)), 2)
        
        # Create new parameter values that give equal arc length segments
        desired_distances = np.linspace(0, total_length, self.num_points)
        new_t_params = np.interp(desired_distances, arc_lengths, t_fine)
        
        # Sample the splines at the new parameter values
        self.points_x = spline_x(new_t_params)
        self.points_y = spline_y(new_t_params)
        self.points_z = spline_z(new_t_params)

    def get_point_at_index(self, index):
        """
        Get the trajectory point at the specified index.

        Parameters:
        -----------
        index : int
            Index of the point to retrieve.

        Returns:
        --------
        Waypoint
            Waypoint object representing the point at the specified index.
        """
        if not (0 <= index < self.num_points):
            raise IndexError(f"Index {index} out of range for trajectory with {self.num_points} points")
            
        return Waypoint(
            self.points_x[index],
            self.points_y[index], 
            self.points_z[index]
        )

    def get_all_points(self):
        """
        Get all trajectory points.

        Returns:
        --------
        tuple
            A tuple containing three numpy arrays (x_points, y_points, z_points).
        """
        return self.points_x, self.points_y, self.points_z

    def find_closest_point_index(self, position):
        """
        Find the index of the closest trajectory point to the given position.

        Parameters:
        -----------
        position : array-like
            A 3-element array-like object [x, y, z] representing a position.

        Returns:
        --------
        int
            Index of the closest point in the trajectory.
        """
        if self.num_points == 0:
            return -1
            
        x, y, z = position
        distances = np.sqrt(
            (self.points_x - x)**2 + 
            (self.points_y - y)**2 + 
            (self.points_z - z)**2
        )
        
        return np.argmin(distances)
    
    def get_lookahead_point(self, current_position, lookahead_distance):
        """
        Find a point at the specified lookahead distance from the current position.

        Parameters:
        -----------
        current_position : array-like
            A 3-element array [x, y, z] representing the current position.
        lookahead_distance : float
            The distance to look ahead along the path.

        Returns:
        --------
        Waypoint
            Waypoint at the specified lookahead distance or the last waypoint
            if the lookahead distance exceeds the path length.
        """
        closest_index = self.find_closest_point_index(current_position)
        
        if closest_index < 0 or closest_index >= self.num_points - 1:
            return self.get_point_at_index(self.num_points - 1) if self.num_points > 0 else None
            
        accumulated_distance = 0.0
        
        # Traverse the trajectory from the closest point
        for i in range(closest_index, self.num_points - 1):
            segment_distance = np.sqrt(
                (self.points_x[i+1] - self.points_x[i])**2 + 
                (self.points_y[i+1] - self.points_y[i])**2 + 
                (self.points_z[i+1] - self.points_z[i])**2
            )
            
            accumulated_distance += segment_distance
            
            if accumulated_distance >= lookahead_distance:
                return self.get_point_at_index(i+1)
        
        # If we've reached the end of the trajectory
        return self.get_point_at_index(self.num_points - 1)

    def verify_constant_speed(self):
        """
        Verify that points along the trajectory are approximately equidistant.
        
        Returns:
        --------
        dict
            A dictionary containing:
            - 'max_deviation': Maximum deviation from expected distance
            - 'mean_deviation': Mean deviation from expected distance
            - 'expected_distance': Expected distance between points
            - 'constant_speed': Boolean indicating if speed is constant within tolerance
        """
        if self.num_points < 2:
            return {
                'max_deviation': 0.0,
                'mean_deviation': 0.0,
                'expected_distance': self.speed * self.dt,
                'constant_speed': True
            }
            
        dx = np.diff(self.points_x)
        dy = np.diff(self.points_y)
        dz = np.diff(self.points_z)
        
        distances = np.sqrt(dx**2 + dy**2 + dz**2)
        expected_distance = self.speed * self.dt
        
        deviations = np.abs(distances - expected_distance)
        max_deviation = np.max(deviations)
        mean_deviation = np.mean(deviations)
        
        # Consider speed constant if max deviation is less than 5% of expected distance
        is_constant = max_deviation < 0.05 * expected_distance
        
        return {
            'max_deviation': max_deviation,
            'mean_deviation': mean_deviation,
            'expected_distance': expected_distance,
            'constant_speed': is_constant
        }


# Unused for now, but could be useful for future extensions
class DroneDynamics:
    """
    Simulates the dynamics of a drone following a trajectory.
    
    This class implements a simplified drone dynamics model that can simulate
    the drone's movement, accounting for physical constraints like maximum 
    acceleration and velocity.
    """
    
    def __init__(self, mass=1.0, max_thrust=15.0, drag_coefficient=0.1):
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
        self.mass = mass
        self.max_thrust = max_thrust
        self.drag_coefficient = drag_coefficient
        
        # State variables
        self.position = np.zeros(3)  # [x, y, z]
        self.velocity = np.zeros(3)  # [vx, vy, vz]
        self.acceleration = np.zeros(3)  # [ax, ay, az]
        
        # Gravity
        self.gravity = np.array([0, 0, -9.81])
    
    def update(self, target_position, dt):
        """
        Update the drone's state based on a target position.
        
        Parameters:
        -----------
        target_position : array-like
            Target position [x, y, z] for the drone to move toward.
        dt : float
            Time step in seconds for the simulation.
            
        Returns:
        --------
        tuple
            Updated position, velocity, and acceleration vectors.
        """
        # Simple PD controller to calculate desired acceleration
        position_error = np.array(target_position) - self.position
        
        # Simplified PD gains
        kp = 2.0  # Proportional gain
        kd = 1.0  # Derivative gain
        
        # Calculate desired acceleration using PD control
        desired_acceleration = kp * position_error - kd * self.velocity
        
        # Add gravity compensation
        desired_acceleration -= self.gravity
        
        # Apply thrust limits
        thrust_magnitude = np.linalg.norm(desired_acceleration)
        max_acceleration = self.max_thrust / self.mass
        
        if thrust_magnitude > max_acceleration:
            desired_acceleration = desired_acceleration * (max_acceleration / thrust_magnitude)
        
        # Apply drag force
        drag = -self.drag_coefficient * self.velocity * np.linalg.norm(self.velocity)
        drag_acceleration = drag / self.mass
        
        # Calculate final acceleration
        self.acceleration = desired_acceleration + drag_acceleration + self.gravity
        
        # Update velocity and position using Euler integration
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        
        return self.position, self.velocity, self.acceleration
    
    def follow_trajectory(self, trajectory, dt, lookahead_distance=1.0):
        """
        Simulate the drone following a trajectory.
        
        Parameters:
        -----------
        trajectory : Trajectory
            Trajectory object defining the path to follow.
        dt : float
            Time step in seconds for the simulation.
        lookahead_distance : float
            Distance ahead of current position to aim for. Default is 1.0.
            
        Returns:
        --------
        tuple
            Lists of positions, velocities, accelerations, and target points over time.
        """
        if trajectory.num_points == 0:
            return [], [], [], []
            
        positions = [self.position.copy()]
        velocities = [self.velocity.copy()]
        accelerations = [self.acceleration.copy()]
        targets = []
        
        # Continue until we're close to the final waypoint
        final_waypoint = trajectory.get_point_at_index(trajectory.num_points - 1)
        final_position = np.array([final_waypoint.x, final_waypoint.y, final_waypoint.z])
        
        max_distance_to_target = lookahead_distance * 0.5
        simulation_time = 0.0
        
        while np.linalg.norm(self.position - final_position) > max_distance_to_target:
            # Get target point ahead on trajectory
            target_point = trajectory.get_lookahead_point(
                self.position, lookahead_distance
            )
            target_position = np.array([target_point.x, target_point.y, target_point.z])
            targets.append(target_position.copy())
            
            # Update drone state
            self.update(target_position, dt)
            
            # Store state
            positions.append(self.position.copy())
            velocities.append(self.velocity.copy())
            accelerations.append(self.acceleration.copy())
            
            # Update simulation time and check for timeout
            simulation_time += dt
            if simulation_time > 60.0:  # 1 minute timeout
                break
                
        return positions, velocities, accelerations, targets