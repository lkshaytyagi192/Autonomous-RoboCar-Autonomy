import unittest
from src.telemetry.streamer import MockTelemetryStreamer
class TestStream(unittest.TestCase):
    def test_stream(self):
        s = MockTelemetryStreamer(size=2)
        s.transmit("p1"); s.transmit("p2"); s.transmit("p3")
        self.assertEqual(s.latest(), "p3")
if __name__ == '__main__': unittest.main()
