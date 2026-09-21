import json, time
class TelemetryPacket:
    @staticmethod
    def create(state: str, dist: float, v: float, w: float, batt: float = 7.4) -> str:
        return json.dumps({
            "ts": round(time.time(), 3), "state": state, "dist_cm": round(dist, 1),
            "v_mps": round(v, 2), "w_radps": round(w, 2), "batt_v": round(batt, 2)
        })
