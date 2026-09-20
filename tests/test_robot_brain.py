import unittest
from src.robot_brain import AutonomousRobotBrain
class TestBrain(unittest.TestCase):
    def test_cycle(self):
        b = AutonomousRobotBrain()
        res = b.process_cycle(100.0)
        self.assertEqual(res["state"], "CRUISE")
        self.assertGreater(res["cmd_v"], 0.0)
if __name__ == '__main__': unittest.main()
