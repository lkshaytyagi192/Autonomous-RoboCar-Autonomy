import unittest
from src.encoder import EncoderTracker
class TestEncoder(unittest.TestCase):
    def test_ticks(self):
        enc = EncoderTracker()
        enc.update(100, 100)
        self.assertEqual(enc.ticks_l, 100)
if __name__ == '__main__': unittest.main()
