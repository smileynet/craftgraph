from typing import Dict, List
from resource_manager import ResourceManager
from knowledge_graph_parser import KnowledgeGraph


class CraftingManager:
    def __init__(
        self, resource_manager: ResourceManager, knowledge_graph: KnowledgeGraph
    ):
        self.resource_manager = resource_manager
        self.knowledge_graph = knowledge_graph

    def check_resources(self, recipe: Dict[str, int]) -> bool:
        """
        Check if the player has the required resources for a recipe.
        """
        for resource, amount in recipe.items():
            if self.resource_manager.get_resource_amount(resource) < amount:
                return False
        return True

    def craft_item(self, item: str, recipe: Dict[str, int]) -> bool:
        """
        Attempt to craft an item using the given recipe.
        Returns True if crafting was successful, False otherwise.
        """
        if not self.check_resources(recipe):
            return False

        # Consume resources
        for resource, amount in recipe.items():
            self.resource_manager.remove_resource(resource, amount)

        # Add crafted item to inventory
        self.resource_manager.add_resource(item, 1)
        return True

    def get_available_recipes(self) -> List[Dict[str, Dict[str, int]]]:
        """
        Get a list of available recipes from the knowledge graph.
        """
        return self.knowledge_graph.get_recipes()
