import unittest
from src.navigation.pid_controller import PIDController
class TestReset(unittest.TestCase):
    def test_reset(self):
        p = PIDController(1, 1, 0)
        p.compute(10, 0, 0.1)
        p.reset()
        self.assertEqual(p.integral, 0.0)
if __name__ == '__main__': unittest.main()
