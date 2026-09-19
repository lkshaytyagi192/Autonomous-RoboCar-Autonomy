import unittest
from src.navigation.wall_follower import WallFollower
class TestWF(unittest.TestCase):
    def test_wf(self):
        wf = WallFollower(30.0)
        w = wf.compute_steering(50.0, 0.1)
        self.assertNotEqual(w, 0.0)
if __name__ == '__main__': unittest.main()
