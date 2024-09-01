import networkx as nx
import matplotlib.pyplot as plt
from knowledge_graph_parser import parse_knowledge_graph


def display_graph_matplotlib(graph):
    """Display the knowledge graph using NetworkX and Matplotlib."""
    plt.clf()  # Clear the current figure

    pos = nx.spring_layout(graph, k=0.5, iterations=50, seed=42)

    color_map = {
        "resource": "lightgreen",
        "raw": "lightcoral",
        "tool": "lightskyblue",
        "item": "lightyellow",
    }

    node_colors = [
        color_map.get(graph.nodes[node].get("type"), "lightgrey")
        for node in graph.nodes()
    ]

    plt.figure(figsize=(12, 8))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=3000,
        font_size=8,
        font_weight="bold",
    )

    edge_labels = nx.get_edge_attributes(graph, "action")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    plt.title("Knowledge Graph (Matplotlib)", fontsize=16)
    plt.axis("off")
    plt.tight_layout()


if __name__ == "__main__":
    graph = parse_knowledge_graph("data/knowledge_graph.json")
    display_graph_matplotlib(graph)
    plt.show()
