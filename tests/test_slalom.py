import unittest
from sim.raycaster import Raycaster
from sim.simulation_runner import run_simulation
class TestSlalom(unittest.TestCase):
    def test_slalom(self):
        traj = run_simulation(60)
        self.assertEqual(len(traj), 60)
if __name__ == '__main__': unittest.main()
