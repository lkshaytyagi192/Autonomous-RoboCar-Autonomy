import unittest
from sim.raycaster import Raycaster
class TestMargin(unittest.TestCase):
    def test_ray(self):
        r = Raycaster()
        d = r.cast_ray(0, 0, 0)
        self.assertGreater(d, 0)
if __name__ == '__main__': unittest.main()
