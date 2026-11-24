# Development Log

This document tracks the major development milestones of the Manhattan Drone Navigator project.

---

# Project Overview

Manhattan Drone Navigator is a Reinforcement Learning project focused on autonomous drone navigation in urban environments.

The long-term vision is to teach a drone how to navigate through Manhattan using:

- OpenStreetMap
- Graph Theory
- Reinforcement Learning
- Building Data
- 3D Airspace Simulation

The project starts with a simple Grid World and incrementally evolves into a realistic navigation environment.

---

# v0.1.0 - Initial Grid World Environment

Release Date: November 2026

## Objectives

Build the first navigation environment and establish the core Reinforcement Learning framework.

## Completed Features

### Manhattan Grid World

Implemented a 2D navigation environment.

State:

```python
(x, y)
```

Goal:

```python
(width - 1, height - 1)
```

Actions:

```text
NORTH
SOUTH
EAST
WEST
```

---

### Manhattan Distance Reward

Implemented the reward function:

```python
reward = old_distance - new_distance
```

The reward encourages the agent to move closer to the goal.

---

### Goal State

Implemented terminal state detection:

```python
done = self.agent_position == self.goal
```

Additional goal reward:

```python
reward += 100
```

---

### Environment Rendering

Implemented ASCII visualization:

```text
. . . . . . . . . G
. . . . . . . . . .
. . . D . . . . . .
. . . . . . . . . .
```

Legend:

```text
D = Drone
G = Goal
. = Empty Cell
```

---

## Lessons Learned

- Environment design is the foundation of Reinforcement Learning.
- Reward shaping directly influences agent behavior.
- A simple environment is sufficient for testing learning algorithms.

---

# v0.2.0 - Q-Learning Agent

Release Date: November 2026

## Objectives

Replace random navigation with a learning-based agent.

## Completed Features

### Random Agent

Implemented a baseline agent.

Behavior:

```python
random.choice(actions)
```

Purpose:

- Environment validation
- Reward testing
- Baseline comparison

---

### Q-Learning Agent

Implemented a tabular Q-Learning algorithm.

Core components:

- Q-table
- Epsilon-greedy exploration
- Learning rate
- Discount factor

---

### Q-Table

State-action values stored in:

```python
Q(state, action)
```

Example:

```text
State (5,5)
Action EAST
Q = 3.27
```

---

### Training Loop

Implemented multi-episode training.

Configuration:

```python
episodes = 1000
max_steps = 100
```

---

### Learned Policy

The agent learns a near-optimal route from the start position to the goal.

Example output:

```text
State (0,0) -> Best Action: NORTH
State (1,0) -> Best Action: EAST
State (5,5) -> Best Action: EAST
State (8,8) -> Best Action: NORTH
```

---

### Training Results

Example result:

```text
Episode 900 | Total Reward: 118
```

Optimal reward calculation:

```text
18 movement rewards
+100 goal reward
------------------
118 total reward
```

Result:

✅ Agent successfully learns the shortest Manhattan path.

---

## Lessons Learned

- Q-Learning converges quickly in deterministic environments.
- Reward engineering is as important as the learning algorithm itself.
- Exploration enables the agent to discover optimal strategies.

---

# Current Project Status

## Completed

- ✅ Project Structure
- ✅ Documentation
- ✅ Manhattan Grid World
- ✅ Manhattan Distance Reward
- ✅ ASCII Rendering
- ✅ Random Agent
- ✅ Q-Learning Agent
- ✅ Q-Table
- ✅ Training Loop
- ✅ Learned Navigation Policy

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

# Upcoming Development

## v0.3.0 - Obstacle Navigation

Goals:

- Static obstacles
- Collision penalties
- Route planning around obstacles

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

---

## v0.4.0 - Real Manhattan Street Network

Goals:

- OpenStreetMap integration
- OSMnx integration
- NetworkX graph representation
- Path planning on real road networks

Research Question:

```text
A*
vs
Q-Learning
vs
Deep Reinforcement Learning
```

---

## v0.5.0 - Building Data

Goals:

- Building footprints
- Building heights
- No-fly zones

Potential Data Sources:

- OpenStreetMap
- NYC Open Data
- Kaggle
- GIS datasets

---

## v1.0.0 - Manhattan Drone Navigator

Goals:

- Full Manhattan environment
- 3D navigation
- Building-aware routing
- Energy-efficient flight planning
- Urban air mobility simulation

State:

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

---

# Long-Term Vision

Build a realistic Reinforcement Learning environment for autonomous urban drone navigation using real-world Manhattan data and modern RL techniques.