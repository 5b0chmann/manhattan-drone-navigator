# environments/manhattan_graph_env.py

from pathlib import Path

import osmnx as ox

import networkx as nx

class ManhattanGraphEnv:

    def __init__(self):

        graph_path = (
            Path(__file__).parent.parent
            / "maps"
            / "manhattan.graphml"
        )

        self.graph = ox.load_graphml(
            graph_path
        )

        self.nodes = list(
            self.graph.nodes
        )

        self.start_node = self.nodes[0]
        self.goal_node = self.nodes[100]

        self.current_node = self.start_node

    def reset(self):

        self.current_node = self.start_node

        return self.current_node

    def get_actions(self):

        return list(
            self.graph.neighbors(
                self.current_node
            )
        )

    def distance_to_goal(self):

        try:

            return nx.shortest_path_length(
                self.graph,
                self.current_node,
                self.goal_node,
                weight="length"
            )

        except nx.NetworkXNoPath:

            return float("inf")

    def step(self, next_node):

        actions = self.get_actions()
        if next_node not in actions:

            return(
                self.current_node,
                -10,
                False
            )

        old_distance = self.distance_to_goal()

        self.current_node = next_node

        new_distance = self.distance_to_goal()

        done = (
            self.current_node
            == self.goal_node
        )
        if done:

            reward = 100

            print(
                f"GOAL REACHED: {self.goal_node}"
            )

        if new_distance < old_distance:

            reward = 1

        else:

            reward = -1

        return(
            self.current_node,
            reward,
            done
        )

    def a_star_route(self):

        path = nx.astar_path(
            self.graph,
            self.start_node,
            self.goal_node,
            weight="length"
        )

        return path

if __name__ == "__main__":
    env = ManhattanGraphEnv()

    state = env.reset()

    print("State:", state)

    print("Actions:")

    for action in env.get_actions():
        print(action)

    actions = env.get_actions()

    print(
        f"Actions available: {len(actions)}"
    )

    if actions:

        next_state, reward, done = env.step(
            actions[0]
        )

        print(next_state)
        print(reward)
        print(done)

    route = env.a_star_route()

    print("\nA* Route")

    print(
        f"Route Length: {len(route)} nodes")

    print(
        f"Goal Reached: {route[-1] == env.goal_node}"
    )

    print(
        f"Start: {env.start_node}"
    )

    print(
        f"Goal: {env.goal_node}"
    )

    print(
        route[:10]
    )