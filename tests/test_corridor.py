import unittest
from src.navigation.corridor_planner import CorridorPlanner
class TestCorridor(unittest.TestCase):
    def test_turn_right(self):
        cp = CorridorPlanner()
        w = cp.select_turn({-60: 10, -30: 15, 30: 80, 60: 90})
        self.assertGreater(w, 0)
if __name__ == '__main__': unittest.main()
