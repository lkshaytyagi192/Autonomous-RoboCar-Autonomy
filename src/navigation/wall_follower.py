from src.navigation.pid_controller import PIDController
class WallFollower:
    def __init__(self, desired_dist_cm: float = 30.0):
        self.target = desired_dist_cm
        self.pid = PIDController(kp=0.05, ki=0.005, kd=0.01, limits=(-1.5, 1.5))
    def compute_steering(self, cur_dist_cm: float, dt: float = 0.05) -> float:
        return self.pid.compute(self.target, cur_dist_cm, dt)
