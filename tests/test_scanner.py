import unittest
from src.sensors.scanner import ObstacleScanner
class TestScanner(unittest.TestCase):
    def test_clearest(self):
        s = ObstacleScanner(angles=[-60, 0, 60])
        s.record(-60, 20.0); s.record(0, 15.0); s.record(60, 150.0)
        best_ang, best_dist = s.get_clearest_direction()
        self.assertEqual(best_ang, 60)
if __name__ == '__main__': unittest.main()
