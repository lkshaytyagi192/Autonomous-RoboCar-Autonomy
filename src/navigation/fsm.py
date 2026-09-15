from enum import Enum, auto
class RobotState(Enum):
    IDLE = auto()
    CRUISE = auto()
    OBSTACLE_DETECTED = auto()
    REVERSING = auto()

class NavigationFSM:
    def __init__(self, stop_cm: float = 15.0, warn_cm: float = 35.0, speed: float = 0.35):
        self.state = RobotState.IDLE
        self.stop_cm = stop_cm
        self.warn_cm = warn_cm
        self.speed = speed
    def update(self, dist_cm: float) -> tuple:
        if dist_cm <= self.stop_cm:
            self.state = RobotState.REVERSING
            return self.state, -0.2, 0.0
        elif dist_cm <= self.warn_cm:
            self.state = RobotState.OBSTACLE_DETECTED
            return self.state, 0.0, 1.8
        else:
            self.state = RobotState.CRUISE
            return self.state, self.speed, 0.0
