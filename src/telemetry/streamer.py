from collections import deque
class MockTelemetryStreamer:
    def __init__(self, size: int = 200): self.q = deque(maxlen=size)
    def transmit(self, pkt: str): self.q.append(pkt)
    def latest(self) -> str: return self.q[-1] if self.q else ""
    def count(self) -> int: return len(self.q)
