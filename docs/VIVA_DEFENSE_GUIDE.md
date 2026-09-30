# 🎓 Viva & Technical Defense Guide: Autonomous RoboCar

### Q1: How does differential drive kinematics work?
- By varying individual velocities of left ($v_L$) and right ($v_R$) wheels, we control linear speed $v = (v_R + v_L)/2$ and yaw rate $\omega = (v_R - v_L)/L$.

### Q2: Why use a hybrid filter (Median + Moving Average)?
- A Median filter rejects instantaneous impulse spikes from false acoustic reflections, while a Moving Average filter smooths high-frequency electrical jitter.

### Q3: What is Integral Anti-Windup in the PID controller?
- Clamping the integrator prevents huge overshoot once an obstacle has cleared.
