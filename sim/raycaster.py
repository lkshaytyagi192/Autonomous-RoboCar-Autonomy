import numpy as np
class Raycaster:
    def __init__(self, obstacles: list = None):
        self.obstacles = obstacles if obstacles else [(2.0, 0.2, 0.4), (4.0, -0.3, 0.5)]
    def cast_ray(self, rx: float, ry: float, rth: float, max_r: float = 4.0) -> float:
        min_d = max_r
        for ox, oy, r in self.obstacles:
            dx, dy = ox - rx, oy - ry
            dist = np.hypot(dx, dy)
            b = np.arctan2(dy, dx) - rth
            b = (b + np.pi) % (2 * np.pi) - np.pi
            if abs(b) < 0.26:
                d = dist - r
                if 0 < d < min_d: min_d = d
        return round(float(min_d * 100.0), 1)
