from src.sensors.ultrasonic import UltrasonicSensor
from src.sensors.scanner import ObstacleScanner
class SensorSuite:
    def __init__(self):
        self.ultrasonic = UltrasonicSensor()
        self.scanner = ObstacleScanner()
