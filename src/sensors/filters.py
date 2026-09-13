from collections import deque
import numpy as np
class MovingAverageFilter:
    def __init__(self, size: int = 5): self.buf = deque(maxlen=size)
    def update(self, val: float) -> float:
        self.buf.append(val)
        return round(float(sum(self.buf) / len(self.buf)), 2)
    def reset(self): self.buf.clear()

class MedianFilter:
    def __init__(self, size: int = 5): self.buf = deque(maxlen=size)
    def update(self, val: float) -> float:
        self.buf.append(val)
        return round(float(np.median(self.buf)), 2)
    def reset(self): self.buf.clear()

class HybridFilter:
    def __init__(self, size: int = 5):
        self.med = MedianFilter(size)
        self.avg = MovingAverageFilter(size)
    def update(self, val: float) -> float:
        return self.avg.update(self.med.update(val))
    def reset(self):
        self.med.reset()
        self.avg.reset()
