class ObstacleScanner:
    def __init__(self, angles: list = None):
        self.angles = angles if angles else [-60, -30, 0, 30, 60]
        self.profile = {a: 400.0 for a in self.angles}
    def record(self, angle: int, dist: float):
        if angle in self.profile: self.profile[angle] = dist
    def get_clearest_direction(self) -> tuple:
        best = max(self.profile, key=self.profile.get)
        return best, self.profile[best]
