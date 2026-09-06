"""Differential Drive Kinematics."""
import numpy as np
class DifferentialDriveKinematics:
    def __init__(self, track_width: float = 0.145, wheel_radius: float = 0.0325, max_omega: float = 25.0):
        self.L = track_width
        self.r = wheel_radius
        self.max_omega = max_omega

    def forward_kinematics(self, w_l: float, w_r: float) -> tuple:
        v = self.r * (w_r + w_l) / 2.0
        w = self.r * (w_r - w_l) / self.L
        return round(float(v), 4), round(float(w), 4)

    def inverse_kinematics(self, target_v: float, target_w: float) -> tuple:
        w_l = (target_v - (target_w * self.L / 2.0)) / self.r
        w_r = (target_v + (target_w * self.L / 2.0)) / self.r
        max_val = max(abs(w_l), abs(w_r))
        if max_val > self.max_omega:
            factor = self.max_omega / max_val
            w_l *= factor
            w_r *= factor
        return round(float(w_l), 3), round(float(w_r), 3)

    def integrate_odometry(self, x: float, y: float, theta: float, v: float, w: float, dt: float) -> tuple:
        new_x = x + v * np.cos(theta) * dt
        new_y = y + v * np.sin(theta) * dt
        new_th = theta + w * dt
        return round(float(new_x), 4), round(float(new_y), 4), round(float(new_th), 4)
