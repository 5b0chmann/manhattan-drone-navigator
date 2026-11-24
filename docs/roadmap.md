# Project Roadmap

This document outlines the planned evolution of the Manhattan Drone Navigator project.

---

# Vision

Build an autonomous drone navigation system that learns how to fly through Manhattan using Reinforcement Learning and real-world geographic data.

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

# Current Status

## Completed

- ✅ Manhattan Grid World
- ✅ Manhattan Distance Reward
- ✅ ASCII Environment Rendering
- ✅ Random Agent
- ✅ Q-Learning Agent
- ✅ Q-Table Implementation
- ✅ Training Loop
- ✅ Learned Navigation Policy
- ✅ Obstacle Navigation
- ✅ Collision Detection
- ✅ Collision Penalty System
- ✅ Environment Analytics


Current Version:

```text
v0.4.0
```

Current Performance:

```text
Success Rate : 100.00%
Average Reward : 117.72
Average Steps : 20.42
Best Reward : 118
```

---

### ✅ Phase 3 – Obstacle Navigation

Completed:

- ✅ Static Obstacles
- ✅ Collision Detection
- ✅ Collision Penalties
- ✅ Obstacle-aware Q-Learning

---

### ✅ Phase 4 – Environment Analytics

Completed:

- ✅ Success Rate
- ✅ Average Reward
- ✅ Average Steps
- ✅ Performance Evaluation

Results:

```text
Success Rate : 100.00%
Average Reward : 117.72
Average Steps : 20.42
Best Reward : 118
```

---

# Phase 5 – Real Manhattan Street Network

## Goal

Replace the artificial Grid World with a real-world street network.

## Technologies

- OpenStreetMap
- OSMnx
- NetworkX

## Planned Features

- Download Manhattan street network
- Graph-based navigation
- Road intersections as states
- Street segments as actions
- Manhattan graph extraction
- Route visualization
- RL vs A* comparison

Research Question:

```text
A*
vs
Q-Learning
vs
Deep Reinforcement Learning

Evaluation Metrics:

- Success Rate
- Route Length
- Computation Time
- Energy Consumption (future)
```

Expected Release:

```text
v0.5.0
```

---

# Phase 6 – Building Data Integration

## Goal

Introduce realistic urban constraints.

## Data Sources

- OpenStreetMap
- NYC Open Data
- GIS datasets
- Kaggle

## Planned Features

- Building footprints
- No-fly zones

Expected Release:

```text
v0.6.0
```

---

# Phase 7 – 3D Drone Navigation

## State Space

```python
(x, y, z)
```

## Actions

```text
NORTH
SOUTH
EAST
WEST
UP
DOWN
```

## Planned Features

- Altitude control
- Building avoidance
- Energy-aware routing
- Wind simulation
- Building heights

Expected Release:

```text
v0.7.0
```

---

# Phase 8 – Deep Reinforcement Learning

## Goal

Scale the navigation environment beyond the limits of tabular Q-Learning.

## Candidates

- DQN
- Double DQN
- PPO
- A2C

## Planned Features

- Neural value approximation
- Large state spaces
- Real-world scalability

Expected Release:

```text
v0.8.0
```

---

# Phase 9 – Manhattan Drone Navigator

## Final Goal

Create a realistic urban drone navigation simulator.

Features:

- Real Manhattan street network
- Building heights
- 3D navigation
- Deep Reinforcement Learning
- Obstacle avoidance
- Energy optimization

Expected Release:

```text
v1.0.0
```

---

# Stretch Goals

Potential future extensions:

- Multi-agent systems
- Multiple drones
- Dynamic weather
- Air traffic management
- Delivery optimization
- Reinforcement Learning benchmarks