import unittest
from src.sensors.filters import MovingAverageFilter
class TestLatency(unittest.TestCase):
    def test_step_response(self):
        f = MovingAverageFilter(size=3)
        f.update(10); f.update(20); res = f.update(30)
        self.assertEqual(res, 20.0)
if __name__ == '__main__': unittest.main()
