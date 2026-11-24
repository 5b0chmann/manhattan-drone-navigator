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

Current Version:

```text
v0.3.0
```

---

# Phase 3 – Obstacle Navigation

## Goal

Teach the agent to avoid obstacles while still reaching the destination.

Example:

```text
. . . . . . . . . G
. . X X X X . . . .
. . X X X X . . . .
. . X X X X . . . .
. . . . . . . . . .
. . . . . . . . . .
D . . . . . . . . .
```

## Completed Features

- Static obstacles
- Collision detection
- Collision penalties
- Alternative route planning
- Obstacle-aware Q-Learning

Expected Release:

```text
v0.3.0
```

---

# Phase 4 – Environment Analytics

## Goal

Understand and visualize agent performance.

## Planned Features

- Episode statistics
- Success rate
- Average reward
- Reward plots
- Learning curves

Example Metrics:

```text
Success Rate
Average Reward
Episodes to Convergence
```

Expected Release:

```text
v0.4.0
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

Research Question:

```text
A*
vs
Q-Learning
vs
Deep Reinforcement Learning
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
- Building heights

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

Expected Release:

```text
v0.7.0
```

---

# Phase 8 – Deep Reinforcement Learning

## Goal

Move from tabular learning to neural-network-based agents.

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