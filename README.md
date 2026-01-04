# Self-Evolving Equation

A simple live simulation where a mathematical equation adapts its own parameters based on its recent behavior and is visualized through continuously updating graphs.

The goal of this project is to make an equation feel *alive* by giving it feedback, memory, and motion.

---

## Overview

Most equations evolve in time, but their rules remain fixed.

In this project, the **rule itself evolves**.

The system observes its own behavior over a short memory window and adjusts one of its parameters to regulate how stable or chaotic it becomes. This feedback loop creates ongoing, non-repeating dynamics that can be observed live.

There is:
- No machine learning
- No training data
- No optimization objective

All behavior emerges purely from mathematical feedback.

---

## Core Idea

The system consists of:
- A nonlinear equation that evolves a state over time
- A memory mechanism that tracks recent behavior
- An adaptation rule that modifies the equation’s parameter

Together, these form a closed loop:

state → memory → adaptation → updated rule → next state


This loop never stops.

---

## Mathematical Model

### State evolution
x(t+1) = a(t) · x(t) · (1 − x(t))


### Parameter adaptation
a(t+1) = a(t) + ε · (Var(x_recent) − τ)


Where:
- `x(t)` is the system state
- `a(t)` is a time-varying parameter
- `ε` controls how fast the parameter adapts
- `τ` is a target variability
- `Var(x_recent)` is the variance over a short rolling window

If the system becomes too stable, it increases complexity.  
If it becomes too chaotic, it self-regulates.

---

## Live Visualization (Planned)

When running the simulation, the following plots update continuously:

1. **Time Series** – evolution of the system state  
2. **Phase Space** – structure of the dynamics (`x(t)` vs `x(t+1)`)  
3. **Parameter Evolution** – how the equation’s rule changes over time  

These visualizations make both the motion and self-modification of the equation directly observable.

---

## Project Structure

self-evolving-equation/
│
├── main.py # Runs the live simulation (entry point)
├── model.py # Equation and parameter update logic
├── memory.py # Rolling memory and variance computation
├── visualize.py # Live animated plots
├── config.py # Initial values and constants
├── utils.py # Small helper functions
│
├── requirements.txt
└── README.md


The structure is intentionally simple and easy to follow.

---

## How to Run (Once Complete)

1. Clone the repository
git clone https://github.com/yuyustu01/self-evolving-equation.git

cd self-evolving-equation

2. Install dependencies
pip install -r requirements.txt


3. Run the simulation


A window will open showing live, moving graphs.

---

## Configuration

All system behavior can be adjusted from `config.py`, including:
- Initial state and parameter values
- Adaptation rate
- Target variability
- Memory window size
- Plot limits

Small changes can lead to very different dynamics.

---

## Purpose

This project exists to show that lifelike behavior can emerge from:
- Nonlinearity
- Feedback
- Memory

without intelligence, learning, or data.

It is meant to be explored visually and intuitively.

---

## License

MIT License.

---

## Closing Thought

This project is not about complexity.

It is about one idea taken seriously:

**An equation that changes itself.**
