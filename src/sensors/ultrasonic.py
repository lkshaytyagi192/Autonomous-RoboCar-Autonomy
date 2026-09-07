class UltrasonicSensor:
    def __init__(self, min_cm: float = 2.0, max_cm: float = 400.0):
        self.min_cm = min_cm
        self.max_cm = max_cm
    def pulse_to_cm(self, echo_us: float) -> float:
        if echo_us <= 0 or echo_us >= 25000: return self.max_cm
        dist = (echo_us * 0.0343) / 2.0
        return round(float(min(max(dist, self.min_cm), self.max_cm)), 2)
