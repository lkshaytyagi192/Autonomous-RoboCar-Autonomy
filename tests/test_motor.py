import unittest
from src.motor_controller import MotorController
class TestMotor(unittest.TestCase):
    def setUp(self): self.m = MotorController()
    def test_brake(self):
        res = self.m.emergency_stop()
        self.assertEqual(res["left"]["pwm"], 0)
    def test_forward(self):
        res = self.m.compute_motor_commands(10.0, 10.0)
        self.assertEqual(res["left"]["in1"], 1)
if __name__ == '__main__': unittest.main()
