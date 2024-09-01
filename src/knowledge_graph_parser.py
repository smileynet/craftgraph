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

    Raises:
        FileNotFoundError: If the specified JSON file is not found.
        json.JSONDecodeError: If the JSON file is not properly formatted.
        KeyError: If the JSON file is missing required keys.
    """
    try:
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

    except FileNotFoundError:
        print(f"Error: Knowledge graph file not found at {json_file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file_path}")
        raise
    except KeyError as e:
        print(f"Error: Missing required key in JSON data: {str(e)}")
        raise


def get_available_resources(graph):
    """
    Get all available resources from the knowledge graph.

    This function identifies all nodes in the graph that are marked as resources.

    Args:
        graph (nx.DiGraph): A NetworkX directed graph representing the knowledge graph.

    Returns:
        list: A list of resource node IDs.
    """
    try:
        # Filter nodes to only include those with type 'resource'
        return [
            node for node, attr in graph.nodes(data=True) if attr.get("type") == "resource"
        ]
    except Exception as e:
        print(f"An error occurred while getting available resources: {str(e)}")
        return []


if __name__ == "__main__":
    try:
        # Example usage
        graph = parse_knowledge_graph("data/knowledge_graph.json")
        resources = get_available_resources(graph)
        print("Available resources:", resources)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
