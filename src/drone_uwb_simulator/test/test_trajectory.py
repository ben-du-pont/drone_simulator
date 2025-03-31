import unittest
import numpy as np
from drone_uwb_simulator.drone_dynamics import (
    Trajectory, Waypoint, InterpolationMethod, Point3D
)

class TestTrajectory(unittest.TestCase):
    """Test cases for the Trajectory class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        # Create a simple set of waypoints for testing
        self.waypoints = [
            Waypoint(0.0, 0.0, 0.0),
            Waypoint(1.0, 0.0, 0.0),
            Waypoint(1.0, 1.0, 0.0),
            Waypoint(0.0, 1.0, 0.0)
        ]
        
        # Standard trajectory parameters
        self.speed = 1.0  # 1.0 units per second
        self.dt = 0.1     # 0.1 seconds per step
    
    def test_initialization(self):
        """Test initialization of Trajectory objects."""
        # Test with default values
        trajectory = Trajectory()
        self.assertEqual(trajectory.speed, 3.0)
        self.assertEqual(trajectory.dt, 0.05)
        self.assertEqual(trajectory.wait_time, 0.0)
        self.assertEqual(trajectory.num_points, 0)
        
        # Test with custom values
        speed = 2.0
        dt = 0.2
        wait_time = 1.0
        trajectory = Trajectory(speed=speed, dt=dt, wait_time=wait_time)
        
        self.assertEqual(trajectory.speed, speed)
        self.assertEqual(trajectory.dt, dt)
        self.assertEqual(trajectory.wait_time, wait_time)
        self.assertEqual(trajectory.num_points, 0)
        
        # Verify attributes are converted to float
        trajectory = Trajectory(speed=2, dt=0.2, wait_time=1)
        self.assertIsInstance(trajectory.speed, float)
        self.assertIsInstance(trajectory.dt, float)
        self.assertIsInstance(trajectory.wait_time, float)
    
    def test_construct_trajectory_linear(self):
        """Test constructing a linear trajectory."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        
        # Construct a linear trajectory
        result = trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Verify construction was successful
        self.assertTrue(result)
        self.assertEqual(trajectory.interpolation_method, InterpolationMethod.LINEAR)
        self.assertGreater(trajectory.num_points, 0)
        
        # Check if waypoints are stored correctly
        self.assertEqual(len(trajectory.waypoints), len(self.waypoints))
        
        # Check that first and last points match the first and last waypoints
        first_point = trajectory.get_point_at_index(0)
        last_point = trajectory.get_point_at_index(trajectory.num_points - 1)
        
        self.assertAlmostEqual(first_point.x, self.waypoints[0].x)
        self.assertAlmostEqual(first_point.y, self.waypoints[0].y)
        self.assertAlmostEqual(first_point.z, self.waypoints[0].z)
        
        self.assertAlmostEqual(last_point.x, self.waypoints[-1].x)
        self.assertAlmostEqual(last_point.y, self.waypoints[-1].y)
        self.assertAlmostEqual(last_point.z, self.waypoints[-1].z)
    
    def test_construct_trajectory_spline(self):
        """Test constructing a spline trajectory."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        
        # Construct a spline trajectory
        result = trajectory.construct_trajectory(self.waypoints, method='spline')
        
        # Verify construction was successful
        self.assertTrue(result)
        self.assertEqual(trajectory.interpolation_method, InterpolationMethod.SPLINE)
        self.assertGreater(trajectory.num_points, 0)
        
        # Check that first and last points match the first and last waypoints
        first_point = trajectory.get_point_at_index(0)
        last_point = trajectory.get_point_at_index(trajectory.num_points - 1)
        
        self.assertAlmostEqual(first_point.x, self.waypoints[0].x)
        self.assertAlmostEqual(first_point.y, self.waypoints[0].y)
        self.assertAlmostEqual(first_point.z, self.waypoints[0].z)
        
        self.assertAlmostEqual(last_point.x, self.waypoints[-1].x)
        self.assertAlmostEqual(last_point.y, self.waypoints[-1].y)
        self.assertAlmostEqual(last_point.z, self.waypoints[-1].z)
    
    def test_construct_trajectory_empty_waypoints(self):
        """Test constructing a trajectory with empty waypoints."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        
        # Construct with empty waypoints
        result = trajectory.construct_trajectory([], method='linear')
        
        # Construction should fail
        self.assertFalse(result)
        self.assertEqual(trajectory.num_points, 0)
    
    def test_construct_trajectory_single_waypoint(self):
        """Test constructing a trajectory with a single waypoint."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        
        # Construct with a single waypoint
        result = trajectory.construct_trajectory([Waypoint(0, 0, 0)], method='linear')
        
        # Construction should fail
        self.assertFalse(result)
        self.assertEqual(trajectory.num_points, 0)
    
    def test_construct_trajectory_enum_method(self):
        """Test constructing a trajectory using enum method parameter."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        
        # Construct using enum value
        result = trajectory.construct_trajectory(
            self.waypoints, 
            method=InterpolationMethod.LINEAR
        )
        
        # Verify construction was successful
        self.assertTrue(result)
        self.assertEqual(trajectory.interpolation_method, InterpolationMethod.LINEAR)
    
    def test_construct_trajectory_invalid_method(self):
        """Test constructing a trajectory with an invalid method."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        
        # This should raise a ValueError
        with self.assertRaises(ValueError):
            trajectory.construct_trajectory(self.waypoints, method='invalid_method')
    
    def test_get_point_at_index(self):
        """Test getting a point at a specific index."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Get a point in the middle of the trajectory
        middle_index = trajectory.num_points // 2
        point = trajectory.get_point_at_index(middle_index)
        
        self.assertIsInstance(point, Waypoint)
        
        # Invalid index should return None
        self.assertIsNone(trajectory.get_point_at_index(-1))
        self.assertIsNone(trajectory.get_point_at_index(trajectory.num_points))
    
    def test_get_all_points(self):
        """Test getting all trajectory points."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Get all points
        x_points, y_points, z_points = trajectory.get_all_points()
        
        self.assertEqual(len(x_points), trajectory.num_points)
        self.assertEqual(len(y_points), trajectory.num_points)
        self.assertEqual(len(z_points), trajectory.num_points)
        
        # First and last points should match waypoints
        self.assertAlmostEqual(x_points[0], self.waypoints[0].x)
        self.assertAlmostEqual(y_points[0], self.waypoints[0].y)
        self.assertAlmostEqual(z_points[0], self.waypoints[0].z)
        
        self.assertAlmostEqual(x_points[-1], self.waypoints[-1].x)
        self.assertAlmostEqual(y_points[-1], self.waypoints[-1].y)
        self.assertAlmostEqual(z_points[-1], self.waypoints[-1].z)
    
    def test_get_points_as_array(self):
        """Test getting all trajectory points as a Nx3 array."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Get points as array
        points_array = trajectory.get_points_as_array()
        
        self.assertIsInstance(points_array, np.ndarray)
        self.assertEqual(points_array.shape, (trajectory.num_points, 3))
        
        # First and last points should match waypoints
        np.testing.assert_almost_equal(
            points_array[0], 
            np.array([self.waypoints[0].x, self.waypoints[0].y, self.waypoints[0].z])
        )
        np.testing.assert_almost_equal(
            points_array[-1], 
            np.array([self.waypoints[-1].x, self.waypoints[-1].y, self.waypoints[-1].z])
        )
    
    def test_find_closest_point_index(self):
        """Test finding the index of the closest point to a position."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Position exactly at a waypoint
        position = [0.0, 0.0, 0.0]  # First waypoint
        index = trajectory.find_closest_point_index(position)
        self.assertEqual(index, 0)
        
        # Position near a point in the trajectory
        # This is implementation-dependent, so just check if we get a valid index
        position = [0.5, 0.5, 0.0]  # Somewhere in the middle
        index = trajectory.find_closest_point_index(position)
        self.assertGreaterEqual(index, 0)
        self.assertLess(index, trajectory.num_points)
        
        # Test with empty trajectory
        empty_trajectory = Trajectory()
        index = empty_trajectory.find_closest_point_index(position)
        self.assertEqual(index, -1)
        
        # Test with invalid position shape
        with self.assertRaises(ValueError):
            trajectory.find_closest_point_index([1, 2])  # Missing z-coordinate
    
    def test_get_lookahead_point(self):
        """Test getting a lookahead point along the trajectory."""
        # Create a straight line trajectory for predictable testing
        waypoints = [
            Waypoint(0.0, 0.0, 0.0),
            Waypoint(10.0, 0.0, 0.0)  # Straight line along x-axis
        ]
        
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(waypoints, method='linear')
        
        # Test with position at the start
        current_position = [0.0, 0.0, 0.0]
        lookahead_distance = 2.0
        
        # Get lookahead point
        point = trajectory.get_lookahead_point(current_position, lookahead_distance)
        
        self.assertIsNotNone(point)
        self.assertAlmostEqual(point.x, 2.0)  # 2.0 units ahead on x-axis
        self.assertAlmostEqual(point.y, 0.0)
        self.assertAlmostEqual(point.z, 0.0)
        
        # Test with lookahead distance beyond the trajectory
        lookahead_distance = 15.0
        
        # With bounded=True (default), should return the last point
        point = trajectory.get_lookahead_point(current_position, lookahead_distance)
        self.assertIsNotNone(point)
        self.assertAlmostEqual(point.x, 10.0)  # Last waypoint
        
        # With bounded=False, should return None
        point = trajectory.get_lookahead_point(
            current_position, lookahead_distance, bounded=False
        )
        self.assertIsNone(point)
        
        # Test with empty trajectory
        empty_trajectory = Trajectory()
        point = empty_trajectory.get_lookahead_point(current_position, lookahead_distance)
        self.assertIsNone(point)
    
    def test_get_trajectory_stats(self):
        """Test getting trajectory statistics."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Get stats
        stats = trajectory.get_trajectory_stats()
        
        # Verify stat properties
        self.assertAlmostEqual(stats.expected_distance, self.speed * self.dt)
        self.assertGreaterEqual(stats.total_length, 0.0)
        self.assertGreaterEqual(stats.duration, 0.0)
        
        # Empty trajectory should have default stats
        empty_trajectory = Trajectory(speed=self.speed, dt=self.dt)
        stats = empty_trajectory.get_trajectory_stats()
        
        self.assertEqual(stats.total_length, 0.0)
        self.assertEqual(stats.duration, 0.0)
    
    def test_get_total_length(self):
        """Test getting the total length of the trajectory."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Get total length
        length = trajectory.get_total_length()
        
        # For our square waypoints, length should be 3.0 (perimeter of a 1x1 square)
        self.assertAlmostEqual(length, 3.0)
        
        # Empty trajectory should have zero length
        empty_trajectory = Trajectory()
        self.assertEqual(empty_trajectory.get_total_length(), 0.0)
    
    def test_get_expected_duration(self):
        """Test getting the expected duration to traverse the trajectory."""
        speed = 2.0  # 2 units per second
        trajectory = Trajectory(speed=speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        # Get expected duration
        duration = trajectory.get_expected_duration()
        
        # Duration should be total_length / speed
        expected_duration = trajectory.get_total_length() / speed
        self.assertAlmostEqual(duration, expected_duration)
    
    def test_len_and_bool(self):
        """Test len() and bool() operations."""
        # Empty trajectory
        trajectory = Trajectory()
        self.assertEqual(len(trajectory), 0)
        self.assertFalse(bool(trajectory))
        
        # Constructed trajectory
        trajectory.construct_trajectory(self.waypoints, method='linear')
        self.assertEqual(len(trajectory), trajectory.num_points)
        self.assertTrue(bool(trajectory))
    
    def test_repr(self):
        """Test string representation."""
        trajectory = Trajectory(speed=self.speed, dt=self.dt)
        trajectory.construct_trajectory(self.waypoints, method='linear')
        
        representation = repr(trajectory)
        
        # Verify the representation contains key information
        self.assertIn("Trajectory", representation)
        self.assertIn(str(trajectory.num_points), representation)
        self.assertIn(str(round(trajectory.get_total_length(), 2)), representation)
        self.assertIn(str(trajectory.speed), representation)


if __name__ == '__main__':
    unittest.main()