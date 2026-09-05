class MotorController:
    def __init__(self, min_duty: int = 40, max_duty: int = 255, max_radps: float = 25.0):
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.max_radps = max_radps
    def radps_to_pwm(self, radps: float) -> int:
        if abs(radps) < 0.1: return 0
        duty = int(self.min_duty + (abs(radps) / self.max_radps) * (self.max_duty - self.min_duty))
        return min(max(duty, self.min_duty), self.max_duty)
