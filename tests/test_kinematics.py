import unittest
from src.kinematics import DifferentialDriveKinematics
class TestKinematics(unittest.TestCase):
    def setUp(self):
        self.kin = DifferentialDriveKinematics()
    def test_forward(self):
        v, w = self.kin.forward_kinematics(10.0, 10.0)
        self.assertGreater(v, 0.0)
        self.assertEqual(w, 0.0)
    def test_spin(self):
        v, w = self.kin.forward_kinematics(-10.0, 10.0)
        self.assertEqual(v, 0.0)
        self.assertGreater(w, 0.0)
    def test_inverse_recovery(self):
        w_l, w_r = self.kin.inverse_kinematics(0.4, 0.0)
        self.assertEqual(w_l, w_r)
if __name__ == '__main__':
    unittest.main()
