class MotorController:
    def __init__(self, min_duty: int = 40, max_duty: int = 255, max_radps: float = 25.0, max_accel: float = 12.0):
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.max_radps = max_radps
        self.max_accel = max_accel
        self.cur_l = 0.0
        self.cur_r = 0.0
        self.e_stop = False
    def radps_to_pwm(self, radps: float) -> int:
        if abs(radps) < 0.1 or self.e_stop: return 0
        duty = int(self.min_duty + (abs(radps) / self.max_radps) * (self.max_duty - self.min_duty))
        return min(max(duty, self.min_duty), self.max_duty)
    def apply_slew(self, target: float, cur: float, dt: float) -> float:
        max_d = self.max_accel * dt
        d = target - cur
        return cur + (max_d if d > 0 else -max_d) if abs(d) > max_d else target
    def step(self, tgt_l: float, tgt_r: float, dt: float = 0.05) -> dict:
        if self.e_stop: return {"left": {"pwm": 0, "in1": 0, "in2": 0}, "right": {"pwm": 0, "in3": 0, "in4": 0}}
        self.cur_l = self.apply_slew(tgt_l, self.cur_l, dt)
        self.cur_r = self.apply_slew(tgt_r, self.cur_r, dt)
        return {
            "left": {"pwm": self.radps_to_pwm(self.cur_l), "in1": 1 if self.cur_l > 0 else 0, "in2": 1 if self.cur_l < 0 else 0},
            "right": {"pwm": self.radps_to_pwm(self.cur_r), "in3": 1 if self.cur_r > 0 else 0, "in4": 1 if self.cur_r < 0 else 0}
        }
