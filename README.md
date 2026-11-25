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

Since Manhattan is organized in a nearly grid-like structure, it provides a natural environment for Reinforcement Learning experiments.

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

### ✅ Phase 3 – Obstacle Navigation

Completed:

- ✅ Static Obstacles
- ✅ Collision Detection
- ✅ Collision Penalties
- ✅ Obstacle-aware Q-Learning

Example Environment:

```text
. . . . . . . . . G
. . X X X X . . . .
. . X X X X . . . .
. . X X X X . . . .
. . . . . . . . . .
. . . . . . . . . .
D . . . . . . . . .
```

The agent successfully learns alternative routes while avoiding collisions.

---

### ✅ Phase 4 – Environment Analytics

Completed:

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
```

The analytics confirm that obstacle-aware navigation converges to a near-optimal policy.

---

### 🚧 Phase 5 – Real Manhattan Street Network

Goal:

Replace the artificial Grid World with a real-world street network.

Technologies:

- OpenStreetMap
- OSMnx
- NetworkX

Current Progress:

- ✅ Manhattan graph download
- ✅ GraphML persistence
- ✅ Graph loading
- ✅ Node inspection
- ✅ Neighbor inspection
- ✅ Shortest path calculation
- ✅ Graph visualization
- ✅ Route visualization

Current Graph Statistics:

```text
Nodes : 4630
Edges : 9915
```

---

### ⬜ Phase 6 – Building Data Integration

Goal:

Introduce realistic urban constraints.

Data Sources:

- OpenStreetMap
- NYC Open Data
- GIS datasets
- Kaggle

Planned Features:

- Building footprints
- No-fly zones

---

### ⬜ Phase 7 – 3D Drone Navigation

State Space:

```python
(x, y, z)
```

Actions:

```text
NORTH
SOUTH
EAST
WEST
UP
DOWN
```

Planned Features:

- Building heights
- Altitude control
- Building avoidance
- Energy-aware routing
- Wind simulation

---

### ⬜ Phase 8 – Deep Reinforcement Learning

Goal:

Scale the navigation environment beyond the limits of tabular Q-Learning.

Candidates:

- DQN
- Double DQN
- PPO
- A2C

Planned Features:

- Neural value approximation
- Large state spaces
- Real-world scalability

---

### ⬜ Phase 9 – Manhattan Drone Navigator

Final Goal:

Create a realistic urban drone navigation simulator.

Features:

- Real Manhattan street network
- Building heights
- 3D navigation
- Deep Reinforcement Learning
- Obstacle avoidance
- Energy optimization
- Urban air mobility simulation

---

## Current Status

✅ Manhattan Grid World implemented

✅ Q-Learning Agent implemented

✅ Obstacle Navigation implemented

✅ Collision Detection implemented

✅ Environment Analytics implemented

✅ Performance Evaluation completed

Current Metrics:

```text
Success Rate : 100.00%
Average Reward : 117.72
Average Steps : 20.42
Best Reward : 118
```

🚧 Preparing integration of the real Manhattan street network

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
│   └── analytics.py
│
├── docs/
│   ├── architecture.md
│   ├── development_log.md
│   └── roadmap.md
│
├── maps/
├── notebooks/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Technologies

- Python
- Reinforcement Learning
- Q-Learning
- OpenStreetMap
- OSMnx
- NetworkX
- NumPy
- Matplotlib

---

## Documentation

Additional project documentation is available in:

- `docs/development_log.md`
- `docs/roadmap.md`
- `docs/architecture.md`

---

## License

MIT License