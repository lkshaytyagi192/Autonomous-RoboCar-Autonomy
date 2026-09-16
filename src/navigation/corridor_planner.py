import numpy as np
class CorridorPlanner:
    def __init__(self, threshold_cm: float = 40.0):
        self.th = threshold_cm
    def select_turn(self, scan_data: dict) -> float:
        l = np.mean([scan_data.get(-60, 0), scan_data.get(-30, 0)])
        r = np.mean([scan_data.get(60, 0), scan_data.get(30, 0)])
        if l > r and l > self.th: return -1.5
        elif r > self.th: return 1.5
        return 2.5
