import time
import numpy as np

import config
from visualize import LiveVisualizer


# ===============================
# Spatial Configuration
# ===============================

GRID_SIZE = (50, 50)      # Spatial resolution
DIFFUSION = 0.05          # Spatial coupling strength
SLEEP_TIME = 0.03         # Controls animation speed


# ===============================
# Helper: Discrete Laplacian
# ===============================

def laplacian(Z):
    """
    Compute a 2D discrete Laplacian using periodic boundaries.
    """
    return (
        -4 * Z
        + np.roll(Z, 1, axis=0)
        + np.roll(Z, -1, axis=0)
        + np.roll(Z, 1, axis=1)
        + np.roll(Z, -1, axis=1)
    )


# ===============================
# Main Loop
# ===============================

def main():
    # Initial spatial state
    X = np.random.rand(*GRID_SIZE)

    # Global adaptive parameter
    a = config.A_INIT

    # Visualization
    visualizer = LiveVisualizer(
        grid_size=GRID_SIZE,
        z_limits=(config.X_MIN, config.X_MAX)
    )

    while True:
        # --- Spatial State Update ---
        X = a * X * (1.0 - X) + DIFFUSION * laplacian(X)
        X = np.clip(X, config.X_MIN, config.X_MAX)

        # --- Measure Global Behavior ---
        variance = np.var(X)

        # --- Adapt Parameter ---
        a = a + config.EPSILON * (variance - config.TARGET_VARIANCE)
        a = np.clip(a, config.A_MIN, config.A_MAX)

        # --- Visualization ---
        visualizer.update(X)

        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
