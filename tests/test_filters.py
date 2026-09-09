import unittest
from src.sensors.filters import HybridFilter
class TestFilters(unittest.TestCase):
    def test_spike(self):
        hf = HybridFilter(size=5)
        for _ in range(4): hf.update(20.0)
        val = hf.update(400.0) # Injected false echo
        self.assertLess(val, 50.0)
if __name__ == '__main__': unittest.main()
