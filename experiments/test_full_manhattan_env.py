from environments.manhattan_graph_env import ManhattanGraphEnv

import random 
import networkx as nx

def test_graph_loaded():

    env = ManhattanGraphEnv()

    print("\n=== GRAPH INFO ===")
    print("Nodes:", env.graph.number_of_nodes())
    print("Edges:", env.graph.number_of_edges())

    assert env.graph.number_of_nodes() > 0
    assert env.graph.number_of_edges() > 0

def test_reset():

    env = ManhattanGraphEnv()

    state = env.reset()

    print("\n=== RESET ===")
    print("Start Node:", state)

    assert state == env.start_node

def test_goal():

    env = ManhattanGraphEnv()

    print("\n=== GOAL ===")
    print("Goal:", env.goal_node)

    assert env.goal_node in env.graph.nodes

def test_actions():

    env = ManhattanGraphEnv()

    state = env.reset()

    actions = env.get_actions()

    print("\n=== ACTIONS ===")
    print("Number of actions:", len(actions))

    assert len(actions) > 0

def test_single_step():

    env = ManhattanGraphEnv()

    env.reset()

    actions = env.get_actions()

    action = actions[0]

    next_state, reward, done = env.step(
        action
    )

    print("\n== SINGLE STEP ===")
    print("Next State:", next_state)
    print("Reward:", reward)
    print("Done:", done)

    assert next_state in env.graph.nodes

def test_random_walk():

    env = ManhattanGraphEnv()

    state = env.reset()

    total_reward = 0

    for step in range(100):
        actions = env.get_actions()

        if not actions:
            break

        action = random.choice(actions)

        state, reward, done = env.step(action)

        total_reward += reward

        if done:
            print(f"\nGoal reached after {step + 1} steps")

            break

    print("\n=== RANDOM WALK ===")
    print("Final State :", state)
    print("Reward      :", total_reward)

def test_connectivity():

    env = ManhattanGraphEnv()

    path = nx.shortest_path(
        G=env.graph,
        source=env.start_node,
        target=env.goal_node
    )

    print("\n=== CONNECTIVITY ===")
    print("Path Length:", len(path))

    assert len(path) > 1

def test_a_star():

    env = ManhattanGraphEnv()

    route = env.a_star_route()

    print("\n=== A* ===")
    print("Nodes:", len(route))

    print(
        f"Shortest Path Length: "
        f"{len(route)}"
    )

    print(
        "Goal Reached:",
        route[-1] == env.goal_node
    )

    assert route[-1] == env.goal_node

def test_episode_generation():
    env = ManhattanGraphEnv()

    for episode in range(100):

        state = env.reset()

        for _ in range(200):

            actions = env.get_actions()

            if not actions:
                break
            
            action = actions[0]

            state, reward, done = env.step(action)

            if done:
                break

    print("\n100 episodes successful.")

if __name__ == "__main__":

    test_graph_loaded()
    test_reset()
    test_goal()
    test_actions()
    test_single_step()
    test_random_walk()
    test_connectivity()
    test_a_star()
    test_episode_generation()

