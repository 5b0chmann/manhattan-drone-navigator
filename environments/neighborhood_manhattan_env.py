from pathlib import Path

import networkx as nx
import osmnx as ox

class NeighborhoodManhattanEnv:

    def __init__(
            self,
            radius=10
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

        self.route_nodes = set(
            self.shortest_route()
        )

        self.current_node = (
            self.start_node
        )

        self.otimal_route = (
            self.shortest_route()
        )

        self.visited_nodes = set()
    #------------------------------------
    # Environment
    #------------------------------------

    def reset(self):

        self.current_node = (
            self.start_node
        )

        self.visited_nodes = {
            self.start_node
        }

        return self.get_state()

    def get_actions(self):

        return list(
            self.graph.neighbors(
                self.current_node
            )
        )

    def get_state(self):

        try:

            distance = nx.shortest_path_length(
                self.graph,
                source=self.current_node,
                target=self.goal_node
            )

        except nx.NetworkXNoPath:

            distance = 9999

        return(
            self.current_node,
            distance
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

        guided_reward = False

        if next_node in self.otimal_route:

            guided_reward = True

        loop_penalty = False

        if next_node in self.visited_nodes:

            loop_penalty = True

        else:

            self.visited_nodes.add(
                next_node
            )

        done = (
            self.current_node
            == self.goal_node
        )

        reward = -1

        if loop_penalty:

            reward = -5

        if next_node in self.route_nodes:

            reward += 5

        if done:

            reward = 100

        return ( 
            self.get_state(),
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

        route = self.shortest_route()

        print(
            f"Shortest Route: "
            f"{len(route)} nodes"
        )

        print(
            "\nRoute:\n"
        )

        for node in route:

            print(node)

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
        radius=10
    )

    env.info()