import unittest
import numpy as np
from drone_uwb_simulator.UWB_protocol import UWBNetwork, Anchor, BiasModel, NoiseModel, MeasurementResult

class TestUWBNetwork(unittest.TestCase):
    """Test cases for the UWBNetwork class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        # Create some test anchors
        self.anchor1 = Anchor("anchor1", [0.0, 0.0, 0.0])
        self.anchor2 = Anchor("anchor2", [10.0, 0.0, 0.0])
        self.anchor3 = Anchor("anchor3", [0.0, 10.0, 0.0])
        
        # Create test anchors with custom error models
        bias_model = BiasModel(constant_bias=0.1, linear_bias=1.05)
        noise_model = NoiseModel(variance=0.01, outlier_probability=0.0, random_seed=42)
        self.anchor4 = Anchor("anchor4", [10.0, 10.0, 0.0], bias_model, noise_model)
    
    def test_initialization_empty(self):
        """Test initializing an empty network."""
        network = UWBNetwork()
        self.assertEqual(len(network), 0)
        self.assertEqual(len(network.anchors), 0)
    
    def test_initialization_with_anchors(self):
        """Test initializing a network with anchors."""
        anchors = [self.anchor1, self.anchor2]
        network = UWBNetwork(anchors)
        
        self.assertEqual(len(network), 2)
        self.assertEqual(len(network.anchors), 2)
        self.assertIn(self.anchor1, network.anchors)
        self.assertIn(self.anchor2, network.anchors)
    
    def test_add_anchor(self):
        """Test adding anchors to the network."""
        network = UWBNetwork()
        
        # Add a single anchor
        network.add_anchor(self.anchor1)
        self.assertEqual(len(network), 1)
        self.assertIn(self.anchor1, network.anchors)
        
        # Add another anchor
        network.add_anchor(self.anchor2)
        self.assertEqual(len(network), 2)
        self.assertIn(self.anchor2, network.anchors)
    
    def test_add_anchor_duplicate_id(self):
        """Test that adding an anchor with a duplicate ID raises an error."""
        network = UWBNetwork([self.anchor1])
        
        # Create a new anchor with the same ID
        duplicate_anchor = Anchor(self.anchor1.anchor_id, [5.0, 5.0, 5.0])
        
        with self.assertRaises(ValueError):
            network.add_anchor(duplicate_anchor)
    
    def test_add_anchors(self):
        """Test adding multiple anchors at once."""
        network = UWBNetwork()
        anchors = [self.anchor1, self.anchor2, self.anchor3]
        
        network.add_anchors(anchors)
        
        self.assertEqual(len(network), 3)
        for anchor in anchors:
            self.assertIn(anchor, network.anchors)
    
    def test_remove_anchor(self):
        """Test removing an anchor from the network."""
        network = UWBNetwork([self.anchor1, self.anchor2])
        
        # Remove an existing anchor
        result = network.remove_anchor(self.anchor1.anchor_id)
        
        self.assertTrue(result)
        self.assertEqual(len(network), 1)
        self.assertNotIn(self.anchor1, network.anchors)
        self.assertIn(self.anchor2, network.anchors)
        
        # Try to remove a non-existent anchor
        result = network.remove_anchor("non_existent")
        
        self.assertFalse(result)
        self.assertEqual(len(network), 1)
    
    def test_get_anchor(self):
        """Test retrieving anchors by ID."""
        network = UWBNetwork([self.anchor1, self.anchor2])
        
        # Get an existing anchor
        anchor = network.get_anchor(self.anchor1.anchor_id)
        
        self.assertEqual(anchor, self.anchor1)
        
        # Try to get a non-existent anchor
        anchor = network.get_anchor("non_existent")
        
        self.assertIsNone(anchor)
    
    def test_measure_distances_no_errors(self):
        """Test measuring distances without errors."""
        network = UWBNetwork([self.anchor1, self.anchor2, self.anchor3])
        target_position = [5.0, 5.0, 0.0]
        
        measurements = network.measure_distances(
            target_position, 
            include_errors=False
        )
        
        self.assertEqual(len(measurements), 3)
        
        # Verify distances
        self.assertAlmostEqual(
            measurements[self.anchor1.anchor_id], 
            np.sqrt(5.0**2 + 5.0**2)
        )
        self.assertAlmostEqual(
            measurements[self.anchor2.anchor_id], 
            np.sqrt(5.0**2 + 5.0**2)
        )
        self.assertAlmostEqual(
            measurements[self.anchor3.anchor_id], 
            np.sqrt(5.0**2 + 5.0**2)
        )
    
    def test_measure_distances_with_errors(self):
        """Test measuring distances with errors."""
        network = UWBNetwork([self.anchor4])  # Use the anchor with known error models
        target_position = [5.0, 5.0, 0.0]
        
        measurements = network.measure_distances(
            target_position, 
            include_errors=True
        )
        
        # We should still get measurements, but they'll include errors
        self.assertEqual(len(measurements), 1)
        
        # The exact value is deterministic but depends on the noise model implementation
        # Just ensure we got a value for the anchor
        self.assertIn(self.anchor4.anchor_id, measurements)
    
    def test_measure_distances_detailed_results(self):
        """Test getting detailed measurement results."""
        network = UWBNetwork([self.anchor1, self.anchor4])  # Mix of anchors
        target_position = [5.0, 5.0, 0.0]
        
        results = network.measure_distances(
            target_position, 
            include_errors=True,
            return_details=True
        )
        
        self.assertEqual(len(results), 2)
        
        # Verify results are MeasurementResult objects
        for anchor_id, result in results.items():
            self.assertIsInstance(result, MeasurementResult)
            self.assertEqual(result.anchor_id, anchor_id)
    
    def test_measure_distances_filtered_anchors(self):
        """Test measuring distances with only selected anchors."""
        network = UWBNetwork([self.anchor1, self.anchor2, self.anchor3])
        target_position = [5.0, 5.0, 0.0]
        
        # Only measure from anchor1 and anchor3
        selected_anchors = [self.anchor1.anchor_id, self.anchor3.anchor_id]
        
        measurements = network.measure_distances(
            target_position, 
            include_errors=False,
            anchor_ids=selected_anchors
        )
        
        self.assertEqual(len(measurements), 2)
        self.assertIn(self.anchor1.anchor_id, measurements)
        self.assertIn(self.anchor3.anchor_id, measurements)
        self.assertNotIn(self.anchor2.anchor_id, measurements)
    
    def test_measure_distances_empty_network(self):
        """Test measuring distances with an empty network."""
        network = UWBNetwork()
        target_position = [5.0, 5.0, 0.0]
        
        measurements = network.measure_distances(target_position)
        
        self.assertEqual(measurements, {})
    
    def test_get_anchor_positions(self):
        """Test getting anchor positions."""
        network = UWBNetwork([self.anchor1, self.anchor2, self.anchor3])
        
        # Get all anchor positions
        positions = network.get_anchor_positions()
        
        self.assertEqual(len(positions), 3)
        np.testing.assert_array_equal(positions[self.anchor1.anchor_id], self.anchor1.position)
        np.testing.assert_array_equal(positions[self.anchor2.anchor_id], self.anchor2.position)
        np.testing.assert_array_equal(positions[self.anchor3.anchor_id], self.anchor3.position)
        
        # Get selected anchor positions
        selected_anchors = [self.anchor1.anchor_id, self.anchor3.anchor_id]
        positions = network.get_anchor_positions(selected_anchors)
        
        self.assertEqual(len(positions), 2)
        self.assertIn(self.anchor1.anchor_id, positions)
        self.assertIn(self.anchor3.anchor_id, positions)
        self.assertNotIn(self.anchor2.anchor_id, positions)
    
    def test_update_anchor_position(self):
        """Test updating an anchor's position."""
        network = UWBNetwork([self.anchor1])
        new_position = [5.0, 5.0, 5.0]
        
        # Update an existing anchor
        result = network.update_anchor_position(self.anchor1.anchor_id, new_position)
        
        self.assertTrue(result)
        np.testing.assert_array_equal(self.anchor1.position, np.array(new_position))
        
        # Try to update a non-existent anchor
        result = network.update_anchor_position("non_existent", new_position)
        
        self.assertFalse(result)
    
    def test_reset_measurements(self):
        """Test resetting all stored measurements."""
        network = UWBNetwork([self.anchor1, self.anchor2])
        target_position = [5.0, 5.0, 0.0]
        
        # Make measurements
        network.measure_distances(target_position, include_errors=True)
        
        # Verify measurements are stored
        self.assertIsNotNone(self.anchor1.get_last_measurement())
        self.assertIsNotNone(self.anchor2.get_last_measurement())
        
        # Reset measurements
        network.reset_measurements()
        
        # Verify measurements are cleared
        self.assertIsNone(self.anchor1.get_last_measurement())
        self.assertIsNone(self.anchor2.get_last_measurement())
    
    def test_get_measurement_errors(self):
        """Test getting measurement errors."""
        network = UWBNetwork([self.anchor1, self.anchor2])
        target_position = [5.0, 5.0, 0.0]
        
        # Make measurements with errors
        network.measure_distances(target_position, include_errors=True)
        
        # Get errors
        errors = network.get_measurement_errors()
        
        self.assertEqual(len(errors), 2)
        self.assertIn(self.anchor1.anchor_id, errors)
        self.assertIn(self.anchor2.anchor_id, errors)
    
    def test_representation(self):
        """Test the string representation of UWBNetwork."""
        network = UWBNetwork([self.anchor1, self.anchor2])
        representation = repr(network)
        
        self.assertIn("UWBNetwork", representation)
        self.assertIn("2", representation)  # number of anchors


if __name__ == '__main__':
    unittest.main()