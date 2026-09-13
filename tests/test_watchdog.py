import unittest, time
from src.sensors.watchdog import SensorWatchdog
class TestWatchdog(unittest.TestCase):
    def test_timeout(self):
        w = SensorWatchdog(timeout_s=0.1)
        time.sleep(0.15)
        self.assertFalse(w.is_healthy())
if __name__ == '__main__': unittest.main()
