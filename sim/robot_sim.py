import numpy as np
class SimulatedCar:
    def __init__(self, x: float = 0, y: float = 0, th: float = 0):
        self.x = x; self.y = y; self.th = th
    def step(self, v: float, w: float, dt: float = 0.05):
        self.x += v * np.cos(self.th) * dt
        self.y += v * np.sin(self.th) * dt
        self.th = np.arctan2(np.sin(self.th + w * dt), np.cos(self.th + w * dt))
