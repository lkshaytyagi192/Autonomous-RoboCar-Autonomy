from src.kinematics import DifferentialDriveKinematics
from src.motor_controller import MotorController
from src.navigation.fsm import NavigationFSM
class AutonomousRobotBrain:
    __slots__ = ('kin', 'motors', 'fsm')
    def __init__(self):
        self.kin = DifferentialDriveKinematics()
        self.motors = MotorController()
        self.fsm = NavigationFSM()
    def process_cycle(self, dist_cm: float, dt: float = 0.05) -> dict:
        state, v, w = self.fsm.update(dist_cm)
        wl, wr = self.kin.inverse_kinematics(v, w)
        sigs = self.motors.step(wl, wr, dt)
        return {"state": state.name, "cmd_v": v, "cmd_w": w, "motors": sigs}
    def e_stop(self): self.motors.e_stop = True
