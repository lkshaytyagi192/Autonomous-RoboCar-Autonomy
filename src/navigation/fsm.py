from enum import Enum, auto
import time
class RobotState(Enum):
    IDLE = auto()
    CRUISE = auto()
    OBSTACLE_DETECTED = auto()
    EVADING = auto()
    REVERSING = auto()

class NavigationFSM:
    def __init__(self, stop_cm: float = 15.0, warn_cm: float = 35.0, speed: float = 0.35):
        self.state = RobotState.IDLE
        self.stop_cm = stop_cm
        self.warn_cm = warn_cm
        self.speed = speed
        self.history = []
    def log(self, prev, cur):
        if prev != cur: self.history.append((round(time.time(), 2), prev.name, cur.name))
    def update(self, dist_cm: float, best_w: float = 1.8) -> tuple:
        prev = self.state
        if dist_cm <= self.stop_cm:
            self.state = RobotState.REVERSING
            cmd = (-0.2, 0.0)
        elif dist_cm <= self.warn_cm:
            self.state = RobotState.EVADING
            cmd = (0.05, best_w)
        else:
            self.state = RobotState.CRUISE
            cmd = (self.speed, 0.0)
        self.log(prev, self.state)
        return self.state, cmd[0], cmd[1]
