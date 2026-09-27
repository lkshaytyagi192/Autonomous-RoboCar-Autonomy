import unittest
from sim.metrics import compute_path_length
class TestMetrics(unittest.TestCase):
    def test_length(self):
        traj = [(0, 0), (1, 0), (1, 1)]
        self.assertEqual(compute_path_length(traj), 2.0)
if __name__ == '__main__': unittest.main()
