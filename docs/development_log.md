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

# v0.3.0 - Obstacle Navigation

Release Date: November 2026

## Objectives

Introduce obstacles that force the agent to plan alternative routes instead of following a direct Manhattan path.

## Completed Features

### Static Obstacles

Added obstacle cells to the environment.

Example:

```text
. . . . . . . . . G
. . . . . . . . . .
. . . X X X . . . .
. . . X . . . . . .
. . . X . . . . . .
D . . . . . . . . .
```

---

### Collision Detection

The environment detects when the agent attempts to move into an obstacle.

---

### Collision Penalty

Obstacle collisions result in:

```python
reward = -10
```

The agent remains in the current position.

---

### Obstacle-aware Q-Learning

The Q-Learning agent successfully learns to avoid obstacles and still reach the goal.

---

### Training Results

Example output:

```text
Episode 0   | Total Reward: 108
Episode 100 | Total Reward: 118
Episode 900 | Total Reward: 118
```

Result:

✅ Agent learns obstacle avoidance behavior.

✅ Agent still converges to an optimal solution.

---

## Lessons Learned

- Environmental constraints significantly change the learned policy.
- Q-Learning can adapt to obstacles without changing the underlying algorithm.
- Reward penalties effectively discourage collisions.

---

# v0.4.0 - Environment Analytics

Release Date: November 2026

## Objectives

Measure and evaluate the performance of the learning agent using quantitative metrics.

## Completed Features

### Training Analytics

Implemented an analytics module for evaluating agent performance.

Collected metrics:

- Success Rate
- Average Reward
- Average Steps
- Best Reward
- Worst Reward
- Best Steps
- Worst Steps

---

### Success Rate

Measured how often the agent successfully reaches the goal state.

Result:

```text
Success Rate: 100.00%
```

The Q-Learning agent reaches the goal in every training episode.

---

### Reward Analysis

Measured overall training performance.

Results:

```text
Average Reward : 117.72
Best Reward    : 118
Worst Reward   : 78
```

The theoretical optimum remains:

```text
18 movement rewards
+100 goal reward
------------------
118 total reward
```

Result:

✅ Average performance is extremely close to the theoretical optimum.

---

### Step Analysis

Measured navigation efficiency.

Results:

```text
Average Steps : 20.42
Best Steps    : 18
Worst Steps   : 74
```

The shortest possible route requires:

```text
18 steps
```

Result:

✅ The learned navigation policy is highly efficient.

---

### Obstacle Environment Evaluation

The analytics confirm that obstacle-aware navigation does not prevent convergence.

Results:

```text
Success Rate  : 100.00%
Average Reward: 117.72
```

The agent reliably avoids obstacles and still reaches the target.

---

## Lessons Learned

- Success Rate alone is not sufficient for evaluating a learning agent.
- Average Reward provides valuable insight into policy quality.
- Average Steps reveal route efficiency.
- Obstacle penalties successfully shape agent behavior.
- Quantitative evaluation is essential before scaling to real-world environments.


---

# v0.5.0 - Real Manhattan Street Network

Release Date: November 2026

## Objectives

Transition from an artificial Grid World to a real-world Manhattan street network.

## Completed Features

### Manhattan Graph Download

Downloaded Manhattan street network from OpenStreetMap using OSMnx.

Result:

```text
Nodes : 4630
Edges : 9915
```

---

### GraphML Persistence

Saved the graph locally as:

```text
maps/manhattan.graphml
```

---

### Node Inspection

Example node:

```text
42421728
```

Attributes:

```python
{
    'y': 40.7980478,
    'x': -73.9600437,
    'highway': 'traffic_signals',
    'street_count': 3
}
```

---

### Neighbor Inspection

Example:

```text
42435337
42421731
42432736
```

---

### Route Planning

Shortest path:

```text
Path Length: 134 Nodes
Route Length: 10332.86 meters
```

---

### Visualization

Implemented:

- Graph visualization
- Route visualization

Result:

✅ Real Manhattan route displayed successfully.

### Route Visualization

Implemented shortest-path visualization on the real Manhattan road network.

Result:

✅ Route successfully rendered on top of the Manhattan street graph.


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