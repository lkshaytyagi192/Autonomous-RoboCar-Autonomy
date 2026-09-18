import unittest
from src.navigation.pid_controller import PIDController
class TestPID(unittest.TestCase):
    def test_p(self):
        p = PIDController(1.0, 0, 0, limits=(-10, 10))
        self.assertEqual(p.compute(10, 6, 0.1), 4.0)
    def test_windup(self):
        p = PIDController(1, 1, 0, limits=(-5, 5))
        for _ in range(50): p.compute(100, 0, 0.1)
        self.assertLessEqual(abs(p.integral), 10.0)
if __name__ == '__main__': unittest.main()
