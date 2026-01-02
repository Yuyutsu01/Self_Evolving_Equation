import matplotlib.pyplot as plt
from collections import deque


class LiveVisualizer:
    def __init__(self, max_steps=500, x_limits=(0, 1), a_limits=(2.5, 4.0)):
        self.max_steps = max_steps

        # Buffers
        self.time = deque(maxlen=max_steps)
        self.x_values = deque(maxlen=max_steps)
        self.x_next_values = deque(maxlen=max_steps)
        self.a_values = deque(maxlen=max_steps)

        # Setup figure
        self.fig, self.axes = plt.subplots(3, 1, figsize=(8, 10))
        plt.ion()

        # --- Time Series Plot ---
        self.ax_time = self.axes[0]
        self.line_time, = self.ax_time.plot([], [], lw=2)
        self.ax_time.set_title("State Evolution x(t)")
        self.ax_time.set_xlim(0, max_steps)
        self.ax_time.set_ylim(*x_limits)
        self.ax_time.set_ylabel("x")

        # --- Phase Space Plot ---
        self.ax_phase = self.axes[1]
        self.scatter_phase = self.ax_phase.scatter([], [], s=10)
        self.ax_phase.set_title("Phase Space x(t) vs x(t+1)")
        self.ax_phase.set_xlim(*x_limits)
        self.ax_phase.set_ylim(*x_limits)
        self.ax_phase.set_xlabel("x(t)")
        self.ax_phase.set_ylabel("x(t+1)")

        # --- Parameter Plot ---
        self.ax_param = self.axes[2]
        self.line_param, = self.ax_param.plot([], [], color="orange", lw=2)
        self.ax_param.set_title("Parameter Evolution a(t)")
        self.ax_param.set_xlim(0, max_steps)
        self.ax_param.set_ylim(*a_limits)
        self.ax_param.set_xlabel("time")
        self.ax_param.set_ylabel("a")

        plt.tight_layout()
        plt.show()

    def update(self, t, x, a):
        # Store values
        self.time.append(t)
        self.x_values.append(x)
        self.a_values.append(a)

        # Phase space requires x(t+1)
        if len(self.x_values) > 1:
            self.x_next_values.append(self.x_values[-1])

        # --- Update Time Series ---
        self.line_time.set_data(self.time, self.x_values)
        self.ax_time.set_xlim(max(0, t - self.max_steps), t + 1)

        # --- Update Phase Space ---
        if len(self.x_next_values) > 0:
            self.scatter_phase.set_offsets(
                list(zip(self.x_values[:-1], self.x_next_values))
            )

        # --- Update Parameter Plot ---
        self.line_param.set_data(self.time, self.a_values)
        self.ax_param.set_xlim(max(0, t - self.max_steps), t + 1)

        # Redraw
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
