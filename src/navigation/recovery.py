class StuckRecovery:
    def __init__(self, max_attempts: int = 3):
        self.attempts = 0
        self.max_attempts = max_attempts
    def get_recovery_action(self) -> tuple:
        self.attempts += 1
        return -0.25, 2.8 # Fast reverse-pivot
