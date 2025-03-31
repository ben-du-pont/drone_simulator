import unittest
from drone_uwb_simulator.drone_dynamics import TrajectoryStats

class TestTrajectoryStats(unittest.TestCase):
    """Test cases for the TrajectoryStats class."""
    
    def test_initialization(self):
        """Test initialization of TrajectoryStats objects."""
        # Test with sample values
        max_deviation = 0.1
        mean_deviation = 0.05
        expected_distance = 2.0
        constant_speed = True
        total_length = 100.0
        duration = 50.0
        
        stats = TrajectoryStats(
            max_deviation=max_deviation,
            mean_deviation=mean_deviation,
            expected_distance=expected_distance,
            constant_speed=constant_speed,
            total_length=total_length,
            duration=duration
        )
        
        self.assertEqual(stats.max_deviation, max_deviation)
        self.assertEqual(stats.mean_deviation, mean_deviation)
        self.assertEqual(stats.expected_distance, expected_distance)
        self.assertEqual(stats.constant_speed, constant_speed)
        self.assertEqual(stats.total_length, total_length)
        self.assertEqual(stats.duration, duration)
    
    def test_max_deviation_percentage(self):
        """Test calculation of max deviation percentage."""
        # Normal case
        stats = TrajectoryStats(
            max_deviation=0.1,
            mean_deviation=0.05,
            expected_distance=2.0,
            constant_speed=True,
            total_length=100.0,
            duration=50.0
        )
        
        # 0.1 / 2.0 * 100 = 5%
        self.assertEqual(stats.max_deviation_percentage, 5.0)
        
        # Edge case: expected_distance = 0
        stats = TrajectoryStats(
            max_deviation=0.1,
            mean_deviation=0.05,
            expected_distance=0.0,
            constant_speed=True,
            total_length=100.0,
            duration=50.0
        )
        
        self.assertEqual(stats.max_deviation_percentage, float('inf'))
    
    def test_mean_deviation_percentage(self):
        """Test calculation of mean deviation percentage."""
        # Normal case
        stats = TrajectoryStats(
            max_deviation=0.1,
            mean_deviation=0.05,
            expected_distance=2.0,
            constant_speed=True,
            total_length=100.0,
            duration=50.0
        )
        
        # 0.05 / 2.0 * 100 = 2.5%
        self.assertEqual(stats.mean_deviation_percentage, 2.5)
        
        # Edge case: expected_distance = 0
        stats = TrajectoryStats(
            max_deviation=0.1,
            mean_deviation=0.05,
            expected_distance=0.0,
            constant_speed=True,
            total_length=100.0,
            duration=50.0
        )
        
        self.assertEqual(stats.mean_deviation_percentage, float('inf'))


if __name__ == '__main__':
    unittest.main()