import numpy as np
def compute_path_length(trajectory: list) -> float:
    pts = np.array([(p[0], p[1]) for p in trajectory])
    diffs = np.diff(pts, axis=0)
    return round(float(np.sum(np.hypot(diffs[:, 0], diffs[:, 1]))), 3)
