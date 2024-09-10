import json
import networkx as nx
from logger import logger


def parse_knowledge_graph(file_path):
    """
    Parse a JSON file to create a knowledge graph using NetworkX.

    This function reads a JSON file containing node and edge data,
    and constructs a directed graph representation of the knowledge graph.

    Args:
        file_path (str): Path to the JSON file containing the knowledge graph data.

    Returns:
        nx.DiGraph: A NetworkX directed graph representing the knowledge graph.

    Raises:
        FileNotFoundError: If the specified JSON file is not found.
        json.JSONDecodeError: If the JSON file is not properly formatted.
        KeyError: If the JSON file is missing required keys.
    """
    logger.debug(f"Parsing knowledge graph from file: {file_path}")
    try:
        # Read the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Create a new directed graph
        graph = nx.DiGraph()

        # Add nodes and edges from JSON data
        for node in data.get("nodes", []):
            # Add node with its attributes
            graph.add_node(node["id"], attributes=node["attributes"])
        logger.debug(f"Added {len(data.get('nodes', []))} nodes to the graph")

        for edge in data.get("edges", []):
            # Add edge with its attributes
            graph.add_edge(
                edge["source"], edge["target"], attributes=edge["attributes"]
            )
        logger.debug(f"Added {len(data.get('edges', []))} edges to the graph")

        logger.debug("Knowledge graph parsed successfully")
        return graph

    except FileNotFoundError:
        logger.debug(f"Knowledge graph file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        logger.debug(f"Invalid JSON format in {file_path}")
        raise
    except KeyError as e:
        logger.debug(f"Missing required key in JSON data: {str(e)}")
        raise


def get_available_resources(graph):
    """
    Get all available resources and tools from the knowledge graph.

    This function identifies all nodes in the graph that are marked as resources or tools.

    Args:
        graph (nx.DiGraph): A NetworkX directed graph representing the knowledge graph.

    Returns:
        list: A list of resource and tool node IDs.
    """
    logger.debug("Retrieving available resources and tools from the knowledge graph")
    try:
        # Filter nodes to include those with type 'resource' or 'tool'
        resources_and_tools = [
            node
            for node, attr in graph.nodes(data=True)
            if attr["attributes"].get("type") in ["resource", "tool"]
        ]
        logger.debug(f"Found {len(resources_and_tools)} available resources and tools")
        return resources_and_tools
    except Exception as e:
        logger.debug(
            f"An error occurred while getting available resources and tools: {str(e)}"
        )
        return []


if __name__ == "__main__":
    try:
        # Example usage
        graph = parse_knowledge_graph("data/knowledge_graph.json")
        resources = get_available_resources(graph)
        logger.debug(f"Available resources and tools: {resources}")
    except Exception as e:
        logger.debug(f"An error occurred: {str(e)}")
