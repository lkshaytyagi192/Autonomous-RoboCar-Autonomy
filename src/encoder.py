class EncoderTracker:
    def __init__(self, cpr: int = 360):
        self.cpr = cpr
        self.ticks_l = 0
        self.ticks_r = 0
    def update(self, dl: int, dr: int):
        self.ticks_l += dl
        self.ticks_r += dr
