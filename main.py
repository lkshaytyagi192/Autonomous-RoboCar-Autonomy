import argparse, unittest
from sim.simulation_runner import run_simulation
from sim.raycaster import Raycaster
from sim.visualizer_gui import plot_arena

def main():
    parser = argparse.ArgumentParser(description="Autonomous RoboCar System")
    parser.add_argument("--mode", type=str, default="sim", choices=["sim", "test"])
    args = parser.parse_args()

    if args.mode == "test":
        print("[+] Running Complete Test Suite...")
        suite = unittest.defaultTestLoader.discover('tests')
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    else:
        print("[+] Launching 2D Autonomous Navigation Simulation...")
        ray = Raycaster()
        traj = run_simulation(steps=150)
        plot_arena(traj, ray.obstacles)
        print(f"[OK] Successfully executed {len(traj)} autonomous navigation cycles!")

if __name__ == '__main__':
    main()
