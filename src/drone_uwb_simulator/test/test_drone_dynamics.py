import unittest
import numpy as np
from drone_uwb_simulator.drone_dynamics import (
    DroneDynamics, Trajectory, Waypoint
)

class TestDroneDynamics(unittest.TestCase):
    """Test cases for the DroneDynamics class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        # Create a simple trajectory for testing
        self.waypoints = [
            Waypoint(0.0, 0.0, 0.0),
            Waypoint(5.0, 0.0, 0.0),
            Waypoint(5.0, 5.0, 0.0),
            Waypoint(0.0, 5.0, 0.0)
        ]
        
        self.trajectory = Trajectory(speed=2.0, dt=0.1)
        self.trajectory.construct_trajectory(self.waypoints, method='linear')
    
    def test_initialization(self):
        """Test initialization of DroneDynamics objects."""
        # Test with default values
        dynamics = DroneDynamics()
        self.assertEqual(dynamics.mass, 1.0)
        self.assertEqual(dynamics.max_thrust, 15.0)
        self.assertEqual(dynamics.drag_coefficient, 0.1)
        
        # Verify initial state
        np.testing.assert_array_equal(dynamics.position, np.zeros(3))
        np.testing.assert_array_equal(dynamics.velocity, np.zeros(3))
        np.testing.assert_array_equal(dynamics.acceleration, np.zeros(3))
        np.testing.assert_array_equal(dynamics.gravity, np.array([0, 0, -9.81]))
        
        # Test with custom values
        mass = 2.0
        max_thrust = 20.0
        drag_coefficient = 0.2
        
        dynamics = DroneDynamics(
            mass=mass,
            max_thrust=max_thrust,
            drag_coefficient=drag_coefficient
        )
        
        self.assertEqual(dynamics.mass, mass)
        self.assertEqual(dynamics.max_thrust, max_thrust)
        self.assertEqual(dynamics.drag_coefficient, drag_coefficient)
        
        # Verify attributes are converted to float
        dynamics = DroneDynamics(mass=2, max_thrust=20, drag_coefficient=0.2)
        self.assertIsInstance(dynamics.mass, float)
        self.assertIsInstance(dynamics.max_thrust, float)
        self.assertIsInstance(dynamics.drag_coefficient, float)
    
    def test_set_controller_gains(self):
        """Test setting controller gains."""
        dynamics = DroneDynamics()
        
        # Initial gain values
        initial_kp = dynamics.kp
        initial_kd = dynamics.kd
        
        # Set new gains
        new_kp = 3.0
        new_kd = 1.5
        
        dynamics.set_controller_gains(new_kp, new_kd)
        
        self.assertEqual(dynamics.kp, new_kp)
        self.assertEqual(dynamics.kd, new_kd)
        
        # Verify gains are converted to float
        dynamics.set_controller_gains(4, 2)
        self.assertIsInstance(dynamics.kp, float)
        self.assertIsInstance(dynamics.kd, float)
    
    def test_update(self):
        """Test updating the drone state based on a target position."""
        dynamics = DroneDynamics()
        
        # Set initial state
        dynamics.position = np.array([0.0, 0.0, 0.0])
        dynamics.velocity = np.array([0.0, 0.0, 0.0])
        
        # Update toward a target position
        target_position = [5.0, 0.0, 0.0]  # 5 units ahead on x-axis
        dt = 0.1
        
        pos, vel, acc = dynamics.update(target_position, dt)
        
        # Verify state changes
        self.assertIsInstance(pos, np.ndarray)
        self.assertIsInstance(vel, np.ndarray)
        self.assertIsInstance(acc, np.ndarray)
        
        # Position should move toward target (x should increase)
        self.assertGreater(pos[0], 0.0)
        
        # There should be positive x velocity
        self.assertGreater(vel[0], 0.0)
        
        # Verify position is updated internally
        np.testing.assert_array_equal(dynamics.position, pos)
        
        # Test with invalid target position shape
        with self.assertRaises(ValueError):
            dynamics.update([1, 2], dt)  # Missing z-coordinate
    
    def test_update_with_gravity(self):
        """Test that gravity affects vertical motion."""
        dynamics = DroneDynamics()
        
        # Set initial state at a height
        initial_height = 10.0
        dynamics.position = np.array([0.0, 0.0, initial_height])
        dynamics.velocity = np.array([0.0, 0.0, 0.0])
        
        # Update toward same x,y but at ground level
        target_position = [0.0, 0.0, 0.0]
        dt = 0.1
        
        # Single update
        pos, vel, acc = dynamics.update(target_position, dt)
        
        # Gravity should cause downward acceleration and velocity
        self.assertLess(acc[2], 0.0)  # Negative z acceleration (downward)
        self.assertLess(vel[2], 0.0)  # Negative z velocity (downward)
        self.assertLess(pos[2], initial_height)  # Height should decrease
    
    def test_update_with_thrust_limit(self):
        """Test that thrust limits are respected."""
        # Create a drone with very low thrust limit
        dynamics = DroneDynamics(mass=1.0, max_thrust=5.0)
        
        # Set initial state
        dynamics.position = np.array([0.0, 0.0, 0.0])
        dynamics.velocity = np.array([0.0, 0.0, 0.0])
        
        # Update toward a distant target requiring high acceleration
        target_position = [100.0, 100.0, 100.0]
        dt = 0.1
        
        pos, vel, acc = dynamics.update(target_position, dt)
        
        # Calculate actual thrust magnitude (excluding gravity)
        thrust_acceleration = dynamics.acceleration - dynamics.gravity
        thrust_magnitude = np.linalg.norm(thrust_acceleration)
        
        # Verify thrust is limited
        self.assertLessEqual(thrust_magnitude, dynamics.max_thrust / dynamics.mass)
    
    def test_update_with_drag(self):
        """Test that drag affects motion at high speeds."""
        dynamics = DroneDynamics(drag_coefficient=0.5)  # High drag
        
        # Set initial state with high velocity
        dynamics.position = np.array([0.0, 0.0, 0.0])
        dynamics.velocity = np.array([10.0, 0.0, 0.0])  # Fast movement along x-axis
        
        # Update toward the same point (to isolate drag effect)
        target_position = [0.0, 0.0, 0.0]
        dt = 0.1
        
        pos, vel, acc = dynamics.update(target_position, dt)
        
        # Drag should cause deceleration in the x direction
        self.assertLess(vel[0], 10.0)  # Velocity should decrease
        self.assertLess(acc[0], 0.0)   # Negative x acceleration (deceleration)
    
    def test_follow_trajectory(self):
        """Test the drone following a trajectory."""
        dynamics = DroneDynamics()
        
        # Reset state to origin
        dynamics.reset_state()
        
        # Save the current position (should be zeros after reset)
        original_position = dynamics.position.copy()
        
        # Follow the trajectory with default parameters
        result = dynamics.follow_trajectory(self.trajectory)
        
        # Verify result structure
        self.assertIsInstance(result, dict)
        self.assertIn('positions', result)
        self.assertIn('velocities', result)
        self.assertIn('accelerations', result)
        self.assertIn('targets', result)
        
        # There should be multiple positions recorded
        self.assertGreater(len(result['positions']), 1)
        
        # The first position should match the drone's position before the trajectory following
        # We use almost_equal instead of exactly equal to account for potential floating-point differences
        np.testing.assert_array_almost_equal(result['positions'][0], original_position)
        
        # Test with an empty trajectory
        empty_trajectory = Trajectory()
        
        # Reset the drone state again
        dynamics.reset_state()
        new_original_position = dynamics.position.copy()
        
        result = dynamics.follow_trajectory(empty_trajectory)
        
        # Should still return a valid result dict with initial state
        self.assertEqual(len(result['positions']), 1)
        np.testing.assert_array_almost_equal(result['positions'][0], new_original_position)
    
    def test_follow_trajectory_target_reached(self):
        """Test that the drone can reach the target position."""
        # Create a simple short trajectory
        waypoints = [
            Waypoint(0.0, 0.0, 0.0),
            Waypoint(1.0, 0.0, 0.0)
        ]
        
        trajectory = Trajectory(speed=1.0, dt=0.1)
        trajectory.construct_trajectory(waypoints, method='linear')
        
        # Set high gains for faster response
        dynamics = DroneDynamics()
        dynamics.set_controller_gains(10.0, 5.0)
        
        # Reset state to origin
        dynamics.reset_state()
        
        # Follow the trajectory with a generous timeout
        result = dynamics.follow_trajectory(
            trajectory,
            dt=0.01,
            timeout_seconds=10.0,
            position_threshold=0.1  # Consider target reached within 0.1 units
        )
        
        # Verify the target was reached
        self.assertIn('target_reached', result)
        self.assertTrue(result['target_reached'])
        
        # Final position should be close to the target
        final_position = result['positions'][-1]
        target_position = waypoints[-1].get_coordinates()
        
        distance_to_target = np.linalg.norm(final_position - target_position)
        self.assertLessEqual(distance_to_target, 0.1)
    
    def test_reset_state(self):
        """Test resetting the drone state."""
        dynamics = DroneDynamics()
        
        # Set some non-zero state
        dynamics.position = np.array([5.0, 5.0, 5.0])
        dynamics.velocity = np.array([1.0, 1.0, 1.0])
        dynamics.acceleration = np.array([0.5, 0.5, 0.5])
        
        # Reset to default state
        dynamics.reset_state()
        
        np.testing.assert_array_equal(dynamics.position, np.zeros(3))
        np.testing.assert_array_equal(dynamics.velocity, np.zeros(3))
        np.testing.assert_array_equal(dynamics.acceleration, np.zeros(3))
        
        # Reset to custom state
        custom_position = [10.0, 10.0, 10.0]
        custom_velocity = [2.0, 2.0, 2.0]
        custom_acceleration = [1.0, 1.0, 1.0]
        
        dynamics.reset_state(custom_position, custom_velocity, custom_acceleration)
        
        np.testing.assert_array_equal(dynamics.position, np.array(custom_position))
        np.testing.assert_array_equal(dynamics.velocity, np.array(custom_velocity))
        np.testing.assert_array_equal(dynamics.acceleration, np.array(custom_acceleration))


if __name__ == '__main__':
    unittest.main()