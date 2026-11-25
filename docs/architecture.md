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
OpenStreetMap
        ↓
OSMnx
        ↓
NetworkX MultiDiGraph
        ↓
GraphML Persistence
        ↓
Node Inspection
        ↓
Neighbor Inspection
        ↓
Shortest Path
        ↓
Route Visualization
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