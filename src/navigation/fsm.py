from enum import Enum, auto
class RobotState(Enum):
    IDLE = auto()
    CRUISE = auto()
    OBSTACLE_DETECTED = auto()
    REVERSING = auto()
