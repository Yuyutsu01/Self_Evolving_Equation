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

