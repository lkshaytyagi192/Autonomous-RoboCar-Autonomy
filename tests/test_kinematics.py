import unittest
from src.kinematics import DifferentialDriveKinematics
class TestKinematics(unittest.TestCase):
    def setUp(self):
        self.kin = DifferentialDriveKinematics()
    def test_forward(self):
        v, w = self.kin.forward_kinematics(10.0, 10.0)
        self.assertGreater(v, 0.0)
        self.assertEqual(w, 0.0)
if __name__ == '__main__':
    unittest.main()
