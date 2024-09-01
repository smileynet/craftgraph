import json
import logging
import networkx as nx

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


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
    logger.info(f"Parsing knowledge graph from file: {json_file_path}")
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
        logger.debug(f"Added {len(data.get('nodes', []))} nodes to the graph")

        for edge in data.get("edges", []):
            # Add edge with its attributes
            graph.add_edge(edge["source"], edge["target"], **edge.get("attributes", {}))
        logger.debug(f"Added {len(data.get('edges', []))} edges to the graph")

        logger.info("Knowledge graph parsed successfully")
        return graph

    except FileNotFoundError:
        logger.error(f"Knowledge graph file not found at {json_file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in {json_file_path}")
        raise
    except KeyError as e:
        logger.error(f"Missing required key in JSON data: {str(e)}")
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
    logger.info("Retrieving available resources from the knowledge graph")
    try:
        # Filter nodes to only include those with type 'resource'
        resources = [
            node
            for node, attr in graph.nodes(data=True)
            if attr.get("type") == "resource"
        ]
        logger.debug(f"Found {len(resources)} available resources")
        return resources
    except Exception as e:
        logger.exception(
            f"An error occurred while getting available resources: {str(e)}"
        )
        return []


if __name__ == "__main__":
    try:
        # Example usage
        graph = parse_knowledge_graph("data/knowledge_graph.json")
        resources = get_available_resources(graph)
        logger.info(f"Available resources: {resources}")
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
