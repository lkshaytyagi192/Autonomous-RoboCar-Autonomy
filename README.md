# 🏎️ Autonomous-RoboCar-Autonomy
### Embedded Mobile Robotics Navigation & Obstacle Avoidance Stack

[![Language: Python & C++](https://img.shields.io/badge/Language-Python%20%7C%20C%2B%2B-blue.svg)](#)
[![Microcontroller: ESP32](https://img.shields.io/badge/Hardware-ESP32%20Dual--Core-red.svg)](#)
[![Architecture: FSM + PID](https://img.shields.io/badge/Control-FSM%20%2B%20PID-green.svg)](#)
[![Status: Production Ready](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](#)

A modular, embedded autonomous navigation framework for 2-wheel differential drive robotic vehicles.

---

## 📌 Architecture Overview

```mermaid
graph TD
    A["HC-SR04 Ultrasonic Sensor"] --> B["Median & Moving Average Filter"]
    B --> C["Corridor Planner & Radar Sweep"]
    C --> D["Finite State Machine (FSM)"]
    D --> E["PID Heading Controller"]
    E --> F["Differential Drive Kinematics"]
    F --> G["L298N PWM Motor Driver"]
    G --> H["Physical Wheels / Propulsion"]
```
