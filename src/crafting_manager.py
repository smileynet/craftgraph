from typing import Dict, List
from interfaces import IResourceManager, IKnowledgeGraph
import logging

# Configure logging
logger = logging.getLogger(__name__)


class CraftingManager:
    """
    Manages the crafting system, including resource checking and item crafting.
    """

    def __init__(
        self, resource_manager: IResourceManager, knowledge_graph: IKnowledgeGraph
    ):
        """
        Initialize the CraftingManager with a ResourceManager and KnowledgeGraph.

        Args:
            resource_manager (IResourceManager): The resource manager instance.
            knowledge_graph (IKnowledgeGraph): The knowledge graph instance.
        """
        self.resource_manager = resource_manager
        self.knowledge_graph = knowledge_graph
        logger.info("CraftingManager initialized")

    def check_resources(self, recipe: Dict[str, int]) -> bool:
        """
        Check if the player has the required resources for a recipe.

        Args:
            recipe (Dict[str, int]): A dictionary of resource names and required amounts.

        Returns:
            bool: True if the player has all required resources, False otherwise.
        """
        for resource, amount in recipe.items():
            if self.resource_manager.get_resource_amount(resource) < amount:
                logger.debug(f"Insufficient resource: {resource}")
                return False
        logger.debug("All required resources available")
        return True

    def craft_item(self, item: str, recipe: Dict[str, int]) -> bool:
        """
        Attempt to craft an item using the given recipe.

        Args:
            item (str): The name of the item to craft.
            recipe (Dict[str, int]): A dictionary of resource names and required amounts.

        Returns:
            bool: True if crafting was successful, False otherwise.
        """
        if not self.check_resources(recipe):
            logger.info(f"Crafting failed: insufficient resources for {item}")
            return False

        try:
            # Consume resources
            for resource, amount in recipe.items():
                self.resource_manager.remove_resource(resource, amount)

            # Add crafted item to inventory
            self.resource_manager.add_resource(item, 1)
            logger.info(f"Successfully crafted: {item}")
            return True
        except Exception as e:
            logger.error(f"Error during crafting of {item}: {str(e)}")
            return False

    def get_available_recipes(self) -> List[Dict[str, Dict[str, int]]]:
        """
        Get a list of available recipes from the knowledge graph.

        Returns:
            List[Dict[str, Dict[str, int]]]: A list of recipes, where each recipe is a
            dictionary with the item name as the key and a dictionary of required
            resources and their amounts as the value.
        """
        try:
            recipes = self.knowledge_graph.get_recipes()
            logger.debug(f"Retrieved {len(recipes)} recipes")
            return recipes
        except Exception as e:
            logger.error(f"Error retrieving recipes: {str(e)}")
            return []
