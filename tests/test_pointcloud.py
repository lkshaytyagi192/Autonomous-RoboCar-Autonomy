import unittest
from src.sensors.scanner import ObstacleScanner
class TestCloud(unittest.TestCase):
    def test_pts(self):
        s = ObstacleScanner(angles=[0])
        s.record(0, 100.0)
        pts = s.to_points()
        self.assertEqual(pts[0], (1.0, 0.0))
if __name__ == '__main__': unittest.main()
