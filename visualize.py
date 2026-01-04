import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class LiveVisualizer:
    def __init__(self, grid_size=(50, 50), z_limits=(0, 1)):
        self.nx, self.ny = grid_size

        # Spatial grid
        self.X, self.Y = np.meshgrid(
            np.linspace(0, 1, self.nx),
            np.linspace(0, 1, self.ny)
        )

        # Figure setup
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

        # Camera
        self.elev = 35
        self.azim = 45
        self.ax.view_init(elev=self.elev, azim=self.azim)

        plt.tight_layout()
        plt.show()

    def update(self, Z):
        # Remove previous surface safely
        if self.surface is not None:
            self.surface.remove()

        # Draw new surface
        self.surface = self.ax.plot_surface(
            self.X, self.Y, Z,
            cmap="inferno",
            linewidth=0,
            antialiased=True
        )

        # Gentle camera rotation
        self.azim = (self.azim + 0.4) % 360
        self.ax.view_init(elev=self.elev, azim=self.azim)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
