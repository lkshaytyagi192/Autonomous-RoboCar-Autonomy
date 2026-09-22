import unittest
from src.telemetry.packet import TelemetryPacket
class TestTelem(unittest.TestCase):
    def test_pkt(self):
        s = TelemetryPacket.create("CRUISE", 50, 0.3, 0)
        d = TelemetryPacket.parse(s)
        self.assertEqual(d["state"], "CRUISE")
if __name__ == '__main__': unittest.main()
