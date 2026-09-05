class MotorController:
    def __init__(self, min_duty: int = 40, max_duty: int = 255, max_radps: float = 25.0):
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.max_radps = max_radps
        self.e_stop = False
    def radps_to_pwm(self, radps: float) -> int:
        if abs(radps) < 0.1 or self.e_stop: return 0
        duty = int(self.min_duty + (abs(radps) / self.max_radps) * (self.max_duty - self.min_duty))
        return min(max(duty, self.min_duty), self.max_duty)
    def emergency_stop(self):
        self.e_stop = True
        return {"left": {"pwm": 0, "in1": 0, "in2": 0}, "right": {"pwm": 0, "in3": 0, "in4": 0}}
    def compute_motor_commands(self, left: float, right: float) -> dict:
        if self.e_stop: return self.emergency_stop()
        return {
            "left": {"pwm": self.radps_to_pwm(left), "in1": 1 if left > 0 else 0, "in2": 1 if left < 0 else 0},
            "right": {"pwm": self.radps_to_pwm(right), "in3": 1 if right > 0 else 0, "in4": 1 if right < 0 else 0}
        }
