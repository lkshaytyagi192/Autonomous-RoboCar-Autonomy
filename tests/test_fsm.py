import unittest
from src.navigation.fsm import NavigationFSM, RobotState
class TestFSM(unittest.TestCase):
    def test_fsm(self):
        f = NavigationFSM()
        s, v, w = f.update(100)
        self.assertEqual(s, RobotState.CRUISE)
        s, v, w = f.update(20)
        self.assertEqual(s, RobotState.EVADING)
if __name__ == '__main__': unittest.main()
