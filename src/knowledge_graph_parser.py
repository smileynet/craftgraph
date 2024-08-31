import json
import networkx as nx

def parse_knowledge_graph(json_file_path):
    """
    Parse a JSON file to create a knowledge graph using NetworkX.

    :param json_file_path: Path to the JSON file containing the knowledge graph data.
    :return: A NetworkX graph representing the knowledge graph.
    """
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    graph = nx.DiGraph()

    # Add nodes and edges from JSON data
    for node in data.get('nodes', []):
        graph.add_node(node['id'], **node.get('attributes', {}))

    for edge in data.get('edges', []):
        graph.add_edge(edge['source'], edge['target'], **edge.get('attributes', {}))

    return graph

def get_available_resources(graph):
    """
    Get all available resources from the knowledge graph.

    :param graph: A NetworkX graph representing the knowledge graph.
    :return: A list of resource node IDs.
    """
    return [node for node, attr in graph.nodes(data=True) if attr.get('type') == 'resource']
