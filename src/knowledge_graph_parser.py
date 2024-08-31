import json
import networkx as nx


def parse_knowledge_graph(json_file_path):
    """
    Parse a JSON file to create a knowledge graph using NetworkX.

    This function reads a JSON file containing node and edge data,
    and constructs a directed graph representation of the knowledge graph.

    Args:
        json_file_path (str): Path to the JSON file containing the knowledge graph data.

    Returns:
        nx.DiGraph: A NetworkX directed graph representing the knowledge graph.
    """
    # Read the JSON file
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Create a new directed graph
    graph = nx.DiGraph()

    # Add nodes and edges from JSON data
    for node in data.get("nodes", []):
        # Add node with its attributes
        graph.add_node(node["id"], **node.get("attributes", {}))

    for edge in data.get("edges", []):
        # Add edge with its attributes
        graph.add_edge(edge["source"], edge["target"], **edge.get("attributes", {}))

    return graph


def get_available_resources(graph):
    """
    Get all available resources from the knowledge graph.

    This function identifies all nodes in the graph that are marked as resources.

    Args:
        graph (nx.DiGraph): A NetworkX directed graph representing the knowledge graph.

    Returns:
        list: A list of resource node IDs.
    """
    # Filter nodes to only include those with type 'resource'
    return [
        node for node, attr in graph.nodes(data=True) if attr.get("type") == "resource"
    ]
