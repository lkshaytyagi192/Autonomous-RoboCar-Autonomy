class PIDController:
    def __init__(self, kp: float, ki: float, kd: float, limits: tuple = (-2.0, 2.0)):
        self.kp = kp; self.ki = ki; self.kd = kd
        self.min_o, self.max_o = limits
        self.prev_e = 0.0; self.integral = 0.0
    def compute(self, target: float, measured: float, dt: float) -> float:
        if dt <= 0: return 0.0
        e = target - measured
        self.integral += e * dt
        max_i = self.max_o / (self.ki if self.ki != 0 else 1.0)
        self.integral = min(max(self.integral, -max_i), max_i)
        d = (e - self.prev_e) / dt
        self.prev_e = e
        out = (self.kp * e) + (self.ki * self.integral) + (self.kd * d)
        return round(float(min(max(out, self.min_o), self.max_o)), 3)
