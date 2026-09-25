from sim.robot_sim import SimulatedCar
from sim.raycaster import Raycaster
from src.robot_brain import AutonomousRobotBrain
def run_simulation(steps: int = 100):
    car = SimulatedCar()
    ray = Raycaster()
    brain = AutonomousRobotBrain()
    traj = []
    for _ in range(steps):
        d = ray.cast_ray(car.x, car.y, car.th)
        res = brain.process_cycle(d)
        car.step(res["cmd_v"], res["cmd_w"])
        traj.append((car.x, car.y, car.th, res["state"]))
    return traj
