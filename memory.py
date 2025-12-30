from collections import deque
import numpy as np


class Memory:
    """
    Maintains a rolling window of recent state values
    and computes simple statistics over that window.
    """

    def __init__(self, window_size):
        self.window_size = window_size
        self.values = deque(maxlen=window_size)

    def update(self, x):
        """
        Add a new state value to memory.
        """
        self.values.append(x)

    def variance(self):
        """
        Compute variance over the stored values.
        Returns 0 if not enough data.
        """
        if len(self.values) < 2:
            return 0.0
        return float(np.var(self.values))

    def is_ready(self):
        """
        Check if memory window is fully populated.
        """
        return len(self.values) == self.window_size
