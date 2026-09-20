import unittest
from src.robot_brain import AutonomousRobotBrain
class TestEStop(unittest.TestCase):
    def test_estop(self):
        b = AutonomousRobotBrain()
        b.e_stop()
        res = b.process_cycle(100.0)
        self.assertEqual(res["motors"]["left"]["pwm"], 0)
if __name__ == '__main__': unittest.main()
