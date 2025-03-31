import unittest
import numpy as np
from drone_uwb_simulator.UWB_protocol import Anchor, BiasModel, NoiseModel, MeasurementResult

class TestAnchor(unittest.TestCase):
    """Test cases for the Anchor class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        self.anchor_id = "test_anchor"
        self.position = [1.0, 2.0, 3.0]
        self.bias_model = BiasModel(constant_bias=0.1, linear_bias=1.05)
        self.noise_model = NoiseModel(variance=0.01, outlier_probability=0.0, random_seed=42)
        
        # Create a standard anchor for testing
        self.anchor = Anchor(
            self.anchor_id,
            self.position,
            self.bias_model,
            self.noise_model
        )
    
    def test_initialization(self):
        """Test anchor initialization with different parameters."""
        # Test with all parameters
        anchor = Anchor(self.anchor_id, self.position, self.bias_model, self.noise_model)
        self.assertEqual(anchor.anchor_id, self.anchor_id)
        np.testing.assert_array_equal(anchor.position, np.array(self.position))
        self.assertEqual(anchor.bias_model, self.bias_model)
        self.assertEqual(anchor.noise_model, self.noise_model)
        
        # Test with default error models
        anchor = Anchor(self.anchor_id, self.position)
        self.assertEqual(anchor.anchor_id, self.anchor_id)
        np.testing.assert_array_equal(anchor.position, np.array(self.position))
        self.assertIsInstance(anchor.bias_model, BiasModel)
        self.assertIsInstance(anchor.noise_model, NoiseModel)
    
    def test_from_coordinates_factory(self):
        """Test the from_coordinates factory method."""
        x, y, z = 4.0, 5.0, 6.0
        anchor = Anchor.from_coordinates(
            self.anchor_id, x, y, z, self.bias_model, self.noise_model
        )
        
        self.assertEqual(anchor.anchor_id, self.anchor_id)
        np.testing.assert_array_equal(anchor.position, np.array([x, y, z]))
        self.assertEqual(anchor.bias_model, self.bias_model)
        self.assertEqual(anchor.noise_model, self.noise_model)
    
    def test_measure_distance_no_errors(self):
        """Test measuring distance without applying error models."""
        target_position = [4.0, 6.0, 8.0]
        
        # Calculate expected distance manually
        expected_distance = np.sqrt(
            (target_position[0] - self.position[0])**2 +
            (target_position[1] - self.position[1])**2 +
            (target_position[2] - self.position[2])**2
        )
        
        # Measure without errors
        measured_distance = self.anchor.measure_distance(target_position, include_errors=False)
        
        self.assertAlmostEqual(measured_distance, expected_distance)
    
    def test_measure_distance_with_errors(self):
        """Test measuring distance with error models applied."""
        target_position = [4.0, 6.0, 8.0]
        
        # Measure with errors
        result = self.anchor.measure_distance(target_position, include_errors=True)
        
        # Verify the result is a MeasurementResult object
        self.assertIsInstance(result, MeasurementResult)
        
        # Calculate expected true distance
        expected_true_distance = np.sqrt(
            (target_position[0] - self.position[0])**2 +
            (target_position[1] - self.position[1])**2 +
            (target_position[2] - self.position[2])**2
        )
        
        # Verify true distance in result
        self.assertAlmostEqual(result.true_distance, expected_true_distance)
        
        # Verify the bias was applied correctly
        expected_biased = self.bias_model.constant_bias + self.bias_model.linear_bias * expected_true_distance
        expected_bias = expected_biased - expected_true_distance
        
        self.assertAlmostEqual(result.bias_applied, expected_bias)
        
        # Verify the result contains the anchor ID
        self.assertEqual(result.anchor_id, self.anchor_id)
    
    def test_get_last_measurement(self):
        """Test retrieving the last measurement result."""
        # Initially, there should be no last measurement
        self.assertIsNone(self.anchor.get_last_measurement())
        
        # Make a measurement
        target_position = [4.0, 6.0, 8.0]
        result = self.anchor.measure_distance(target_position, include_errors=True)
        
        # Verify the last measurement is stored correctly
        last_measurement = self.anchor.get_last_measurement()
        self.assertIsNotNone(last_measurement)
        self.assertEqual(last_measurement, result)
    
    def test_update_bias_model(self):
        """Test updating the bias model parameters."""
        new_constant_bias = 0.2
        new_linear_bias = 1.1
        
        # Update both parameters
        self.anchor.update_bias_model(
            constant_bias=new_constant_bias,
            linear_bias=new_linear_bias
        )
        
        self.assertEqual(self.anchor.bias_model.constant_bias, new_constant_bias)
        self.assertEqual(self.anchor.bias_model.linear_bias, new_linear_bias)
        
        # Update only constant bias
        newer_constant_bias = 0.3
        self.anchor.update_bias_model(constant_bias=newer_constant_bias)
        
        self.assertEqual(self.anchor.bias_model.constant_bias, newer_constant_bias)
        self.assertEqual(self.anchor.bias_model.linear_bias, new_linear_bias)
        
        # Update only linear bias
        newer_linear_bias = 1.2
        self.anchor.update_bias_model(linear_bias=newer_linear_bias)
        
        self.assertEqual(self.anchor.bias_model.constant_bias, newer_constant_bias)
        self.assertEqual(self.anchor.bias_model.linear_bias, newer_linear_bias)
    
    def test_update_noise_model(self):
        """Test updating the noise model parameters."""
        new_variance = 0.2
        new_outlier_probability = 0.1
        new_outlier_range = (0.5, 0.6)
        new_random_seed = 123
        
        # Update all parameters
        self.anchor.update_noise_model(
            variance=new_variance,
            outlier_probability=new_outlier_probability,
            outlier_range=new_outlier_range,
            random_seed=new_random_seed
        )
        
        self.assertEqual(self.anchor.noise_model.variance, new_variance)
        self.assertEqual(self.anchor.noise_model.outlier_probability, new_outlier_probability)
        self.assertEqual(self.anchor.noise_model.outlier_range, new_outlier_range)
        self.assertEqual(self.anchor.noise_model.random_seed, new_random_seed)
        
        # Update only variance
        newer_variance = 0.3
        self.anchor.update_noise_model(variance=newer_variance)
        
        self.assertEqual(self.anchor.noise_model.variance, newer_variance)
        self.assertEqual(self.anchor.noise_model.outlier_probability, new_outlier_probability)
    
    def test_ground_truth_property(self):
        """Test the ground_truth property returns correct values."""
        ground_truth = self.anchor.ground_truth
        
        self.assertIn('position', ground_truth)
        self.assertIn('bias_model', ground_truth)
        self.assertIn('noise_model', ground_truth)
        
        np.testing.assert_array_equal(ground_truth['position'], np.array(self.position))
        self.assertEqual(ground_truth['bias_model'], self.bias_model)
        self.assertEqual(ground_truth['noise_model'], self.noise_model)
    
    def test_representation(self):
        """Test the string representation of Anchor."""
        representation = repr(self.anchor)
        
        # Verify the representation contains the relevant values
        self.assertIn("Anchor", representation)
        self.assertIn(self.anchor_id, representation)
        
        # Check if the position is in the representation
        for coord in self.position:
            self.assertIn(str(round(coord, 2)), representation)


if __name__ == '__main__':
    unittest.main()