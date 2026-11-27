# 🚁 Manhattan Drone Navigator

A Reinforcement Learning project that teaches an autonomous drone to navigate through Manhattan using OpenStreetMap, graph theory, and Reinforcement Learning.

---

# Vision

The long-term goal is to create a realistic 3D navigation environment in which an autonomous drone learns optimal flight paths through Manhattan while avoiding obstacles, buildings, and restricted airspace.

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

# Project Motivation

The project originated from the Manhattan distance metric:

```math
d = |x_1 - x_2| + |y_1 - y_2|
```

Because Manhattan's street layout resembles a grid, it provides an ideal environment for Reinforcement Learning experiments.

The project evolves from a simple Grid World into a realistic graph-based urban navigation system and later into a full 3D drone simulation.

---

# Development Roadmap

## ✅ Phase 1 – Reinforcement Learning Fundamentals

Completed Topics:

- Markov Decision Process (MDP)
- Reward Functions
- Q-Learning
- DQN Fundamentals
- PPO Fundamentals
- Exploration vs Exploitation

Status:

```text
Completed
```

---

## ✅ Phase 2 – Manhattan Grid World

Implemented:

- ✅ Manhattan Grid Environment
- ✅ Manhattan Distance Reward
- ✅ ASCII Rendering
- ✅ Random Agent
- ✅ Q-Learning Agent
- ✅ Q-Table Implementation
- ✅ Training Loop
- ✅ Learned Navigation Policy

State Representation:

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

Reward Function:

```python
reward = old_distance - new_distance
```

Goal Reward:

```python
reward += 100
```

Training Result:

```text
Episode 900 | Total Reward: 118
```

Result:

✅ Agent successfully learned the optimal Manhattan route.

---

## ✅ Phase 3 – Obstacle Navigation

Implemented:

- ✅ Static Obstacles
- ✅ Collision Detection
- ✅ Collision Penalties
- ✅ Obstacle-aware Q-Learning

Environment Example:

```text
. . . . . . . . . G
. . X X X X . . . .
. . X X X X . . . .
. . X X X X . . . .
. . . . . . . . . .
. . . . . . . . . .
D . . . . . . . . .
```

Result:

✅ Agent learns alternative routes while avoiding collisions.

---

## ✅ Phase 4 – Environment Analytics

Implemented:

- ✅ Success Rate Analysis
- ✅ Reward Analytics
- ✅ Step Analytics
- ✅ Performance Evaluation

Results:

```text
Success Rate : 100.00%
Average Reward : 117.72
Average Steps : 20.42
Best Reward : 118
Best Steps : 18
Worst Reward : 78
Worst Steps : 74
```

Result:

✅ Analytics confirmed convergence toward a near-optimal policy.

---

## 🚧 Phase 5 – Graph Reinforcement Learning

### Goal

Replace the artificial Grid World with a real-world Manhattan street network.

Technologies:

- OpenStreetMap
- OSMnx
- NetworkX
- Graph Theory
- Reinforcement Learning

---

### ✅ Phase 5.0 – Manhattan Street Graph

Implemented:

- ✅ Manhattan Graph Download
- ✅ OSMnx Integration
- ✅ GraphML Persistence
- ✅ Graph Loading
- ✅ Node Inspection
- ✅ Neighbor Inspection
- ✅ Shortest Path Calculation
- ✅ A* Baseline
- ✅ Graph Visualization
- ✅ Route Visualization

Graph Statistics:

```text
Nodes : 4630
Edges : 9915
```

A* Results:

```text
Path Length  : 134 Nodes
Route Length : 10332.86 meters
Goal Reached : True
```

Result:

✅ Real-world Manhattan route successfully generated and visualized. 【1-6fa378】【2-b0d827】【3-cef987】

---

### ✅ Phase 5A – Mini Manhattan

Goal:

Validate Reinforcement Learning on a real graph.

Environment:

```text
Mini Manhattan
```

Training Results:

```text
Nodes          : 9
Shortest Route : 3 Nodes
Success Rate   : 95.8%
```

Implemented:

- ✅ MiniManhattanEnv
- ✅ DroneNavigatorAgent
- ✅ Graph-based Actions
- ✅ Graph-based States
- ✅ Graph Training Pipeline

Result:

✅ Agent successfully learns to reach the goal on a real-world Manhattan subgraph.

---

### ✅ Phase 5B – Neighborhood Manhattan

Goal:

Scale Reinforcement Learning to a larger graph.

Environment:

```text
Neighborhood Manhattan
```

Training Results:

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
- ✅ Neighborhood Training
- ✅ Success Tracking
- ✅ Graph Navigation

Result:

✅ Agent successfully scales beyond Mini Manhattan.

---

### 🚧 Phase 5C – Large Neighborhood Manhattan

Goal:

Increase graph complexity before moving to Full Manhattan.

Target Size:

```text
50 - 500 Nodes
```

Implemented:

- ✅ Radius 10 graph generation
- ✅ Large Neighborhood Environment
- ✅ Large Neighborhood Training
- ✅ Random-Agent Benchmark
- ✅ Policy Evaluation
- ✅ Route Inspection

Success Criteria:

```text
Success Rate > 80%
```

### 🔬 Learning Investigation

During Phase 5C, a major performance degradation was observed while scaling from small graph environments to larger Manhattan subgraphs.

Initial results suggested that tabular Q-Learning might not scale effectively:

```text
Mini Manhattan
Nodes: 9
Success Rate: 95.8%

Neighborhood Manhattan
Nodes: 24
Success Rate: 97.9%

Large Neighborhood Manhattan
Nodes: 127
Success Rate: 3.1%
```

Several hypotheses were investigated:

- Reward shaping
- Loop penalties
- Goal-aware state representation
- Random-agent benchmarking
- Route analysis based on A* paths

A random baseline was implemented:

```text
Random Agent
Success Rate: 2.0%
```

The investigation eventually revealed a critical implementation bug in the Q-learning update function.

### Root Cause

The Q-value update was executed only inside the wrong conditional branch:

```python
if next_actions:
    max_future_q = ...

else:
    updated_q = ...
    self.q_table[(state, action)] = updated_q
```

As a result, Q-values were often not updated correctly during training.

### Fix

The Q-value update was moved outside the conditional block:

```python
if next_actions:
    max_future_q = ...
else:
    max_future_q = 0.0

updated_q = ...

self.q_table[(state, action)] = updated_q
```

### Result

After correcting the implementation:

```text
Large Neighborhood Manhattan

Nodes          : 127
Shortest Route : 11 Nodes

Success Rate:
3.1%
→
97.3%
```

### Lessons Learned

- Poor RL performance can originate from implementation bugs rather than algorithmic limitations.
- Benchmarking against random agents and analyzing learned policies can be invaluable debugging tools.
- Systematic experimentation is often more effective than immediately increasing model complexity.
- Careful verification of the learning update rule is essential when investigating scaling behavior.

---

### ⬜ Phase 5D – Full Manhattan RL

Goal:

Train directly on the full Manhattan street network.

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

- ⬜ Full Manhattan Environment
- ⬜ Full Manhattan Training
- ⬜ Agent Evaluation
- ⬜ Runtime Benchmarking
- ⬜ Route Efficiency Analysis
- ⬜ A* vs RL Comparison

---

## ⬜ Phase 6 – Building Data Integration

Goal:

Introduce realistic urban constraints.

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

## ⬜ Phase 7 – 3D Drone Navigation

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
- ⬜ Energy-Aware Routing
- ⬜ Wind Simulation

Target Version:

```text
v0.7.0
```

---

## ⬜ Phase 8 – Deep Reinforcement Learning

Goal:

Scale beyond the limits of tabular Q-Learning.

Candidates:

- DQN
- Double DQN
- PPO
- A2C

Planned Features:

- ⬜ Neural Value Approximation
- ⬜ Large State Spaces
- ⬜ Real-world Scalability

Target Version:

```text
v0.8.0
```

---

## ⬜ Phase 9 – Manhattan Drone Navigator

Final Goal:

Create a realistic urban drone navigation simulator.

Features:

- Real Manhattan Street Network
- Building Heights
- 3D Navigation
- Deep Reinforcement Learning
- Obstacle Avoidance
- Energy Optimization
- Urban Air Mobility Simulation

Target Version:

```text
v1.0.0
```

---

# Current Status

Current Version:

```text
v0.5.1
```

Completed:

```text
✅ Phase 1 – RL Fundamentals
✅ Phase 2 – Manhattan Grid World
✅ Phase 3 – Obstacle Navigation
✅ Phase 4 – Analytics
✅ Phase 5.0 – Manhattan Street Graph
✅ Phase 5A – Mini Manhattan
✅ Phase 5B – Neighborhood Manhattan
```

Current Focus:

```text
🚧 Phase 5C – Large Neighborhood Manhattan
```

---

# Repository Structure

```text
manhattan-drone-navigator/
│
├── agents/
│   ├── random_agent.py
│   ├── q_learning_agent.py
│   └── manhattan_drone_agent.py
│
├── environments/
│   ├── grid_world.py
│   ├── manhattan_graph_env.py
│   ├── mini_manhattan_env.py
│   └── neighborhood_manhattan_env.py
│
├── experiments/
│   ├── analytics.py
│   ├── train_mini_manhattan.py
│   └── train_neighborhood_manhattan.py
│
├── maps/
│   ├── manhattan.graphml
│   └── manhattan_graph.py
│
├── docs/
│   ├── roadmap.md
│   ├── development_log.md
│   └── architecture.md
│
├── notebooks/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Technologies

- Python
- Reinforcement Learning
- Q-Learning
- OpenStreetMap
- OSMnx
- NetworkX
- NumPy
- Matplotlib

---

# Documentation

Additional project documentation is available in:

- `docs/roadmap.md`
- `docs/development_log.md`
- `docs/architecture.md`

---

# License

MIT License