import unittest
import numpy as np
from drone_uwb_simulator.UWB_protocol import BiasModel

class TestBiasModel(unittest.TestCase):
    """Test cases for the BiasModel class."""
    
    def test_default_initialization(self):
        """Test that the BiasModel initializes with default values."""
        model = BiasModel()
        self.assertEqual(model.constant_bias, 0.0)
        self.assertEqual(model.linear_bias, 1.0)
    
    def test_custom_initialization(self):
        """Test that the BiasModel initializes with custom values."""
        constant_bias = 0.15
        linear_bias = 1.03
        model = BiasModel(constant_bias=constant_bias, linear_bias=linear_bias)
        self.assertEqual(model.constant_bias, constant_bias)
        self.assertEqual(model.linear_bias, linear_bias)
    
    def test_apply_zero_distance(self):
        """Test applying bias to a zero distance."""
        model = BiasModel(constant_bias=0.1, linear_bias=1.05)
        biased_distance, bias_amount = model.apply(0.0)
        self.assertEqual(biased_distance, 0.1)
        self.assertEqual(bias_amount, 0.1)
    
    def test_apply_positive_distance(self):
        """Test applying bias to a positive distance."""
        model = BiasModel(constant_bias=0.1, linear_bias=1.05)
        
        # Test with a simple distance
        distance = 10.0
        expected_biased = 0.1 + 1.05 * 10.0
        expected_bias = expected_biased - distance
        
        biased_distance, bias_amount = model.apply(distance)
        
        self.assertAlmostEqual(biased_distance, expected_biased)
        self.assertAlmostEqual(bias_amount, expected_bias)
    
    def test_apply_negative_distance(self):
        """Test applying bias to a negative distance (unusual but should work)."""
        model = BiasModel(constant_bias=0.1, linear_bias=1.05)
        
        # Test with a negative distance
        distance = -5.0
        expected_biased = 0.1 + 1.05 * (-5.0)
        expected_bias = expected_biased - distance
        
        biased_distance, bias_amount = model.apply(distance)
        
        self.assertAlmostEqual(biased_distance, expected_biased)
        self.assertAlmostEqual(bias_amount, expected_bias)
    
    def test_no_bias(self):
        """Test that a 'no bias' model doesn't change distances."""
        model = BiasModel(constant_bias=0.0, linear_bias=1.0)
        
        # Test with a simple distance
        distance = 10.0
        biased_distance, bias_amount = model.apply(distance)
        
        self.assertEqual(biased_distance, distance)
        self.assertEqual(bias_amount, 0.0)
    
    def test_representation(self):
        """Test the string representation of BiasModel."""
        model = BiasModel(constant_bias=0.123, linear_bias=1.056)
        representation = repr(model)
        
        # Verify the representation contains the relevant values
        self.assertIn("BiasModel", representation)
        self.assertIn("0.123", representation)
        self.assertIn("1.056", representation)


if __name__ == '__main__':
    unittest.main()