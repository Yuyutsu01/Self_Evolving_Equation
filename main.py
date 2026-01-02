import time

from model import step
from memory import Memory
import config
from visualize import LiveVisualizer


def main():
    # Initialize state and parameter
    x = config.X_INIT
    a = config.A_INIT

    # Initialize memory
    memory = Memory(config.MEMORY_WINDOW)

    # Initialize visualization
    visualizer = LiveVisualizer(
        max_steps=config.MAX_STEPS,
        x_limits=(config.X_MIN, config.X_MAX),
        a_limits=(config.A_MIN, config.A_MAX),
    )

    t = 0

    while True:
        # Update memory with current state
        memory.update(x)

        # Compute variance from memory
        variance = memory.variance()

        # Step the system
        x, a = step(
            x=x,
            a=a,
            variance=variance,
            epsilon=config.EPSILON,
            target_variance=config.TARGET_VARIANCE,
        )

        # Update visualization
        visualizer.update(t, x, a)

        t += 1

        # Small pause to control animation speed
        time.sleep(0.02)


if __name__ == "__main__":
    main()