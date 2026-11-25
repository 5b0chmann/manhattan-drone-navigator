from pathlib import Path

import osmnx as ox

import networkx as nx

def load_graph():

    graph_path = (
        Path(__file__).parent
            / "manhattan.graphml"
    )

    return ox.load_graphml(graph_path)
    

def graph_statistics(graph):

    print(graph)
    
    print(f"Nodes: {len(graph.nodes)}")
    print(f"Edges: {len(graph.edges)}")

def inspect_graph(graph):

    first_node = list(graph.nodes)[0]

    print("\nExample node:")
    print(first_node)

    print("\nNode attributes:")
    print(graph.nodes[first_node])

def inspect_neighbors(graph):

    node = list(graph.nodes)[0]

    print("\nCurrent node:")
    print(node)

    print("\nConnected nodes:")

    for neighbor in graph.neighbors(node):
        print(neighbor)

def shortest_path_demo(graph):

    nodes = list(graph.nodes)

    origin = nodes[0]
    destination = nodes[100]

    path = nx.shortest_path(
        graph,
        origin,
        destination,
        weight="length"
    )

    route_length = nx.shortest_path_length(
        graph,
        origin,
        destination,
        weight="length"
    )

    print(f"Route length: {route_length:.2f} meters")

    print("\nShortest path")

    print(f"Origin: {origin}")
    print(f"Destination: {destination}")

    print(f"Path length: {len(path)}")

def inspect_path(graph):

    nodes = list(graph.nodes)

    origin = nodes[0]
    destination = nodes[100]

    path = nx.shortest_path(
        graph,
        origin,
        destination, 
        weight="length"
    )

    print("\nFirst five nodes:")

    for node in path[:5]:
        print(node)

    print("...")

def visualize_graph(graph):

    ox.plot_graph(
        graph,
        node_size=5
    )

def visualize_route(graph):

    nodes = list(graph.nodes)

    origin = nodes[0]
    destination = nodes[100]

    path = nx.shortest_path(
        graph,
        origin,
        destination,
        weight="length"
    )

    ox.plot_graph_route(
        graph,
        path,
        route_linewidth=3,
        node_size=0
    )
    
if __name__ == "__main__":

    graph = load_graph()

    graph_statistics(graph)

    inspect_graph(graph)

    inspect_neighbors(graph)

    shortest_path_demo(graph)

    inspect_path(graph)

    visualize_graph(graph)

    visualize_route(graph)
