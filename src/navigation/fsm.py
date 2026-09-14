from enum import Enum, auto
class RobotState(Enum):
    IDLE = auto()
    CRUISE = auto()
    OBSTACLE_DETECTED = auto()
    REVERSING = auto()

class NavigationFSM:
    def __init__(self, stop_cm: float = 15.0, warn_cm: float = 35.0):
        self.state = RobotState.IDLE
        self.stop_cm = stop_cm
        self.warn_cm = warn_cm
    def update(self, dist_cm: float) -> RobotState:
        if dist_cm <= self.stop_cm: self.state = RobotState.REVERSING
        elif dist_cm <= self.warn_cm: self.state = RobotState.OBSTACLE_DETECTED
        else: self.state = RobotState.CRUISE
        return self.state
