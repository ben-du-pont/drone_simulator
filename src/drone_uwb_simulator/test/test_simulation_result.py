import unittest
import numpy as np
import tempfile
import os
import json
from drone_uwb_simulator.drone_simulator import SimulationResult, AnchorID

class TestSimulationResult(unittest.TestCase):
    """Test cases for the SimulationResult class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        # Sample data for testing
        self.positions = [
            np.array([0.0, 0.0, 0.0]),
            np.array([1.0, 1.0, 1.0]),
            np.array([2.0, 2.0, 2.0])
        ]
        
        self.measurements = [
            {"A1": 1.0, "A2": 2.0, "A3": 3.0},
            {"A1": 2.0, "A2": 3.0, "A3": 4.0},
            {"A1": 3.0, "A2": 4.0, "A3": 5.0}
        ]
        
        self.timestamps = [0.0, 1.0, 2.0]
    
    def test_initialization(self):
        """Test initialization of SimulationResult objects."""
        # Test default initialization
        result = SimulationResult()
        self.assertEqual(len(result.drone_positions), 0)
        self.assertEqual(len(result.anchor_measurements), 0)
        self.assertEqual(len(result.timestamps), 0)
    
    def test_add_step(self):
        """Test adding simulation steps."""
        result = SimulationResult()
        
        # Add a step
        position = np.array([1.0, 2.0, 3.0])
        measurements = {"A1": 1.0, "A2": 2.0}
        timestamp = 0.5
        
        result.add_step(position, measurements, timestamp)
        
        # Verify data was added
        self.assertEqual(len(result.drone_positions), 1)
        self.assertEqual(len(result.anchor_measurements), 1)
        self.assertEqual(len(result.timestamps), 1)
        
        # Verify values
        np.testing.assert_array_equal(result.drone_positions[0], position)
        self.assertEqual(result.anchor_measurements[0], measurements)
        self.assertEqual(result.timestamps[0], timestamp)
        
        # Add more steps
        for i in range(3):
            result.add_step(
                self.positions[i],
                self.measurements[i],
                self.timestamps[i]
            )
        
        # Verify all data
        self.assertEqual(len(result.drone_positions), 4)  # 1 initial + 3 new
        self.assertEqual(len(result.anchor_measurements), 4)
        self.assertEqual(len(result.timestamps), 4)
    
    def test_clear(self):
        """Test clearing simulation results."""
        result = SimulationResult()
        
        # Add some steps
        for i in range(3):
            result.add_step(
                self.positions[i],
                self.measurements[i],
                self.timestamps[i]
            )
        
        # Verify data exists
        self.assertEqual(len(result.drone_positions), 3)
        
        # Clear results
        result.clear()
        
        # Verify data was cleared
        self.assertEqual(len(result.drone_positions), 0)
        self.assertEqual(len(result.anchor_measurements), 0)
        self.assertEqual(len(result.timestamps), 0)
    
    def test_to_dict(self):
        """Test converting results to a dictionary."""
        result = SimulationResult()
        
        # Add some steps
        for i in range(3):
            result.add_step(
                self.positions[i],
                self.measurements[i],
                self.timestamps[i]
            )
        
        # Convert to dict
        result_dict = result.to_dict()
        
        # Verify dictionary structure
        self.assertIn("drone_positions", result_dict)
        self.assertIn("anchor_measurements", result_dict)
        self.assertIn("timestamps", result_dict)
        
        # Verify data
        self.assertEqual(len(result_dict["drone_positions"]), 3)
        self.assertEqual(len(result_dict["anchor_measurements"]), 3)
        self.assertEqual(len(result_dict["timestamps"]), 3)
        
        # Positions should be converted to lists
        self.assertIsInstance(result_dict["drone_positions"][0], list)
        
        # Measurements should be preserved
        self.assertEqual(result_dict["anchor_measurements"], self.measurements)
        
        # Timestamps should be preserved
        self.assertEqual(result_dict["timestamps"], self.timestamps)
    
    def test_json_serialization(self):
        """Test saving and loading results to/from JSON."""
        result = SimulationResult()
        
        # Add some steps
        for i in range(3):
            result.add_step(
                self.positions[i],
                self.measurements[i],
                self.timestamps[i]
            )
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            temp_path = temp_file.name
        
        try:
            result.to_json(temp_path)
            
            # Verify file exists and is not empty
            self.assertTrue(os.path.exists(temp_path))
            self.assertGreater(os.path.getsize(temp_path), 0)
            
            # Load back
            loaded_result = SimulationResult.from_json(temp_path)
            
            # Verify loaded data
            self.assertEqual(len(loaded_result.drone_positions), 3)
            self.assertEqual(len(loaded_result.anchor_measurements), 3)
            self.assertEqual(len(loaded_result.timestamps), 3)
            
            # Verify position data is correctly loaded as numpy arrays
            for i in range(3):
                np.testing.assert_array_almost_equal(
                    loaded_result.drone_positions[i],
                    self.positions[i]
                )
            
            # Verify measurements are preserved
            self.assertEqual(loaded_result.anchor_measurements, self.measurements)
            
            # Verify timestamps are preserved
            self.assertEqual(loaded_result.timestamps, self.timestamps)
            
        finally:
            # Clean up the temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)


if __name__ == '__main__':
    unittest.main()