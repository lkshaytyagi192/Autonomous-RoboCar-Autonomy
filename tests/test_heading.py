import unittest, numpy as np
from src.navigation.heading import normalize_angle
class TestHeading(unittest.TestCase):
    def test_norm(self):
        self.assertAlmostEqual(normalize_angle(3 * np.pi), np.pi, places=2)
if __name__ == '__main__': unittest.main()
