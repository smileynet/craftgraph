import networkx as nx
import matplotlib.pyplot as plt
from knowledge_graph_parser import parse_knowledge_graph


def display_graph(graph):
    """
    Display the knowledge graph using matplotlib.

    This function visualizes the knowledge graph, coloring nodes based on their type
    and displaying edge labels for actions.

    Args:
        graph (nx.DiGraph): A NetworkX directed graph representing the knowledge graph.
    """
    # Set up the layout for the graph
    pos = nx.spring_layout(
        graph,
        k=0.6,  # Adjust spring constant for optimal distance between nodes
        seed=42,  # Set seed for reproducible layout
    )

    # Define color map for node types
    color_map = {
        "resource": "lightgreen",
        "raw": "lightcoral",
        "tool": "lightskyblue",
        "item": "lightyellow",
    }

    # Assign colors to nodes based on their type
    node_colors = [
        color_map.get(attr.get("type"), "lightgrey")
        for _, attr in graph.nodes(data=True)
    ]

    # Draw the graph
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=2000,
        node_color=node_colors,
        font_size=10,
        font_weight="bold",
    )

    # Add edge labels
    edge_labels = nx.get_edge_attributes(graph, "action")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Display the graph
    plt.show()


if __name__ == "__main__":
    # Load and parse the knowledge graph
    graph = parse_knowledge_graph("data/knowledge_graph.json")
    # Display the graph
    display_graph(graph)
