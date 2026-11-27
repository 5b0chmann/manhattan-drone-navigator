# Project Roadmap

This document outlines the planned evolution of the Manhattan Drone Navigator project.

---

# Vision

Build an autonomous drone navigation system that learns how to navigate through Manhattan using Reinforcement Learning and real-world geographic data.

```text
OpenStreetMap
        +
Street Network
        +
Building Data
        +
Building Heights
        +
Reinforcement Learning
        =
Manhattan Drone Navigator
```

---

# Current Status

Current Version:

```text
v0.5.1
```

---

# ✅ Phase 1 – Reinforcement Learning Fundamentals

Completed Topics:

- ✅ Markov Decision Process (MDP)
- ✅ Reward Functions
- ✅ Q-Learning
- ✅ Deep Q-Networks (DQN)
- ✅ PPO Fundamentals
- ✅ Exploration vs Exploitation

Status:

```text
Completed
```

---

# ✅ Phase 2 – Manhattan Grid World

Implemented:

- ✅ Manhattan Grid Environment
- ✅ Manhattan Distance Reward
- ✅ ASCII Rendering
- ✅ Random Agent
- ✅ Q-Learning Agent
- ✅ Q-Table
- ✅ Training Loop
- ✅ Learned Navigation Policy

State Space:

```python
(x, y)
```

Actions:

```text
NORTH
SOUTH
EAST
WEST
```

Training Result:

```text
Episode 900 | Total Reward: 118
```

Status:

```text
Completed
```

---

# ✅ Phase 3 – Obstacle Navigation

Implemented:

- ✅ Static Obstacles
- ✅ Collision Detection
- ✅ Collision Penalties
- ✅ Obstacle-aware Q-Learning

Results:

```text
Agent learns alternative routes
while avoiding collisions.
```

Status:

```text
Completed
```

---

# ✅ Phase 4 – Environment Analytics

Implemented:

- ✅ Success Rate Analysis
- ✅ Average Reward Analysis
- ✅ Step Analysis
- ✅ Performance Evaluation

Results:

```text
Success Rate : 100.00%
Average Reward : 117.72
Average Steps : 20.42
Best Reward : 118
Best Steps : 18
```

Status:

```text
Completed
```

---

# 🚧 Phase 5 – Graph Reinforcement Learning

## Goal

Replace the artificial Grid World with a real Manhattan street network based on OpenStreetMap.

Technologies:

- OpenStreetMap
- OSMnx
- NetworkX
- Graph Theory
- Reinforcement Learning

---

## ✅ Phase 5.0 – Manhattan Street Graph

Completed:

- ✅ Manhattan graph download
- ✅ OSMnx integration
- ✅ GraphML persistence
- ✅ Graph loading
- ✅ Node inspection
- ✅ Neighbor inspection
- ✅ Shortest path calculation
- ✅ Graph visualization
- ✅ Route visualization
- ✅ A* baseline

Graph Statistics:

```text
Nodes : 4630
Edges : 9915
```

A* Baseline:

```text
Path Length  : 134 Nodes
Route Length : 10332.86 meters
Goal Reached : True
```

Status:

```text
Completed
```

---

## ✅ Phase 5A – Mini Manhattan

Goal:

Validate Reinforcement Learning on a small real-world graph.

Environment:

```text
Mini Manhattan
```

Results:

```text
Nodes          : 9
Shortest Route : 3 Nodes
Success Rate   : 95.8%
```

Implemented:

- ✅ MiniManhattanEnv
- ✅ DroneNavigatorAgent
- ✅ Graph-based actions
- ✅ Graph-based state space
- ✅ Q-Learning training pipeline

Status:

```text
Completed
```

---

## ✅ Phase 5B – Neighborhood Manhattan

Goal:

Scale Reinforcement Learning to a larger graph environment.

Environment:

```text
Neighborhood Manhattan
```

Results:

```text
Nodes          : 24
Shortest Route : 9 Nodes
Success Rate   : 97.9%
```

Agent Statistics:

```text
Q-Table Entries : 52
```

Implemented:

- ✅ NeighborhoodManhattanEnv
- ✅ Neighborhood training pipeline
- ✅ Success-rate tracking
- ✅ Performance evaluation
- ✅ Graph-based navigation

Status:

```text
Completed
```

---

## 🚧 Phase 5C – Large Neighborhood Manhattan

### Goal

Scale graph-based Reinforcement Learning beyond small neighborhood environments while maintaining successful navigation performance.

### Environment

```text
Large Neighborhood Manhattan
```

### Current Results

```text
Nodes          : 127
Shortest Route : 11 Nodes
Success Rate   : 4.0%
```

### Key Observation

The transition from small graph environments to larger Manhattan subgraphs revealed a significant learning challenge.

```text
Mini Manhattan
Nodes: 9
Success Rate: 95.8%

Neighborhood Manhattan
Nodes: 24
Success Rate: 97.9%

Large Neighborhood Manhattan
Nodes: 127
Success Rate: 3.4%

Random Agent
Nodes: 127
Success Rate: 2.0%
```

### Initial Findings

- Q-Learning significantly outperforms random exploration on small graph environments.
- Performance remains strong on Neighborhood Manhattan.
- Scaling from 24 nodes to 127 nodes results in a dramatic reduction in success rate.
- The Q-Learning agent still performs slightly better than a random agent, indicating that some useful navigation behavior is learned.
- Additional investigation is required to determine whether the limitation is caused by state-space growth, reward design, local policy loops, or the limits of tabular Q-Learning.

### Research Question

```text
How well does tabular Q-Learning
scale to larger real-world street
graphs before Deep Reinforcement
Learning becomes necessary?
```

### Research Question

```text
At which graph size does
tabular Q-Learning stop scaling
effectively?
```

### Planned Tasks

- ⬜ Analyze failure cases
- ⬜ Route efficiency evaluation
- ⬜ Q-Table growth analysis
- ⬜ Hyperparameter tuning
- ⬜ Reward function optimization
- ⬜ Curriculum learning experiments
- ⬜ Agent benchmarking

### Evaluation Metrics

```text
Success Rate
Route Length
Training Time
Q-Table Size
Goal Completion Rate
```

### Expected Outcome

```text
Identify the scaling limits
of tabular Q-Learning before
transitioning to Deep RL methods.
```

### Status

```text
In Progress
```

---

## ⬜ Phase 5D – Full Manhattan RL

Goal:

Train an RL agent on the complete Manhattan street network.

Environment:

```text
Full Manhattan
```

Graph:

```text
Nodes : 4630
Edges : 9915
```

Research Question:

```text
A*
vs
Q-Learning
```

Planned Features:

- ⬜ Full Manhattan RL Environment
- ⬜ Large Scale Training
- ⬜ Agent Evaluation
- ⬜ Runtime Analysis
- ⬜ Route Efficiency Comparison
- ⬜ A* vs RL Benchmark

Status:

```text
Planned
```

---

# ⬜ Phase 6 – Building Data Integration

Goal:

Introduce realistic urban obstacles.

Data Sources:

- OpenStreetMap
- NYC Open Data
- GIS Datasets
- Kaggle

Planned Features:

- ⬜ Building Footprints
- ⬜ No-Fly Zones
- ⬜ Restricted Areas
- ⬜ Urban Obstacles

Target Version:

```text
v0.6.0
```

---

# ⬜ Phase 7 – 3D Drone Navigation

Goal:

Extend navigation from 2D streets to 3D urban airspace.

State Space:

```python
(node, altitude)
```

Actions:

```text
LEFT
RIGHT
FORWARD
UP
DOWN
```

Planned Features:

- ⬜ Building Heights
- ⬜ Altitude Control
- ⬜ Building Avoidance
- ⬜ Energy-aware Routing
- ⬜ Wind Simulation

Target Version:

```text
v0.7.0
```

---

# ⬜ Phase 8 – Deep Reinforcement Learning

Goal:

Scale beyond the limits of tabular Q-Learning.

Candidates:

- ⬜ DQN
- ⬜ Double DQN
- ⬜ PPO
- ⬜ A2C

Planned Features:

- ⬜ Neural Value Approximation
- ⬜ Large State Spaces
- ⬜ Real-world Scalability

Target Version:

```text
v0.8.0
```

---

# ⬜ Phase 9 – Manhattan Drone Navigator

Final Goal:

Create a realistic urban drone navigation simulator.

Features:

- ⬜ Real Manhattan Street Network
- ⬜ Building Heights
- ⬜ 3D Navigation
- ⬜ Deep Reinforcement Learning
- ⬜ Obstacle Avoidance
- ⬜ Energy Optimization
- ⬜ Urban Air Mobility Simulation

Target Version:

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
- RL benchmarks
- Graph Neural Networks (GNNs)
- Real-world GIS integration

---

# Current Project Status

```text
✅ Phase 1 – RL Fundamentals
✅ Phase 2 – Manhattan Grid World
✅ Phase 3 – Obstacle Navigation
✅ Phase 4 – Analytics
✅ Phase 5.0 – Manhattan Graph
✅ Phase 5A – Mini Manhattan
✅ Phase 5B – Neighborhood Manhattan

🚧 Phase 5C – Large Neighborhood Manhattan
```