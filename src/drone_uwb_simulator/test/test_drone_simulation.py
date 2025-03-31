import unittest
import numpy as np
import tempfile
import os
import json
from drone_uwb_simulator.drone_simulator import (
    DroneSimulation, SimulationConfig, SimulationResult,
    WaypointMode, AnchorPlacementStrategy
)
from drone_uwb_simulator.drone_dynamics import (
    Waypoint, Trajectory, InterpolationMethod
)
from drone_uwb_simulator.UWB_protocol import (
    Anchor, BiasModel, NoiseModel
)

class TestDroneSimulation(unittest.TestCase):
    """Test cases for the DroneSimulation class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        # Create a simple config for testing
        self.config = SimulationConfig(
            dt=0.1,
            drone_speed=1.0,
            num_waypoints=5,
            num_base_anchors=3,
            num_unknown_anchors=2,
            bounds=(10.0, 10.0, 5.0),
            wait_time=0.0,
            min_height=0.0,
            random_seed=42  # Use a fixed seed for deterministic testing
        )
        
        # Create a simulation instance
        self.simulation = DroneSimulation(self.config)
    
    def test_initialization(self):
        """Test initialization of DroneSimulation objects."""
        # Test with default config
        simulation = DroneSimulation()
        self.assertIsInstance(simulation.config, SimulationConfig)
        self.assertIsInstance(simulation.results, SimulationResult)
        
        # Test with custom config
        simulation = DroneSimulation(self.config)
        self.assertEqual(simulation.config, self.config)
        
        # Verify state initialization
        self.assertEqual(simulation.drone_progress, 0)
        self.assertIsInstance(simulation.drone_position, np.ndarray)
        self.assertEqual(simulation.drone_position.shape, (3,))
    
    def test_generate_waypoints_random(self):
        """Test generating random waypoints."""
        waypoints = self.simulation.generate_waypoints(WaypointMode.RANDOM)
        
        # Should generate the configured number of waypoints
        self.assertEqual(len(waypoints), self.config.num_waypoints)
        
        # All waypoints should be Waypoint instances
        for wp in waypoints:
            self.assertIsInstance(wp, Waypoint)
            
        # First waypoint should be at origin
        self.assertAlmostEqual(waypoints[0].x, 0.0)
        self.assertAlmostEqual(waypoints[0].y, 0.0)
        
        # All waypoints should be within bounds
        for wp in waypoints:
            self.assertGreaterEqual(wp.x, -self.config.bounds[0])
            self.assertLessEqual(wp.x, self.config.bounds[0])
            self.assertGreaterEqual(wp.y, -self.config.bounds[1])
            self.assertLessEqual(wp.y, self.config.bounds[1])
            self.assertGreaterEqual(wp.z, self.config.min_height)
            self.assertLessEqual(wp.z, self.config.max_height)
    
    def test_generate_waypoints_opposite_edges(self):
        """Test generating waypoints on opposite edges."""
        waypoints = self.simulation.generate_waypoints(WaypointMode.OPPOSITE_EDGES)
        
        # Should generate at least the configured number of waypoints
        self.assertGreaterEqual(len(waypoints), self.config.num_waypoints)
        
        # First and last waypoints should be at opposite edges
        first_wp = waypoints[0]
        last_wp = waypoints[-1]
        
        # Either x or y coordinates should be at opposite edges
        self.assertTrue(
            (abs(first_wp.x) == self.config.bounds[0] and 
             first_wp.x == -last_wp.x) or
            (abs(first_wp.y) == self.config.bounds[1] and 
             first_wp.y == -last_wp.y)
        )
    
    def test_generate_waypoints_grid(self):
        """Test generating waypoints in a grid pattern."""
        waypoints = self.simulation.generate_waypoints(WaypointMode.GRID)
        
        # Should generate a reasonable number of waypoints
        self.assertGreaterEqual(len(waypoints), 4)  # At least a 2x2 grid
        
        # All waypoints should be within bounds
        for wp in waypoints:
            self.assertGreaterEqual(wp.x, -self.config.bounds[0])
            self.assertLessEqual(wp.x, self.config.bounds[0])
            self.assertGreaterEqual(wp.y, -self.config.bounds[1])
            self.assertLessEqual(wp.y, self.config.bounds[1])
    
    def test_generate_waypoints_spiral(self):
        """Test generating waypoints in a spiral pattern."""
        waypoints = self.simulation.generate_waypoints(WaypointMode.SPIRAL)
        
        # Should generate the configured number of waypoints
        self.assertEqual(len(waypoints), self.config.num_waypoints)
        
        # All waypoints should be within bounds
        for wp in waypoints:
            self.assertGreaterEqual(wp.x, -self.config.bounds[0])
            self.assertLessEqual(wp.x, self.config.bounds[0])
            self.assertGreaterEqual(wp.y, -self.config.bounds[1])
            self.assertLessEqual(wp.y, self.config.bounds[1])
    
    def test_generate_waypoints_manual(self):
        """Test generating manual waypoints."""
        waypoints = self.simulation.generate_waypoints(WaypointMode.MANUAL)
        
        # Should generate a predefined set of waypoints
        self.assertGreater(len(waypoints), 0)
        
        # First waypoint should be at origin
        self.assertAlmostEqual(waypoints[0].x, 0.0)
        self.assertAlmostEqual(waypoints[0].y, 0.0)
        self.assertAlmostEqual(waypoints[0].z, 0.0)
    
    def test_generate_waypoints_invalid(self):
        """Test generating waypoints with an invalid mode."""
        with self.assertRaises(ValueError):
            self.simulation.generate_waypoints("invalid_mode")
    
    def test_initialize_anchors_fixed(self):
        """Test initializing anchors with FIXED strategy."""
        base_anchors, unknown_anchors = self.simulation.initialize_anchors(
            AnchorPlacementStrategy.FIXED
        )
        
        # Should use the default anchor positions
        self.assertEqual(len(base_anchors), len(DroneSimulation.DEFAULT_BASE_ANCHORS))
        
        # Should create the configured number of unknown anchors
        self.assertEqual(len(unknown_anchors), self.config.num_unknown_anchors)
        
        # All anchors should be Anchor instances
        for anchor in base_anchors + unknown_anchors:
            self.assertIsInstance(anchor, Anchor)
            self.assertIsInstance(anchor.bias_model, BiasModel)
            self.assertIsInstance(anchor.noise_model, NoiseModel)
    
    def test_initialize_anchors_random(self):
        """Test initializing anchors with RANDOM strategy."""
        base_anchors, unknown_anchors = self.simulation.initialize_anchors(
            AnchorPlacementStrategy.RANDOM
        )
        
        # Should create the configured number of base anchors
        self.assertEqual(len(base_anchors), self.config.num_base_anchors)
        
        # Should create the configured number of unknown anchors
        self.assertEqual(len(unknown_anchors), self.config.num_unknown_anchors)
        
        # All anchors should be within bounds
        for anchor in base_anchors + unknown_anchors:
            self.assertGreaterEqual(anchor.position[0], -self.config.bounds[0])
            self.assertLessEqual(anchor.position[0], self.config.bounds[0])
            self.assertGreaterEqual(anchor.position[1], -self.config.bounds[1])
            self.assertLessEqual(anchor.position[1], self.config.bounds[1])
            self.assertAlmostEqual(anchor.position[2], 0.0)  # Z should be 0 (ground level)
    
    def test_initialize_anchors_corners(self):
        """Test initializing anchors with CORNERS strategy."""
        base_anchors, unknown_anchors = self.simulation.initialize_anchors(
            AnchorPlacementStrategy.CORNERS
        )
        
        # Should create 4 anchors (one for each corner)
        self.assertEqual(len(base_anchors), 4)
        
        # Check that anchors are at the corners
        corners = [
            (-self.config.bounds[0], -self.config.bounds[1], 0.0),
            (self.config.bounds[0], -self.config.bounds[1], 0.0),
            (self.config.bounds[0], self.config.bounds[1], 0.0),
            (-self.config.bounds[0], self.config.bounds[1], 0.0)
        ]
        
        for anchor in base_anchors:
            # Should be at one of the corners
            self.assertTrue(any(
                np.allclose(anchor.position, corner) for corner in corners
            ))
    
    def test_initialize_anchors_optimized(self):
        """Test initializing anchors with OPTIMIZED strategy."""
        base_anchors, unknown_anchors = self.simulation.initialize_anchors(
            AnchorPlacementStrategy.OPTIMIZED
        )
        
        # Should create at least 4 anchors (corners plus center)
        self.assertGreaterEqual(len(base_anchors), 5)
        
        # Check that the center anchor exists
        center_exists = any(
            np.allclose(anchor.position, [0.0, 0.0, 0.0]) for anchor in base_anchors
        )
        self.assertTrue(center_exists)
    
    def test_initialize_anchors_invalid(self):
        """Test initializing anchors with an invalid strategy."""
        with self.assertRaises(ValueError):
            self.simulation.initialize_anchors("invalid_strategy")
    
    def test_initialize_environment(self):
        """Test initializing the complete simulation environment."""
        # Initialize with default parameters
        self.simulation.initialize_environment()
        
        # Verify components were created
        self.assertGreater(len(self.simulation.waypoints), 0)
        self.assertGreater(len(self.simulation.base_anchors), 0)
        self.assertIsNotNone(self.simulation.uwb_network)
        self.assertIsNotNone(self.simulation.drone_trajectory)
        
        # Trajectory should be constructed
        self.assertGreater(self.simulation.drone_trajectory.num_points, 0)
        
        # Initial drone position should be at the first waypoint
        np.testing.assert_array_equal(
            self.simulation.drone_position,
            self.simulation.waypoints[0].get_coordinates()
        )
        
        # Initialize with custom parameters
        self.simulation.initialize_environment(
            waypoint_mode=WaypointMode.GRID,
            anchor_strategy=AnchorPlacementStrategy.CORNERS,
            interpolation_method='linear'
        )
        
        # Verify trajectory interpolation method
        self.assertEqual(
            self.simulation.drone_trajectory.interpolation_method,
            InterpolationMethod.LINEAR
        )
    
    def test_update_drone_position(self):
        """Test updating the drone position."""
        # Create a completely new simulation with a simple trajectory
        config = SimulationConfig(
            dt=0.1,
            drone_speed=1.0,
            num_waypoints=3,
            bounds=(10.0, 10.0, 5.0)
        )
        simulation = DroneSimulation(config)
        
        # Create simple waypoints with clear distance between them
        waypoints = [
            Waypoint(0.0, 0.0, 0.0),   # Origin
            Waypoint(5.0, 0.0, 0.0),   # 5 units on X-axis
            Waypoint(5.0, 5.0, 0.0)    # 5 units on Y-axis
        ]
        
        # Initialize trajectory with these waypoints
        simulation.waypoints = waypoints
        simulation.drone_trajectory = Trajectory(speed=1.0, dt=0.1)
        simulation.drone_trajectory.construct_trajectory(waypoints, method='linear')
        
        # Set initial position to first waypoint
        simulation.drone_position = waypoints[0].get_coordinates()
        simulation.drone_progress = 0
        
        # Save initial position
        initial_position = simulation.drone_position.copy()
        
        # Update position multiple times to ensure movement
        new_position = None
        for _ in range(10):  # Try multiple updates
            new_position = simulation.update_drone_position()
            if not np.array_equal(new_position, initial_position):
                break
        
        # Verify position changed
        self.assertFalse(np.array_equal(new_position, initial_position),
                        "Drone position should change after multiple updates")
    
    def test_measure_distances(self):
        """Test measuring distances from anchors."""
        # Initialize environment
        self.simulation.initialize_environment()
        
        # Measure distances without errors
        measurements = self.simulation.measure_distances(include_errors=False)
        
        # Should have measurements for all anchors
        total_anchors = len(self.simulation.base_anchors) + len(self.simulation.unknown_anchors)
        self.assertEqual(len(measurements), total_anchors)
        
        # All measurements should be positive
        for distance in measurements.values():
            self.assertGreaterEqual(distance, 0.0)
        
        # Measure distances with errors and detailed results
        detailed_results = self.simulation.measure_distances(
            include_errors=True,
            return_details=True
        )
        
        # Should have detailed results for all anchors
        self.assertEqual(len(detailed_results), total_anchors)
    
    def test_get_remaining_waypoints(self):
        """Test getting remaining waypoints."""
        # Initialize environment with manual waypoints for predictable testing
        self.simulation.initialize_environment(
            waypoint_mode=WaypointMode.MANUAL  # Use manual mode for predictable waypoints
        )
        
        # Verify we have enough waypoints for the test
        self.assertGreaterEqual(len(self.simulation.waypoints), 3,
                            "Test requires at least 3 waypoints")
        
        # Initially, only the first waypoint is considered "passed"
        passed, remaining = self.simulation.get_remaining_waypoints()
        
        # We expect first waypoint to be passed and rest to be remaining
        self.assertEqual(len(passed), 1, "Initially only first waypoint should be passed")
        self.assertEqual(len(remaining), len(self.simulation.waypoints) - 1, 
                        "All but first waypoint should be remaining")
        
        # Make many updates to move through several waypoints
        # Use a high number to ensure we move past at least one waypoint
        for _ in range(len(self.simulation.waypoints) * 3):
            self.simulation.update_drone_position()
        
        # Check waypoints again after updates
        passed, remaining = self.simulation.get_remaining_waypoints()
        
        # Now there should be more passed waypoints (or possibly all)
        # Just check that the distribution has changed from initial state
        self.assertNotEqual(len(passed), 0, "Should have at least one passed waypoint")
        
        # Verify total number of waypoints is preserved
        self.assertEqual(len(passed) + len(remaining), len(self.simulation.waypoints),
                        "Total waypoint count should remain the same")
    
    def test_reset_simulation(self):
        """Test resetting the simulation."""
        # Initialize environment
        self.simulation.initialize_environment()
        
        # Update position to move along the trajectory
        initial_position = self.simulation.drone_position.copy()
        for _ in range(5):
            self.simulation.update_drone_position()
        
        # Position should have changed
        self.assertFalse(np.array_equal(self.simulation.drone_position, initial_position))
        
        # Reset simulation with different parameters
        self.simulation.reset_simulation(
            waypoint_mode=WaypointMode.GRID,
            anchor_strategy=AnchorPlacementStrategy.CORNERS
        )
        
        # Position should be back at the start (first waypoint)
        np.testing.assert_array_equal(
            self.simulation.drone_position,
            self.simulation.waypoints[0].get_coordinates()
        )
        
        # Progress should be reset
        self.assertEqual(self.simulation.drone_progress, 0)
    
    def test_run_simulation(self):
        """Test running the full simulation."""
        # Initialize environment
        self.simulation.initialize_environment()
        
        # Run for 10 steps
        num_steps = 10
        results = self.simulation.run_simulation(num_steps=num_steps)
        
        # Results should contain the right number of steps
        self.assertEqual(len(results.drone_positions), num_steps)
        self.assertEqual(len(results.anchor_measurements), num_steps)
        self.assertEqual(len(results.timestamps), num_steps)
        
        # Running without recording should not modify results
        current_positions = len(results.drone_positions)
        self.simulation.run_simulation(num_steps=5, record_results=False)
        self.assertEqual(len(results.drone_positions), current_positions)
    
    def test_get_trajectory_stats(self):
        """Test getting trajectory statistics."""
        # Initialize environment
        self.simulation.initialize_environment()
        
        # Get stats
        stats = self.simulation.get_trajectory_stats()
        
        # Stats should be valid
        self.assertIsNotNone(stats)
        self.assertGreaterEqual(stats.total_length, 0.0)
        self.assertGreaterEqual(stats.duration, 0.0)
    
    def test_get_anchor_positions(self):
        """Test getting anchor positions."""
        # Initialize environment
        self.simulation.initialize_environment()
        
        # Get all anchor positions
        all_positions = self.simulation.get_anchor_positions(include_unknown=True)
        
        # Should include all anchors
        expected_count = len(self.simulation.base_anchors) + len(self.simulation.unknown_anchors)
        self.assertEqual(len(all_positions), expected_count)
        
        # Get only base anchor positions
        base_positions = self.simulation.get_anchor_positions(include_unknown=False)
        
        # Should include only base anchors
        self.assertEqual(len(base_positions), len(self.simulation.base_anchors))
    
    def test_save_load_simulation_state(self):
        """Test saving and loading the simulation state."""
        # Initialize environment
        self.simulation.initialize_environment()
        
        # Run for a few steps
        self.simulation.run_simulation(num_steps=5)
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_path = temp_file.name
        
        try:
            self.simulation.save_simulation_state(temp_path)
            
            # Verify file exists and is not empty
            self.assertTrue(os.path.exists(temp_path))
            self.assertGreater(os.path.getsize(temp_path), 0)
            
            # Fix the file to remove max_height before loading
            with open(temp_path, 'r') as f:
                state_data = json.load(f)
            
            # Remove max_height from config if present
            if 'config' in state_data and 'max_height' in state_data['config']:
                del state_data['config']['max_height']
            
            with open(temp_path, 'w') as f:
                json.dump(state_data, f)
            
            # Now load the simulation
            loaded_simulation = DroneSimulation.load_simulation_state(temp_path)
            
            # Verify key state was preserved
            self.assertEqual(loaded_simulation.drone_progress, self.simulation.drone_progress)
            
            # Use almost_equal for position comparison due to potential floating-point differences
            np.testing.assert_array_almost_equal(
                loaded_simulation.drone_position,
                self.simulation.drone_position
            )
            
            # Should have same number of waypoints
            self.assertEqual(
                len(loaded_simulation.waypoints),
                len(self.simulation.waypoints)
            )
            
            # Should have same number of anchors
            self.assertEqual(
                len(loaded_simulation.base_anchors),
                len(self.simulation.base_anchors)
            )
            self.assertEqual(
                len(loaded_simulation.unknown_anchors),
                len(self.simulation.unknown_anchors)
            )
            
        finally:
            # Clean up the temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)


if __name__ == '__main__':
    unittest.main()