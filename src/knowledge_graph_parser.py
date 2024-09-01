import json
import logging
import networkx as nx

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def parse_knowledge_graph(file_path):
    """
    Parse a JSON file to create a knowledge graph using NetworkX.

    This function reads a JSON file containing node and edge data,
    and constructs a directed graph representation of the knowledge graph.

    Args:
        file_path (str): Path to the JSON file containing the knowledge graph data.

    Returns:
        nx.DiGraph: A NetworkX directed graph representing the knowledge graph.
        dict: A dictionary of recipes parsed from the JSON data.

    Raises:
        FileNotFoundError: If the specified JSON file is not found.
        json.JSONDecodeError: If the JSON file is not properly formatted.
        KeyError: If the JSON file is missing required keys.
    """
    logger.info(f"Parsing knowledge graph from file: {file_path}")
    try:
        # Read the JSON file
        with open(file_path, "r") as file:
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

        # Parse recipes
        recipes = {}
        for recipe in data.get("recipes", []):
            recipes[recipe["id"]] = {
                "input": recipe["input"],
                "output": recipe["output"],
            }

        logger.info("Knowledge graph parsed successfully")
        return graph, recipes

    except FileNotFoundError:
        logger.error(f"Knowledge graph file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in {file_path}")
        raise
    except KeyError as e:
        logger.error(f"Missing required key in JSON data: {str(e)}")
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
    logger.info("Retrieving available resources and tools from the knowledge graph")
    try:
        # Filter nodes to include those with type 'resource' or 'tool'
        resources_and_tools = [
            node
            for node, attr in graph.nodes(data=True)
            if attr.get("type") in ["resource", "tool"]
        ]
        logger.debug(f"Found {len(resources_and_tools)} available resources and tools")
        return resources_and_tools
    except Exception as e:
        logger.exception(
            f"An error occurred while getting available resources and tools: {str(e)}"
        )
        return []


def get_crafting_recipes(G, recipes):
    """
    Get crafting recipes from the knowledge graph.

    This function organizes the recipes by their output item for easy access.

    Args:
        G (nx.DiGraph): A NetworkX directed graph representing the knowledge graph.
        recipes (dict): A dictionary of recipes parsed from the JSON data.

    Returns:
        dict: A dictionary of crafting recipes, keyed by the output item.
    """
    logger.info("Organizing crafting recipes")
    crafting_recipes = {}
    for recipe_id, recipe_data in recipes.items():
        output_item = recipe_data["output"]["item"]
        crafting_recipes[output_item] = {
            "input": recipe_data["input"],
            "output": recipe_data["output"],
        }
    logger.debug(f"Organized {len(crafting_recipes)} crafting recipes")
    return crafting_recipes


if __name__ == "__main__":
    try:
        # Example usage
        graph, recipes = parse_knowledge_graph("data/knowledge_graph.json")
        resources = get_available_resources(graph)
        crafting_recipes = get_crafting_recipes(graph, recipes)
        logger.info(f"Available resources: {resources}")
        logger.info(f"Crafting recipes: {crafting_recipes}")
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
