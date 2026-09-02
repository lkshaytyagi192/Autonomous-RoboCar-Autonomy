"""Differential Drive Kinematics."""
class DifferentialDriveKinematics:
    def __init__(self, track_width: float = 0.145, wheel_radius: float = 0.0325):
        self.L = track_width
        self.r = wheel_radius

    def forward_kinematics(self, w_l: float, w_r: float) -> tuple:
        v = self.r * (w_r + w_l) / 2.0
        w = self.r * (w_r - w_l) / self.L
        return round(float(v), 4), round(float(w), 4)

    def inverse_kinematics(self, target_v: float, target_w: float) -> tuple:
        v_l = target_v - (target_w * self.L / 2.0)
        v_r = target_v + (target_w * self.L / 2.0)
        return round(float(v_l / self.r), 3), round(float(v_r / self.r), 3)
