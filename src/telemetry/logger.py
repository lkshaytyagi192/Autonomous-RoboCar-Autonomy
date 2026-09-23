import csv
class TelemetryLogger:
    def __init__(self, path: str = "telemetry.csv"):
        self.f = open(path, "w", newline="")
        self.w = csv.writer(self.f)
        self.w.writerow(["ts", "state", "dist", "v", "w"])
    def log(self, ts, s, d, v, w): self.w.writerow([ts, s, d, v, w]); self.f.flush()
    def close(self): self.f.close()
