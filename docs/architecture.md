# System Architecture

## Project Evolution

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
| Manhattan Distance  |
| Reward Function     |
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
| Analytics Module    |
+---------------------+
          |
          v
+---------------------+
| Learned Policy      |
+---------------------+
```

---

## Current Performance

```text
Success Rate : 100.00%
Average Reward : 117.72
Average Steps : 20.42
Best Reward : 118
Worst Reward : 78
Best Steps : 18
Worst Steps : 74
```

---

## Next Architecture

```text
OpenStreetMap
      ↓
OSMnx
      ↓
NetworkX
      ↓
Manhattan Road Graph
      ↓
RL Environment
      ↓
Q-Learning / PPO / DQN
      ↓
3D Drone Navigation
```