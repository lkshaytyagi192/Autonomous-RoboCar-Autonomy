import numpy as np
def normalize_angle(theta: float) -> float:
    return np.arctan2(np.sin(theta), np.cos(theta))
