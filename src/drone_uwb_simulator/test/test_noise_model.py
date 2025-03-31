import unittest
import numpy as np
from drone_uwb_simulator.UWB_protocol import NoiseModel

class TestNoiseModel(unittest.TestCase):
    """Test cases for the NoiseModel class."""
    
    def test_default_initialization(self):
        """Test that the NoiseModel initializes with default values."""
        model = NoiseModel()
        self.assertEqual(model.variance, 0.1)
        self.assertEqual(model.outlier_probability, 0.0)
        self.assertEqual(model.outlier_range, (0.2, 0.3))
        self.assertIsNone(model.random_seed)
    
    def test_custom_initialization(self):
        """Test that the NoiseModel initializes with custom values."""
        variance = 0.2
        outlier_probability = 0.05
        outlier_range = (0.4, 0.6)
        random_seed = 42
        
        model = NoiseModel(
            variance=variance,
            outlier_probability=outlier_probability,
            outlier_range=outlier_range,
            random_seed=random_seed
        )
        
        self.assertEqual(model.variance, variance)
        self.assertEqual(model.outlier_probability, outlier_probability)
        self.assertEqual(model.outlier_range, outlier_range)
        self.assertEqual(model.random_seed, random_seed)
    
    def test_negative_variance_validation(self):
        """Test that initializing with negative variance raises ValueError."""
        with self.assertRaises(ValueError):
            NoiseModel(variance=-0.1)
    
    def test_invalid_outlier_probability_validation(self):
        """Test that initializing with invalid outlier probability raises ValueError."""
        # Test probability < 0
        with self.assertRaises(ValueError):
            NoiseModel(outlier_probability=-0.1)
        
        # Test probability > 1
        with self.assertRaises(ValueError):
            NoiseModel(outlier_probability=1.1)
    
    def test_invalid_outlier_range_validation(self):
        """Test that initializing with invalid outlier range raises ValueError."""
        with self.assertRaises(ValueError):
            NoiseModel(outlier_range=(0.3, 0.2))  # min > max
    
    def test_apply_with_seed(self):
        """Test applying noise with a fixed random seed for deterministic testing."""
        model = NoiseModel(variance=0.01, outlier_probability=0.0, random_seed=42)
        
        # Apply noise to a distance
        distance = 10.0
        noisy_distance, noise_amount, is_outlier = model.apply(distance)
        
        # With variance 0.01, noise should typically be within +/- 0.3 (3 sigma)
        self.assertLess(abs(noise_amount), 0.3)
        self.assertEqual(noisy_distance, distance + noise_amount)
        self.assertFalse(is_outlier)
        
        # Check that using the same seed gives the same result
        model2 = NoiseModel(variance=0.01, outlier_probability=0.0, random_seed=42)
        noisy_distance2, noise_amount2, is_outlier2 = model2.apply(distance)
        
        self.assertEqual(noisy_distance, noisy_distance2)
        self.assertEqual(noise_amount, noise_amount2)
        self.assertEqual(is_outlier, is_outlier2)
    
    def test_apply_outlier(self):
        """Test generating outliers with a 100% outlier probability."""
        outlier_range = (0.4, 0.5)
        model = NoiseModel(
            variance=0.01,
            outlier_probability=1.0,  # Always generate outliers
            outlier_range=outlier_range,
            random_seed=42
        )
        
        distance = 10.0
        noisy_distance, noise_amount, is_outlier = model.apply(distance)
        
        # Verify it's an outlier
        self.assertTrue(is_outlier)
        
        # Noise should be within the outlier range * distance
        min_noise = distance * outlier_range[0]
        max_noise = distance * outlier_range[1]
        
        self.assertGreaterEqual(noise_amount, min_noise)
        self.assertLessEqual(noise_amount, max_noise)
    
    def test_apply_no_noise(self):
        """Test a 'no noise' model (variance=0, no outliers)."""
        model = NoiseModel(variance=0.0, outlier_probability=0.0)
        
        distance = 10.0
        noisy_distance, noise_amount, is_outlier = model.apply(distance)
        
        # With zero variance and no outliers, distance shouldn't change
        self.assertEqual(noisy_distance, distance)
        self.assertEqual(noise_amount, 0.0)
        self.assertFalse(is_outlier)
    
    def test_statistical_properties(self):
        """Test the statistical properties of the noise model (mean and variance)."""
        variance = 0.1
        model = NoiseModel(variance=variance, outlier_probability=0.0, random_seed=42)
        
        # Apply noise multiple times to check statistical properties
        distance = 10.0
        n_samples = 1000
        noise_values = []
        
        for _ in range(n_samples):
            _, noise, _ = model.apply(distance)
            noise_values.append(noise)
        
        # Check that the noise has approximately the expected mean and variance
        # (Allow some tolerance due to random sampling)
        sample_mean = np.mean(noise_values)
        sample_variance = np.var(noise_values)
        
        # Mean should be close to 0
        self.assertAlmostEqual(sample_mean, 0.0, delta=0.05)
        
        # Variance should be close to the specified value
        self.assertAlmostEqual(sample_variance, variance, delta=0.05)
    
    def test_representation(self):
        """Test the string representation of NoiseModel."""
        model = NoiseModel(variance=0.25, outlier_probability=0.1, outlier_range=(0.4, 0.6))
        representation = repr(model)
        
        # Verify the representation contains the relevant values
        self.assertIn("NoiseModel", representation)
        self.assertIn("0.25", representation)  # variance
        self.assertIn("0.1", representation)   # outlier_probability
        self.assertIn("(0.4, 0.6)", representation)  # outlier_range


if __name__ == '__main__':
    unittest.main()