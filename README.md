# 🚁 Manhattan Drone Navigator

A Reinforcement Learning project that teaches an autonomous drone to navigate through Manhattan using OpenStreetMap, graph theory, and Deep Reinforcement Learning.

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

The project evolves from a simple Grid World into a realistic 3D urban airspace simulation.

---

## Development Roadmap

### ✅ Phase 1 – Reinforcement Learning Fundamentals

Topics:

- Markov Decision Process (MDP)
- Reward Functions
- Q-Learning
- Deep Q-Networks (DQN)
- PPO
- Exploration vs. Exploitation

---

### ✅ Phase 2 – Manhattan Grid World

Completed:

- ✅ 2D Grid Environment
- ✅ Manhattan Distance Reward Function
- ✅ ASCII Rendering
- ✅ Random Navigation Agent
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

Example Training Result:

```text
Episode 900 | Total Reward: 118
```

The agent successfully learns the optimal Manhattan path.

---

### 🚧 Phase 3 – Obstacle Navigation

Goal:

Teach the drone to avoid obstacles while still reaching the target.

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

Planned Features:

- Static Obstacles
- Collision Penalties
- Alternative Route Planning
- Obstacle-Aware Q-Learning

---

### ⬜ Phase 4 – Real Manhattan Street Network

Transition from:

```text
Grid World
```

to:

```text
Real Manhattan Street Network
```

Technologies:

- OpenStreetMap
- OSMnx
- NetworkX

Research Question:

```text
A*
vs
RL Agent
```

---

### ⬜ Phase 5 – Building Obstacles

Buildings become no-fly zones.

Data Sources:

- OpenStreetMap
- NYC Open Data
- GIS Datasets
- Kaggle

---

### ⬜ Phase 6 – Building Heights

Additional State Information:

```python
(x, y, z)
```

Potential Data Sources:

- height
- building:levels
- LiDAR Data
- GIS Building Datasets

---

### ⬜ Phase 7 – 3D Manhattan Drone Navigator

Actions:

```text
NORTH
SOUTH
EAST
WEST
UP
DOWN
```

Additional Factors:

- Building Heights
- Wind Conditions
- Energy Consumption
- Dynamic Obstacles
- Air Traffic Constraints

---

## Current Status

✅ Manhattan Grid World implemented

✅ Random Agent implemented

✅ Q-Learning Agent implemented

✅ Training successful

🚧 Working on obstacle-aware navigation

---

## Repository Structure

```text
manhattan-drone-navigator/
│
├── agents/
│   ├── random_agent.py
│   └── q_learning_agent.py
│
├── environments/
│   └── grid_world.py
│
├── experiments/
├── maps/
├── notebooks/
├── docs/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Technologies

- Python
- Reinforcement Learning
- Q-Learning
- OpenStreetMap
- NetworkX
- OSMnx
- NumPy
- Matplotlib

---

## License

MIT License