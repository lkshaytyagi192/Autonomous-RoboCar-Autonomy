#ifndef KINEMATICS_H
#define KINEMATICS_H
struct WheelSpeeds { float left; float right; };
class Kinematics {
    float L, r;
public:
    Kinematics(float track = 0.145f, float radius = 0.0325f) : L(track), r(radius) {}
    WheelSpeeds compute(float v, float w) {
        return { (v - w * L / 2.0f) / r, (v + w * L / 2.0f) / r };
    }
};
#endif
