class ServoDriver:
    def angle_to_duty(self, angle_deg: int) -> int:
        angle = min(max(angle_deg, -90), 90) + 90 # Map [-90, 90] to [0, 180]
        # Standard 50Hz servo: 0.5ms (2.5%) to 2.5ms (12.5%) duty
        return int(26 + (angle / 180.0) * 102)
