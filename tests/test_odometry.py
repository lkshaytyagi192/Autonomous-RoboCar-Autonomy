import unittest
from src.kinematics import DifferentialDriveKinematics
class TestOdom(unittest.TestCase):
    def test_pose(self):
        k = DifferentialDriveKinematics()
        x, y, th = k.integrate_odometry(0, 0, 0, 1.0, 0.0, 0.5)
        self.assertEqual(x, 0.5)
        self.assertEqual(y, 0.0)
if __name__ == '__main__': unittest.main()
