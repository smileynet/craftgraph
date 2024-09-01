import networkx as nx
from knowledge_graph_parser import parse_knowledge_graph

try:
    import igraph as ig
    import cairo

    IGRAPH_AVAILABLE = True
except ImportError:
    IGRAPH_AVAILABLE = False


def networkx_to_igraph(nx_graph):
    """Convert a NetworkX graph to an igraph Graph."""
    ig_graph = ig.Graph(directed=nx_graph.is_directed())
    ig_graph.add_vertices(list(nx_graph.nodes()))
    ig_graph.add_edges(list(nx_graph.edges()))

    # Copy node attributes
    for attr in nx_graph.nodes(data=True):
        for key, value in attr[1].items():
            ig_graph.vs[attr[0]][key] = value

    # Copy edge attributes
    for u, v, attr in nx_graph.edges(data=True):
        edge = ig_graph.es.find(_source=u, _target=v)
        for key, value in attr.items():
            edge[key] = value

    return ig_graph


def display_graph_igraph(graph):
    """Display the knowledge graph using igraph."""
    if not IGRAPH_AVAILABLE:
        print(
            "igraph or cairo is not available. Please install them to use this feature."
        )
        return

    ig_graph = networkx_to_igraph(graph)

    color_map = {
        "resource": "lightgreen",
        "raw": "lightcoral",
        "tool": "lightskyblue",
        "item": "lightyellow",
    }

    # Set node colors and labels
    ig_graph.vs["color"] = [
        color_map.get(node.get("type"), "lightgrey") for node in ig_graph.vs
    ]
    ig_graph.vs["label"] = ig_graph.vs["_nx_name"]

    # Set edge labels
    ig_graph.es["label"] = ig_graph.es["action"]

    # Create the plot
    visual_style = {
        "vertex_size": 50,
        "vertex_label_size": 12,
        "edge_curved": 0.2,
        "layout": ig_graph.layout_fruchterman_reingold(),
        "bbox": (800, 600),
        "margin": 50,
        "edge_label_size": 8,
    }

    plot = ig.plot(ig_graph, "knowledge_graph_igraph.png", **visual_style)
    print("Graph saved as 'knowledge_graph_igraph.png'")


if __name__ == "__main__":
    graph = parse_knowledge_graph("data/knowledge_graph.json")
    display_graph_igraph(graph)
