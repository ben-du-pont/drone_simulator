import unittest
from drone_uwb_simulator.drone_dynamics import InterpolationMethod

class TestInterpolationMethod(unittest.TestCase):
    """Test cases for the InterpolationMethod enum."""
    
    def test_enum_values(self):
        """Test that enum values exist and are unique."""
        self.assertIsNotNone(InterpolationMethod.LINEAR)
        self.assertIsNotNone(InterpolationMethod.SPLINE)
        
        # Values should be different
        self.assertNotEqual(InterpolationMethod.LINEAR, InterpolationMethod.SPLINE)
    
    def test_from_string_valid(self):
        """Test conversion from valid string to enum value."""
        # Test conversion with lowercase
        self.assertEqual(
            InterpolationMethod.from_string("linear"),
            InterpolationMethod.LINEAR
        )
        self.assertEqual(
            InterpolationMethod.from_string("spline"),
            InterpolationMethod.SPLINE
        )
        
        # Test conversion with mixed case (should be case-insensitive)
        self.assertEqual(
            InterpolationMethod.from_string("Linear"),
            InterpolationMethod.LINEAR
        )
        self.assertEqual(
            InterpolationMethod.from_string("SPLINE"),
            InterpolationMethod.SPLINE
        )
    
    def test_from_string_invalid(self):
        """Test conversion from invalid string raises ValueError."""
        with self.assertRaises(ValueError):
            InterpolationMethod.from_string("invalid_method")
        
        with self.assertRaises(ValueError):
            InterpolationMethod.from_string("")
            
        # Error message should list valid methods
        try:
            InterpolationMethod.from_string("invalid_method")
        except ValueError as e:
            error_message = str(e)
            self.assertIn("Valid methods are", error_message)
            self.assertIn("linear", error_message.lower())
            self.assertIn("spline", error_message.lower())


if __name__ == '__main__':
    unittest.main()