import networkx as nx
from knowledge_graph_parser import parse_knowledge_graph

try:
    import pygraphviz as pgv

    PYGRAPHVIZ_AVAILABLE = True
except ImportError:
    PYGRAPHVIZ_AVAILABLE = False


def display_graph_pygraphviz(graph):
    """Display the knowledge graph using PyGraphviz."""
    if not PYGRAPHVIZ_AVAILABLE:
        print("PyGraphviz is not available. Please install it to use this feature.")
        return

    agraph = nx.nx_agraph.to_agraph(graph)

    color_map = {
        "resource": "lightgreen",
        "raw": "lightcoral",
        "tool": "lightskyblue",
        "item": "lightyellow",
    }

    for node in agraph.nodes():
        node_type = graph.nodes[node].get("type", "unknown")
        node.attr["style"] = "filled"
        node.attr["fillcolor"] = color_map.get(node_type, "lightgrey")
        node.attr["fontsize"] = "10"
        node.attr["fontweight"] = "bold"

    for edge in agraph.edges():
        edge.attr["label"] = graph.edges[edge[0], edge[1]].get("action", "")

    agraph.graph_attr.update(overlap="false", splines="true", rankdir="LR", K="0.6")
    agraph.layout(prog="dot")
    agraph.draw("knowledge_graph_pygraphviz.png")
    print("Graph saved as 'knowledge_graph.png'")


if __name__ == "__main__":
    graph = parse_knowledge_graph("data/knowledge_graph.json")
    display_graph_pygraphviz(graph)
