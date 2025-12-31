# ===============================
# System Initial Conditions
# ===============================

# Initial state (must be in (0, 1) for logistic-style dynamics)
X_INIT = 0.4

# Initial parameter value
A_INIT = 3.2


# Adaptation Settings
# ===============================

# Adaptation rate (ε)
EPSILON = 0.05

# Target variance (τ)
TARGET_VARIANCE = 0.02



# Memory Settings
# ===============================

# Number of past values used to compute variance
MEMORY_WINDOW = 50


# Simulation Settings

# Total steps to keep in visualization buffers
MAX_STEPS = 500


# Visualization Limits


# Time series plot limits
X_MIN = 0.0
X_MAX = 1.0

# Parameter plot limits
A_MIN = 2.5
A_MAX = 4.0
