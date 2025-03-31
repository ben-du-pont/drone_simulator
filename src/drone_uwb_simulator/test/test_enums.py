import unittest
from drone_uwb_simulator.drone_simulator import (
    WaypointMode, AnchorPlacementStrategy
)

class TestWaypointMode(unittest.TestCase):
    """Test cases for the WaypointMode enum."""
    
    def test_enum_values(self):
        """Test that enum values exist and are unique."""
        # Verify all expected values exist
        self.assertIsNotNone(WaypointMode.MANUAL)
        self.assertIsNotNone(WaypointMode.RANDOM)
        self.assertIsNotNone(WaypointMode.OPPOSITE_EDGES)
        self.assertIsNotNone(WaypointMode.GRID)
        self.assertIsNotNone(WaypointMode.SPIRAL)
        
        # Create a set of values to check uniqueness
        values = {
            WaypointMode.MANUAL,
            WaypointMode.RANDOM,
            WaypointMode.OPPOSITE_EDGES,
            WaypointMode.GRID,
            WaypointMode.SPIRAL
        }
        
        # Number of unique values should match number of enum members
        self.assertEqual(len(values), 5)


class TestAnchorPlacementStrategy(unittest.TestCase):
    """Test cases for the AnchorPlacementStrategy enum."""
    
    def test_enum_values(self):
        """Test that enum values exist and are unique."""
        # Verify all expected values exist
        self.assertIsNotNone(AnchorPlacementStrategy.FIXED)
        self.assertIsNotNone(AnchorPlacementStrategy.RANDOM)
        self.assertIsNotNone(AnchorPlacementStrategy.CORNERS)
        self.assertIsNotNone(AnchorPlacementStrategy.OPTIMIZED)
        
        # Create a set of values to check uniqueness
        values = {
            AnchorPlacementStrategy.FIXED,
            AnchorPlacementStrategy.RANDOM,
            AnchorPlacementStrategy.CORNERS,
            AnchorPlacementStrategy.OPTIMIZED
        }
        
        # Number of unique values should match number of enum members
        self.assertEqual(len(values), 4)


if __name__ == '__main__':
    unittest.main()