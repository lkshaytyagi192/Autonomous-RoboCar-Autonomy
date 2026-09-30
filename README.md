# 🏎️ Autonomous-RoboCar-Autonomy
### Embedded Mobile Robotics Navigation & Obstacle Avoidance Stack

[![Language: Python & C++](https://img.shields.io/badge/Language-Python%20%7C%20C%2B%2B-blue.svg)](#)
[![Microcontroller: ESP32](https://img.shields.io/badge/Hardware-ESP32%20Dual--Core-red.svg)](#)
[![Architecture: FSM + PID](https://img.shields.io/badge/Control-FSM%20%2B%20PID-green.svg)](#)
[![Status: Production Ready](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](#)

A modular, embedded autonomous navigation framework for 2-wheel differential drive robotic vehicles. Features forward/inverse kinematics, hybrid sensor noise filtering, multi-angle radar corridor sweeping, a finite state machine (FSM), and closed-loop PID control.

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

---

## ⚡ Quickstart

### 1. Run Automated Unit Tests
```bash
python main.py --mode test
```

### 2. Run 2D Autonomous Navigation Simulation
```bash
python main.py --mode sim
```

---

## 👨‍💻 Author
**LKSHAY TYAGI**  
*SRM Institute of Science and Technology, Delhi-NCR*  
*Specialization: Autonomous Systems, Robotics & Embedded Intelligence*
