import matplotlib.pyplot as plt
import matplotlib.patches as patches
def plot_arena(trajectory, obstacles):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title("Autonomous RoboCar Navigation Simulation", fontweight='bold')
    for ox, oy, r in obstacles:
        ax.add_patch(patches.Circle((ox, oy), r, color='crimson', alpha=0.6))
    xs = [p[0] for p in trajectory]
    ys = [p[1] for p in trajectory]
    ax.plot(xs, ys, 'b-', linewidth=2, label="Traveled Path")
    ax.scatter([xs[0]], [ys[0]], color='green', s=100, label="Start Pose")
    ax.scatter([xs[-1]], [ys[-1]], color='purple', s=100, label="End Pose")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    plt.tight_layout()
    plt.savefig("sim/simulation_trajectory.png")
    plt.close()
