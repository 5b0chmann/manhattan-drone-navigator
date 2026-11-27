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

# ✅ Phase 5 – Graph Reinforcement Learning

Current Status:

```text
✅ Phase 5.0 – Manhattan Street Graph
✅ Phase 5A – Mini Manhattan
✅ Phase 5B – Neighborhood Manhattan
✅ Phase 5C – Large Neighborhood Manhattan
✅ Phase 5D.1 – Full Manhattan Environment
✅ Phase 5D.2 – Random Benchmark
✅ Phase 5D.3 – Full Manhattan Q-Learning

🚧 Current Focus:
Phase 5D.4 – Policy Evaluation
```

## Goal

Replace the artificial Grid World with a real-world Manhattan street network and evaluate how Reinforcement Learning scales from small graph environments to a complete urban road network.

Technologies:

- OpenStreetMap
- OSMnx
- NetworkX
- Graph Theory
- Reinforcement Learning

---

## ✅ Phase 5.0 – Manhattan Street Graph

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

✅ Real-world Manhattan route successfully generated and visualized. 【1-5cc63b】【2-8eba5a】【3-d754b7】

---

## ✅ Phase 5A – Mini Manhattan

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

## ✅ Phase 5B – Neighborhood Manhattan

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

## ✅ Phase 5C – Large Neighborhood Manhattan

Goal:

Scale Reinforcement Learning to significantly larger Manhattan subgraphs.

Environment:

```text
Large Neighborhood Manhattan
```

Training Results:

```text
Nodes          : 127
Shortest Route : 11 Nodes
Success Rate   : 97.3%
```

Agent Statistics:

```text
Q-Table Entries : 257
```

Implemented:

- ✅ Radius 10 Graph Generation
- ✅ Large Neighborhood Environment
- ✅ Large Neighborhood Training
- ✅ Random Agent Benchmark
- ✅ Policy Evaluation
- ✅ Route Inspection
- ✅ Root Cause Analysis
- ✅ Bug Fix Validation

Result:

✅ Agent successfully scales to 127-node Manhattan subgraphs.

✅ Success Rate exceeds 97%.

✅ Large Neighborhood Manhattan completed.

### Bug Fix Validation

After fixing the Q-learning update implementation:

```text
Large Neighborhood Manhattan

Nodes          : 127
Shortest Route : 11 Nodes

Success Rate:
3.1%
→
97.3%
```

This confirmed that the primary limitation was not graph size, reward shaping, or state representation, but an implementation defect in the Q-value update rule.

---

## ✅ Phase 5D.1 – Full Manhattan Environment

Environment Validation:

```text
Nodes : 4630
Edges : 9915
```

Implemented:

- ✅ Full Manhattan Environment
- ✅ Graph Connectivity Testing
- ✅ Environment Validation Suite
- ✅ Random Walk Testing
- ✅ A* Route Validation

Tests Passed:

```text
✅ Graph Loaded
✅ Reset
✅ Actions
✅ Step Function
✅ Connectivity
✅ A* Routing
✅ Episode Generation
✅ Environment Stability
```

Result:

✅ Full Manhattan RL environment successfully validated.

---

## ✅ Phase 5D.2 – Full Manhattan Random Benchmark

Goal:

Measure the baseline performance of a completely random agent on the full Manhattan graph.

Results:

```text
Episodes      : 100
Successes     : 0
Success Rate  : 0.00%
Average Reward: 42.00
```

Conclusion:

```text
Random exploration is
insufficient for solving
the full Manhattan
navigation problem.
```

Result:

✅ Official baseline established.

---

## ✅ Phase 5D.3 – Full Manhattan Q-Learning

### Environment

```text
Nodes : 4630
Edges : 9915
```

### A* Baseline

```text
Route Length : 134 Nodes
Goal Reached : True
```

### Random Agent Benchmark

```text
Episodes      : 100
Successes     : 0
Success Rate  : 0.00%
```

### Key Result

```text
Random Agent     : 0.00%
Q-Learning Agent : 95.00%
```

### Training Configuration

```text
Episodes  : 5000
Max Steps : 500
```

### Final Results

```text
Episodes         : 5000
Successes        : 4750
Success Rate     : 95.00%
Q-Table Entries  : 4683
```

### Learning Progress

```text
Episode 500   : 67.80%
Episode 1000  : 81.80%
Episode 1500  : 86.80%
Episode 2000  : 89.55%
Episode 2500  : 91.00%
Episode 3000  : 92.00%
Episode 3500  : 93.11%
Episode 4000  : 93.90%
Episode 4500  : 94.51%
Episode 5000  : 95.00%
```

### Conclusion

```text
Q-Learning successfully scaled
from small Manhattan graphs
to the complete Manhattan
street network.

Performance improved from

0.00% success rate
(Random Agent)

to

95.00% success rate
(Q-Learning).
```

Result:

✅ Full Manhattan Q-Learning completed.

✅ Success Rate reached 95.00%.

✅ Q-Learning successfully scaled to the complete Manhattan street network.

✅ Phase 5D.3 completed.

---

## 🚧 Phase 5D.4 – Policy Evaluation

Current Goal:

Evaluate route quality and compare learned policies against the A* optimum.

Planned Metrics:

```text
Average Success Steps
Best Success Steps
Worst Success Steps

A* vs Q-Learning

Route Efficiency
Policy Quality
```

Research Question:

```text
How close can
Q-Learning get to
the optimal A* route?
```

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
v0.5.3
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
✅ Phase 5C – Large Neighborhood Manhattan
✅ Phase 5D.1 – Full Manhattan Environment
✅ Phase 5D.2 – Random Benchmark
✅ Phase 5D.3 – Full Manhattan Q-Learning
```

Current Focus:

```text
🚧 Phase 5D.4 – Policy Evaluation
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
|   ├── test_full_manhattan_env.py
|   ├── random_agent_full_manhattan.py
|   ├── train_full_manhattan.py
│   └── train_neighborhood_manhattan.py
|   └── random_agent_benchmark.py
|   └── evaluation.py
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