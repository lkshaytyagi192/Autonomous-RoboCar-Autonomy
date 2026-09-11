import unittest
from src.sensors.servo import ServoDriver
class TestServo(unittest.TestCase):
    def test_center(self):
        s = ServoDriver()
        duty = s.angle_to_duty(0)
        self.assertGreater(duty, 50)
if __name__ == '__main__': unittest.main()
