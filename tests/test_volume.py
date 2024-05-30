import unittest
from foo_parameterization import calculate_volume

class TestCalculateVolume(unittest.TestCase):
    
    def test_volume_positive_radius(self):
        self.assertAlmostEqual(calculate_volume(1), 4.1887902047863905)
        
    def test_volume_zero_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(0)
            
    def test_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1)

if __name__ == "__main__":
    unittest.main()
