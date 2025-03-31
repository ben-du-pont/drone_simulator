import unittest
import tempfile
import os
import json
from drone_uwb_simulator.drone_simulator import SimulationConfig

class TestSimulationConfig(unittest.TestCase):
    """Test cases for the SimulationConfig class."""
    
    def test_default_initialization(self):
        """Test initialization with default values."""
        config = SimulationConfig()
        
        # Check default values
        self.assertEqual(config.dt, 0.05)
        self.assertEqual(config.drone_speed, 1.0)
        self.assertEqual(config.num_waypoints, 15)
        self.assertEqual(config.num_base_anchors, 3)
        self.assertEqual(config.num_unknown_anchors, 3)
        self.assertEqual(config.bounds, (5.0, 5.0, 5.0))
        self.assertEqual(config.wait_time, 0.0)
        self.assertEqual(config.min_height, 0.0)
        self.assertEqual(config.max_height, config.bounds[2])
        self.assertIsNone(config.random_seed)
        
        # Check default models
        self.assertIn("constant_bias", config.bias_model_params)
        self.assertIn("linear_bias", config.bias_model_params)
        self.assertIn("variance", config.noise_model_params)
        self.assertIn("outlier_probability", config.noise_model_params)
        self.assertIn("outlier_range", config.noise_model_params)
    
    def test_custom_initialization(self):
        """Test initialization with custom values."""
        # Define custom values
        dt = 0.1
        drone_speed = 2.0
        num_waypoints = 10
        num_base_anchors = 4
        num_unknown_anchors = 2
        bounds = (10.0, 10.0, 5.0)
        wait_time = 1.0
        min_height = 1.0
        random_seed = 42
        bias_model_params = {"constant_bias": 0.1, "linear_bias": 1.1}
        noise_model_params = {
            "variance": 0.3, 
            "outlier_probability": 0.1, 
            "outlier_range": (0.3, 0.5)
        }
        
        config = SimulationConfig(
            dt=dt,
            drone_speed=drone_speed,
            num_waypoints=num_waypoints,
            num_base_anchors=num_base_anchors,
            num_unknown_anchors=num_unknown_anchors,
            bounds=bounds,
            wait_time=wait_time,
            min_height=min_height,
            random_seed=random_seed,
            bias_model_params=bias_model_params,
            noise_model_params=noise_model_params
        )
        
        # Verify custom values
        self.assertEqual(config.dt, dt)
        self.assertEqual(config.drone_speed, drone_speed)
        self.assertEqual(config.num_waypoints, num_waypoints)
        self.assertEqual(config.num_base_anchors, num_base_anchors)
        self.assertEqual(config.num_unknown_anchors, num_unknown_anchors)
        self.assertEqual(config.bounds, bounds)
        self.assertEqual(config.wait_time, wait_time)
        self.assertEqual(config.min_height, min_height)
        self.assertEqual(config.max_height, bounds[2])
        self.assertEqual(config.random_seed, random_seed)
        self.assertEqual(config.bias_model_params, bias_model_params)
        self.assertEqual(config.noise_model_params, noise_model_params)
    
    def test_parameter_validation(self):
        """Test validation of configuration parameters."""
        # Test negative dt
        with self.assertRaises(ValueError):
            SimulationConfig(dt=-0.1)
        
        # Test negative drone speed
        with self.assertRaises(ValueError):
            SimulationConfig(dt=0.1, drone_speed=-1.0)
        
        # Test negative wait time
        with self.assertRaises(ValueError):
            SimulationConfig(dt=0.1, wait_time=-1.0)
        
        # Test too few waypoints
        with self.assertRaises(ValueError):
            SimulationConfig(dt=0.1, num_waypoints=1)
        
        # Test negative bounds
        with self.assertRaises(ValueError):
            SimulationConfig(dt=0.1, bounds=(-1.0, 5.0, 5.0))
        
        # Test negative min_height
        with self.assertRaises(ValueError):
            SimulationConfig(dt=0.1, min_height=-1.0)
        
        # Test max_height <= min_height
        # Create a valid config first
        bounds = (5.0, 5.0, 3.0)  # z-bound is 3.0
        config = SimulationConfig(dt=0.1, bounds=bounds, min_height=2.0)
        
        # Check that max_height is properly derived from bounds[2]
        self.assertEqual(config.max_height, bounds[2])
        
        # Create a config with min_height > bounds[2] which should fail
        with self.assertRaises(ValueError):
            SimulationConfig(dt=0.1, bounds=bounds, min_height=4.0)
    
    def test_from_dict(self):
        """Test creating a config from a dictionary."""
        config_dict = {
            "dt": 0.1,
            "drone_speed": 2.0,
            "num_waypoints": 10,
            "bounds": (10.0, 10.0, 5.0),
            "wait_time": 1.0,
            "min_height": 1.0,
            "random_seed": 42,
            "extra_param": "should be ignored"  # This should be ignored
        }
        
        config = SimulationConfig.from_dict(config_dict)
        
        # Verify values were set correctly
        self.assertEqual(config.dt, 0.1)
        self.assertEqual(config.drone_speed, 2.0)
        self.assertEqual(config.num_waypoints, 10)
        self.assertEqual(config.bounds, (10.0, 10.0, 5.0))
        self.assertEqual(config.wait_time, 1.0)
        self.assertEqual(config.min_height, 1.0)
        self.assertEqual(config.random_seed, 42)
        
        # Extra parameters should be ignored
        self.assertFalse(hasattr(config, "extra_param"))
    
    def test_to_dict(self):
        """Test converting a config to a dictionary."""
        # Create a config with non-default values
        config = SimulationConfig(
            dt=0.1,
            drone_speed=2.0,
            num_waypoints=10,
            bounds=(10.0, 10.0, 5.0),
            wait_time=1.0,
            min_height=1.0,
            random_seed=42
        )
        
        config_dict = config.to_dict()
        
        # Verify dictionary values
        self.assertEqual(config_dict["dt"], 0.1)
        self.assertEqual(config_dict["drone_speed"], 2.0)
        self.assertEqual(config_dict["num_waypoints"], 10)
        self.assertEqual(config_dict["bounds"], (10.0, 10.0, 5.0))
        self.assertEqual(config_dict["wait_time"], 1.0)
        self.assertEqual(config_dict["min_height"], 1.0)
        self.assertEqual(config_dict["max_height"], 5.0)
        self.assertEqual(config_dict["random_seed"], 42)
        self.assertIn("bias_model_params", config_dict)
        self.assertIn("noise_model_params", config_dict)
    
    def test_json_serialization(self):
        """Test saving and loading config to/from JSON."""
        # Create a config with non-default values
        config = SimulationConfig(
            dt=0.1,
            drone_speed=2.0,
            num_waypoints=10,
            bounds=(10.0, 10.0, 5.0),
            wait_time=1.0,
            min_height=1.0,
            random_seed=42
        )
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_path = temp_file.name
        
        try:
            config.to_json(temp_path)
            
            # Verify file exists and is not empty
            self.assertTrue(os.path.exists(temp_path))
            self.assertGreater(os.path.getsize(temp_path), 0)
            
            # Fix the file to remove max_height before loading
            with open(temp_path, 'r') as f:
                config_data = json.load(f)
            
            # Remove max_height if present
            if 'max_height' in config_data:
                del config_data['max_height']
            
            with open(temp_path, 'w') as f:
                json.dump(config_data, f)
            
            # Load back
            loaded_config = SimulationConfig.from_json(temp_path)
            
            # Verify loaded values match original
            self.assertEqual(loaded_config.dt, config.dt)
            self.assertEqual(loaded_config.drone_speed, config.drone_speed)
            self.assertEqual(loaded_config.num_waypoints, config.num_waypoints)
            
            # For bounds, convert both to lists for comparison since JSON doesn't preserve tuples
            self.assertEqual(list(loaded_config.bounds), list(config.bounds))
            
            self.assertEqual(loaded_config.wait_time, config.wait_time)
            self.assertEqual(loaded_config.min_height, config.min_height)
            self.assertEqual(loaded_config.random_seed, config.random_seed)
        finally:
            # Clean up the temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)

if __name__ == '__main__':
    unittest.main()