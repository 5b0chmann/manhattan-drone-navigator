# System Architecture

## Evolution of the Project

```text
Manhattan Distance
        ↓
Grid World
        ↓
Random Agent
        ↓
Q-Learning Agent
        ↓
Obstacle Navigation
        ↓
Environment Analytics
        ↓
OpenStreetMap Integration
        ↓
Real Manhattan Graph
        ↓
Building Data
        ↓
3D Navigation
        ↓
Manhattan Drone Navigator
```

---

## Current Architecture

```text
+---------------------+
| ManhattanGridWorld  |
+---------------------+
          |
          v
+---------------------+
| Reward Function     |
| Manhattan Distance  |
+---------------------+
          |
          v
+---------------------+
| Obstacles           |
| Collision Penalty   |
+---------------------+
          |
          v
+---------------------+
| Q-Learning Agent    |
+---------------------+
          |
          v
+---------------------+
| Learned Policy      |
+---------------------+
```

---

## Future Architecture

```text
OpenStreetMap
      ↓
OSMnx
      ↓
NetworkX Graph
      ↓
RL Environment
      ↓
Q-Learning / PPO / DQN
      ↓
3D Drone Navigation
```