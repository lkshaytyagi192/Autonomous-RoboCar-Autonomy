import unittest
from src.sensors.ultrasonic import UltrasonicSensor
class TestSensors(unittest.TestCase):
    def test_distance(self):
        s = UltrasonicSensor()
        self.assertAlmostEqual(s.pulse_to_cm(1000), 17.15, places=1)
if __name__ == '__main__': unittest.main()
