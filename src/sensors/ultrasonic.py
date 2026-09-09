from src.sensors.filters import HybridFilter
class UltrasonicSensor:
    def __init__(self, min_cm: float = 2.0, max_cm: float = 400.0):
        self.min_cm = min_cm
        self.max_cm = max_cm
        self.filter = HybridFilter(size=5)
    def pulse_to_cm(self, echo_us: float) -> float:
        if echo_us <= 0 or echo_us >= 25000: dist = self.max_cm
        else: dist = (echo_us * 0.0343) / 2.0
        dist = min(max(dist, self.min_cm), self.max_cm)
        return self.filter.update(dist)
