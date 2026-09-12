import numpy as np
class ObstacleScanner:
    def __init__(self, angles: list = None):
        self.angles = angles if angles else [-60, -30, 0, 30, 60]
        self.profile = {a: 400.0 for a in self.angles}
    def record(self, angle: int, dist: float):
        if angle in self.profile: self.profile[angle] = dist
    def get_clearest_direction(self) -> tuple:
        best = max(self.profile, key=self.profile.get)
        return best, self.profile[best]
    def to_points(self) -> list:
        angs = np.deg2rad(list(self.profile.keys()))
        dists = np.array(list(self.profile.values())) / 100.0
        xs = dists * np.cos(angs)
        ys = dists * np.sin(angs)
        return [(round(float(x), 3), round(float(y), 3)) for x, y in zip(xs, ys)]
