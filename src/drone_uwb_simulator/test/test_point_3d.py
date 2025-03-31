import unittest
import numpy as np
from drone_uwb_simulator.drone_dynamics import Point3D

class TestPoint3D(unittest.TestCase):
    """Test cases for the Point3D class."""
    
    def test_initialization(self):
        """Test initialization of Point3D objects."""
        # Test with integer coordinates
        point = Point3D(1, 2, 3)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.z, 3)
        
        # Test with float coordinates
        point = Point3D(1.5, 2.5, 3.5)
        self.assertEqual(point.x, 1.5)
        self.assertEqual(point.y, 2.5)
        self.assertEqual(point.z, 3.5)
    
    def test_immutability(self):
        """Test that Point3D objects are immutable."""
        point = Point3D(1, 2, 3)
        
        # Attempting to modify the point should raise an exception
        with self.assertRaises(Exception):
            point.x = 10
        
        with self.assertRaises(Exception):
            point.y = 20
        
        with self.assertRaises(Exception):
            point.z = 30
    
    def test_as_array(self):
        """Test conversion to numpy array."""
        point = Point3D(1, 2, 3)
        array = point.as_array()
        
        self.assertIsInstance(array, np.ndarray)
        self.assertEqual(array.shape, (3,))
        np.testing.assert_array_equal(array, np.array([1, 2, 3]))
    
    def test_distance_to(self):
        """Test calculating distance between points."""
        point1 = Point3D(0, 0, 0)
        point2 = Point3D(3, 4, 0)
        
        # Distance should be 5 (Pythagorean theorem)
        self.assertEqual(point1.distance_to(point2), 5.0)
        
        # Distance should be symmetric
        self.assertEqual(point2.distance_to(point1), 5.0)
        
        # Distance to self should be 0
        self.assertEqual(point1.distance_to(point1), 0.0)
        
        # Test with 3D distance
        point3 = Point3D(1, 1, 1)
        distance = np.sqrt(3)  # sqrt(1^2 + 1^2 + 1^2)
        self.assertAlmostEqual(point1.distance_to(point3), distance)
    
    def test_repr(self):
        """Test string representation."""
        point = Point3D(1.234, 2.345, 3.456)
        representation = repr(point)
        
        # Verify format and rounding to 2 decimal places
        self.assertEqual(representation, "Point3D(1.23, 2.35, 3.46)")
        
        # Test with integer values
        point = Point3D(1, 2, 3)
        representation = repr(point)
        self.assertEqual(representation, "Point3D(1.00, 2.00, 3.00)")


if __name__ == '__main__':
    unittest.main()