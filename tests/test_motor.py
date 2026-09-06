import unittest
from src.motor_controller import MotorController
class TestMotor(unittest.TestCase):
    def test_ramp(self):
        m = MotorController(max_accel=10.0)
        cmd = m.step(20.0, 20.0, dt=0.1)
        self.assertLess(m.cur_l, 20.0)
        self.assertAlmostEqual(m.cur_l, 1.0, places=2)
if __name__ == '__main__': unittest.main()
