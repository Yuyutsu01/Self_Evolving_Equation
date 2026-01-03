import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class LiveVisualizer:
    def __init__(self, grid_size=(50, 50), z_limits=(0, 1)):
        self.nx, self.ny = grid_size

        # Create grid
        self.X, self.Y = np.meshgrid(
            np.linspace(0, 1, self.nx),
            np.linspace(0, 1, self.ny)
        )

        # Setup figure
        self.fig = plt.figure(figsize=(10, 7))
        self.ax = self.fig.add_subplot(111, projection="3d")
        plt.ion()

        # Initial surface
        self.Z = np.zeros((self.nx, self.ny))
        self.surface = self.ax.plot_surface(
            self.X, self.Y, self.Z,
            cmap="inferno",
            linewidth=0,
            antialiased=True
        )

        self.ax.set_zlim(*z_limits)
        self.ax.set_title("Self-Evolving Spatial Equation")
        self.ax.set_xlabel("Space X")
        self.ax.set_ylabel("Space Y")
        self.ax.set_zlabel("State")

        # Camera polish
        self.ax.view_init(elev=35, azim=45)

        plt.tight_layout()
        plt.show()

    def update(self, Z):
        self.ax.collections.clear()

        self.surface = self.ax.plot_surface(
            self.X, self.Y, Z,
            cmap="inferno",
            linewidth=0,
            antialiased=True
        )

        # Slow camera rotation for life-like feel
        self.ax.view_init(
            elev=35,
            azim=(self.ax.azim + 0.5) % 360
        )

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
