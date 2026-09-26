import matplotlib.pyplot as plt
import matplotlib.patches as patches
def plot_arena(trajectory, obstacles):
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=160)
    ax.set_title("Autonomous RoboCar 2D Navigation Simulator", fontsize=12, fontweight='bold')
    ax.set_xlabel("X Metric Position (Meters)", fontweight='bold')
    ax.set_ylabel("Y Metric Position (Meters)", fontweight='bold')
    for ox, oy, r in obstacles:
        ax.add_patch(patches.Circle((ox, oy), r, color='#d62728', alpha=0.65, label="Obstacle" if ox == obstacles[0][0] else ""))
    xs = [p[0] for p in trajectory]
    ys = [p[1] for p in trajectory]
    ax.plot(xs, ys, color='#1f77b4', linewidth=2.4, label="Autonomous Path")
    ax.scatter([xs[0]], [ys[0]], color='#2ca02c', s=120, edgecolors='black', label="Start Pose", zorder=5)
    ax.scatter([xs[-1]], [ys[-1]], color='#9467bd', s=120, edgecolors='black', label="Final Pose", zorder=5)
    ax.text(0.02, 0.95, f"Steps: {len(trajectory)} | Status: Navigation Active",
            transform=ax.transAxes, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig("sim/simulation_trajectory.png", dpi=160)
    plt.close()
