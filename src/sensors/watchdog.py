import time
class SensorWatchdog:
    def __init__(self, timeout_s: float = 1.0):
        self.timeout = timeout_s
        self.last_ts = time.time()
    def kick(self): self.last_ts = time.time()
    def is_healthy(self) -> bool: return (time.time() - self.last_ts) < self.timeout
