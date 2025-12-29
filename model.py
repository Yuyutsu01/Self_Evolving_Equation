import numpy as np


def step_state(x, a):
    """
    Compute the next system state.

    x(t+1) = a(t) * x(t) * (1 - x(t))
    """
    return a * x * (1.0 - x)


def step_parameter(a, variance, epsilon, target_variance):
    """
    Update the parameter based on recent system behavior.

    a(t+1) = a(t) + ε * (Var(x_recent) - τ)
    """
    return a + epsilon * (variance - target_variance)


def step(x, a, variance, epsilon, target_variance):
    """
    Perform one full update step of the self-evolving system.

    Returns:
        x_next, a_next
    """
    x_next = step_state(x, a)
    a_next = step_parameter(a, variance, epsilon, target_variance)

    return x_next, a_next
