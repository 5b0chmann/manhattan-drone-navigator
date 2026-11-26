from pathlib import Path

import networkx as nx
import osmnx as ox

class NeighborhoodManhattanEnv:

    def __init__(
            self,
            radius=4
    ):

        graph_path = (
            Path(__file__).parent.parent
            / "maps"
            / "manhattan.graphml"
        )

        full_graph = ox.load_graphml(
            graph_path
        )

        center_node = list(
            full_graph.nodes
        )[0]

        self.graph = nx.ego_graph(
            full_graph,
            center_node,
            radius=radius
        )

        self.nodes = list(
            self.graph.nodes
        )

        self.start_node = (
            self.nodes[0]
        )

        self.goal_node = (
            self.nodes[-1]
        )

        self.current_node = (
            self.start_node
        )
    #------------------------------------
    # Environment
    #------------------------------------

    def reset(self):

        self.current_node = (
            self.start_node
        )

        return self.current_node

    def get_actions(self):

        return list(
            self.graph.neighbors(
                self.current_node
            )
        )

    def step(
            self,
            next_node
    ):

        actions = (
            self.get_actions()
        )

        if next_node not in actions:

            return (
                self.current_node,
                -10,
                False
            )
        
        self.current_node = (
            next_node
        )

        done = (
            self.current_node
            == self.goal_node
        )

        reward = -1

        if done:

            reward = 100

        return ( 
            self.current_node,
            reward,
            done
        )

    #------------------------------------
    # Analytics
    #------------------------------------

    def shortest_route(self):

        return nx.shortest_path(
            self.graph,
            self.start_node,
            self.goal_node
        )

    def info(self):

        print(
            "\n=== NEIGHBORHOOD ===\n"
        )

        print(
            f"Nodes: {len(self.nodes)}"
        )

        print(
            f"Start: {self.start_node}"
        )

        print(
            f"Goal : {self.goal_node}"
        )

        print(
            f"Shortest Route: "
            f"{len(self.shortest_route())}"
            f"nodes"
        )

if __name__ == "__main__":

    env = NeighborhoodManhattanEnv(
        radius=4
    )

    env.info()