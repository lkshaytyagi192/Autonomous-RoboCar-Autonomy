import unittest
from src.navigation.recovery import StuckRecovery
class TestRec(unittest.TestCase):
    def test_rec(self):
        r = StuckRecovery()
        v, w = r.get_recovery_action()
        self.assertLess(v, 0)
if __name__ == '__main__': unittest.main()
