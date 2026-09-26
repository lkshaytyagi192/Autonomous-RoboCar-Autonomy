import matplotlib.pyplot as plt
import matplotlib.patches as patches
def plot_arena(trajectory, obstacles):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title("Autonomous RoboCar Navigation Simulation")
    for ox, oy, r in obstacles:
        ax.add_patch(patches.Circle((ox, oy), r, color='crimson', alpha=0.6))
    xs = [p[0] for p in trajectory]
    ys = [p[1] for p in trajectory]
    ax.plot(xs, ys, 'b-', label="Trajectory")
    ax.scatter([xs[0]], [ys[0]], color='g', label="Start")
    ax.scatter([xs[-1]], [ys[-1]], color='purple', label="End")
    ax.legend()
    plt.savefig("sim/simulation_trajectory.png")
    plt.close()
