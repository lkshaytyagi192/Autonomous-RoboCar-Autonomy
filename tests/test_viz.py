import unittest, os
from sim.simulation_runner import run_simulation
from sim.raycaster import Raycaster
from sim.visualizer_gui import plot_arena
class TestViz(unittest.TestCase):
    def test_viz(self):
        r = Raycaster()
        traj = run_simulation(20)
        plot_arena(traj, r.obstacles)
        self.assertTrue(os.path.exists("sim/simulation_trajectory.png"))
if __name__ == '__main__': unittest.main()
