import unittest
import numpy as np
from drone_uwb_simulator.drone_dynamics import Waypoint, Point3D

class TestWaypoint(unittest.TestCase):
    """Test cases for the Waypoint class."""
    
    def test_initialization(self):
        """Test initialization of Waypoint objects."""
        # Test with integer coordinates
        waypoint = Waypoint(1, 2, 3)
        self.assertEqual(waypoint.x, 1.0)
        self.assertEqual(waypoint.y, 2.0)
        self.assertEqual(waypoint.z, 3.0)
        
        # Verify conversion to float
        self.assertIsInstance(waypoint.x, float)
        self.assertIsInstance(waypoint.y, float)
        self.assertIsInstance(waypoint.z, float)
        
        # Test with float coordinates
        waypoint = Waypoint(1.5, 2.5, 3.5)
        self.assertEqual(waypoint.x, 1.5)
        self.assertEqual(waypoint.y, 2.5)
        self.assertEqual(waypoint.z, 3.5)
        
        # Test with string coordinates (should convert to float)
        waypoint = Waypoint("1", "2", "3")
        self.assertEqual(waypoint.x, 1.0)
        self.assertEqual(waypoint.y, 2.0)
        self.assertEqual(waypoint.z, 3.0)
    
    def test_from_point(self):
        """Test creating a waypoint from a Point3D object."""
        point = Point3D(1, 2, 3)
        waypoint = Waypoint.from_point(point)
        
        self.assertEqual(waypoint.x, point.x)
        self.assertEqual(waypoint.y, point.y)
        self.assertEqual(waypoint.z, point.z)
    
    def test_from_array(self):
        """Test creating a waypoint from an array."""
        # Test with numpy array
        array = np.array([1, 2, 3])
        waypoint = Waypoint.from_array(array)
        
        self.assertEqual(waypoint.x, 1.0)
        self.assertEqual(waypoint.y, 2.0)
        self.assertEqual(waypoint.z, 3.0)
        
        # Test with list
        waypoint = Waypoint.from_array([4, 5, 6])
        
        self.assertEqual(waypoint.x, 4.0)
        self.assertEqual(waypoint.y, 5.0)
        self.assertEqual(waypoint.z, 6.0)
        
        # Test with tuple
        waypoint = Waypoint.from_array((7, 8, 9))
        
        self.assertEqual(waypoint.x, 7.0)
        self.assertEqual(waypoint.y, 8.0)
        self.assertEqual(waypoint.z, 9.0)
        
        # Test with invalid array shape
        with self.assertRaises(ValueError):
            Waypoint.from_array([1, 2])
        
        with self.assertRaises(ValueError):
            Waypoint.from_array([1, 2, 3, 4])
    
    def test_to_point3d(self):
        """Test conversion to Point3D."""
        waypoint = Waypoint(1, 2, 3)
        point = waypoint.to_point3d()
        
        self.assertIsInstance(point, Point3D)
        self.assertEqual(point.x, waypoint.x)
        self.assertEqual(point.y, waypoint.y)
        self.assertEqual(point.z, waypoint.z)
    
    def test_get_coordinates(self):
        """Test getting coordinates as a numpy array."""
        waypoint = Waypoint(1, 2, 3)
        coords = waypoint.get_coordinates()
        
        self.assertIsInstance(coords, np.ndarray)
        self.assertEqual(coords.shape, (3,))
        self.assertEqual(coords.dtype, np.float64)
        np.testing.assert_array_equal(coords, np.array([1.0, 2.0, 3.0]))
    
    def test_distance_to_waypoint(self):
        """Test calculating distance to another waypoint."""
        waypoint1 = Waypoint(0, 0, 0)
        waypoint2 = Waypoint(3, 4, 0)
        
        # Distance should be 5 (Pythagorean theorem)
        self.assertEqual(waypoint1.distance_to(waypoint2), 5.0)
        
        # Distance should be symmetric
        self.assertEqual(waypoint2.distance_to(waypoint1), 5.0)
        
        # Distance to self should be 0
        self.assertEqual(waypoint1.distance_to(waypoint1), 0.0)
    
    def test_distance_to_position(self):
        """Test calculating distance to a position."""
        waypoint = Waypoint(0, 0, 0)
        
        # Test with numpy array
        position = np.array([3, 4, 0])
        self.assertEqual(waypoint.distance_to(position), 5.0)
        
        # Test with list
        position = [3, 4, 0]
        self.assertEqual(waypoint.distance_to(position), 5.0)
        
        # Test with tuple
        position = (3, 4, 0)
        self.assertEqual(waypoint.distance_to(position), 5.0)
        
        # Test with invalid position shape
        with self.assertRaises(ValueError):
            waypoint.distance_to([1, 2])
    
    def test_repr(self):
        """Test string representation."""
        waypoint = Waypoint(1.234, 2.345, 3.456)
        representation = repr(waypoint)
        
        # Verify format and rounding to 2 decimal places
        self.assertEqual(representation, "Waypoint(1.23, 2.35, 3.46)")
    
    def test_equality(self):
        """Test equality comparison between waypoints."""
        waypoint1 = Waypoint(1, 2, 3)
        waypoint2 = Waypoint(1, 2, 3)
        waypoint3 = Waypoint(4, 5, 6)
        
        # Equal waypoints
        self.assertEqual(waypoint1, waypoint2)
        self.assertTrue(waypoint1 == waypoint2)
        
        # Different waypoints
        self.assertNotEqual(waypoint1, waypoint3)
        self.assertTrue(waypoint1 != waypoint3)
        
        # Comparison with non-Waypoint object
        self.assertNotEqual(waypoint1, "waypoint")
        self.assertFalse(waypoint1 == "waypoint")


if __name__ == '__main__':
    unittest.main()