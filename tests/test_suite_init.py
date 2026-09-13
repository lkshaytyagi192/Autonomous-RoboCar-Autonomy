import unittest
from src.sensors.sensor_suite import SensorSuite
class TestSuite(unittest.TestCase):
    def test_init(self):
        ss = SensorSuite()
        self.assertIsNotNone(ss.ultrasonic)
if __name__ == '__main__': unittest.main()
