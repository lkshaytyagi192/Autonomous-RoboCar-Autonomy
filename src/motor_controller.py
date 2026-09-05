class MotorController:
    def __init__(self, min_duty: int = 40, max_duty: int = 255):
        self.min_duty = min_duty
        self.max_duty = max_duty
