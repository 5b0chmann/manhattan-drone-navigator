# 🚁 Manhattan Drone Navigator

A Reinforcement Learning project that teaches an autonomous drone to navigate through Manhattan using OpenStreetMap, graph theory and Deep Reinforcement Learning.

---

## Vision

The long-term goal is to create a 3D navigation environment in which an autonomous drone learns optimal flight paths through Manhattan while avoiding buildings and no-fly zones.

```text
OpenStreetMap
        +
Street Network
        +
Buildings
        +
Building Heights
        +
Reinforcement Learning
        =
Manhattan Drone Navigator
```

---

## Project Motivation

The idea originated from the Manhattan distance metric:

```math
d = |x₁ - x₂| + |y₁ - y₂|
```

Since Manhattan is organized in a nearly grid-like structure, it provides a natural environment for reinforcement learning experiments.

The project evolves from a simple Grid World to a realistic 3D urban airspace simulation.

---

## Development Roadmap

### ✅ Phase 1 – Reinforcement Learning Fundamentals

Topics:

- Markov Decision Process (MDP)
- Reward Functions
- Q-Learning
- Deep Q-Networks (DQN)
- PPO
- Exploration vs Exploitation

---

### ⬜ Phase 2 – Manhattan Grid World

First RL environment:

Actions:

```text
NORTH
SOUTH
EAST
WEST
```

State:

```python
(x, y)
```

Reward:

```python
reward = old_distance - new_distance
```

using Manhattan distance.

---

### ⬜ Phase 3 – Real Manhattan Street Network

Transition from:

```text
Grid World
```

to

```text
Real Street Network
```

Technologies:

- OpenStreetMap
- OSMnx
- NetworkX

Research question:

```text
A*
vs
RL Agent
```

---

### ⬜ Phase 4 – Building Obstacles

Buildings are introduced as no-fly zones.

Example:

```text
########
#      #
# BLDG #
#      #
########
```

The drone must find alternative routes.

---

### ⬜ Phase 5 – Building Heights

Additional data sources:

- OpenStreetMap
- NYC Open Data
- GIS Datasets
- Kaggle

New constraint:

```text
