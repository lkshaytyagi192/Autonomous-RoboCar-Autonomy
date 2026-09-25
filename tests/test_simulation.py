import unittest
from sim.simulation_runner import run_simulation
class TestSim(unittest.TestCase):
    def test_run(self):
        traj = run_simulation(50)
        self.assertEqual(len(traj), 50)
        self.assertGreater(traj[-1][0], 0)
if __name__ == '__main__': unittest.main()
