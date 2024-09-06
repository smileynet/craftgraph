import json
import logging
import networkx as nx
from typing import List, Dict, Tuple
from interfaces import IKnowledgeGraph

# Configure logging
logger = logging.getLogger(__name__)


class KnowledgeGraph(IKnowledgeGraph):
    def __init__(self, file_path: str):
        """
        Initialize the KnowledgeGraph by parsing the given JSON file.

        Args:
            file_path (str): Path to the JSON file containing the knowledge graph data.
        """
        self.graph, self.recipes = self._parse_knowledge_graph(file_path)
        logger.info(f"KnowledgeGraph initialized from {file_path}")

    def get_recipes(self) -> List[Dict[str, Dict[str, int]]]:
        """
        Get all recipes from the knowledge graph.

        Returns:
            List[Dict[str, Dict[str, int]]]: A list of recipes.
        """
        return self.recipes

    def _parse_knowledge_graph(self, file_path: str) -> Tuple[nx.DiGraph, Dict]:
        """
        Parse the JSON file to create a knowledge graph and extract recipes.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            Tuple[nx.DiGraph, Dict]: The parsed graph and recipes.

        Raises:
            FileNotFoundError: If the specified JSON file is not found.
            json.JSONDecodeError: If the JSON file is not properly formatted.
            KeyError: If the JSON file is missing required keys.
        """
        logger.info(f"Parsing knowledge graph from file: {file_path}")
        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            graph = nx.DiGraph()

            for node in data.get("nodes", []):
                graph.add_node(node["id"], **node.get("attributes", {}))
            logger.debug(f"Added {len(data.get('nodes', []))} nodes to the graph")

            for edge in data.get("edges", []):
                graph.add_edge(
                    edge["source"], edge["target"], **edge.get("attributes", {})
                )
            logger.debug(f"Added {len(data.get('edges', []))} edges to the graph")

            recipes = {
                recipe["id"]: {"input": recipe["input"], "output": recipe["output"]}
                for recipe in data.get("recipes", [])
            }
            logger.debug(f"Parsed {len(recipes)} recipes")

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

    def get_available_resources(self) -> List[str]:
        """
        Get all available resources and tools from the knowledge graph.

        Returns:
            List[str]: A list of resource and tool node IDs.
        """
        logger.info("Retrieving available resources and tools from the knowledge graph")
        try:
            resources_and_tools = [
                node
                for node, attr in self.graph.nodes(data=True)
                if attr.get("type") in ["resource", "tool"]
            ]
            logger.debug(
                f"Found {len(resources_and_tools)} available resources and tools"
            )
            return resources_and_tools
        except Exception as e:
            logger.exception(f"Error getting available resources and tools: {str(e)}")
            return []

    def get_crafting_recipes(self) -> Dict[str, Dict[str, Dict[str, int]]]:
        """
        Get organized crafting recipes from the knowledge graph.

        Returns:
            Dict[str, Dict[str, Dict[str, int]]]: A dictionary of crafting recipes, keyed by the output item.
        """
        logger.info("Organizing crafting recipes")
        try:
            crafting_recipes = {}
            for recipe_id, recipe_data in self.recipes.items():
                output_item = recipe_data["output"]["item"]
                crafting_recipes[output_item] = {
                    "input": recipe_data["input"],
                    "output": recipe_data["output"],
                }
            logger.debug(f"Organized {len(crafting_recipes)} crafting recipes")
            return crafting_recipes
        except Exception as e:
            logger.exception(f"Error organizing crafting recipes: {str(e)}")
            return {}


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        kg = KnowledgeGraph("data/knowledge_graph.json")
        resources = kg.get_available_resources()
        crafting_recipes = kg.get_crafting_recipes()
        logger.info(f"Available resources: {resources}")
        logger.info(f"Crafting recipes: {crafting_recipes}")
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
