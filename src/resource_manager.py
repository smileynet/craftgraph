import random
from knowledge_graph_parser import parse_knowledge_graph, get_available_resources


class ResourceManager:
    """
    Manages the game's resources based on a knowledge graph.

    This class handles the initialization, generation, gathering, and replenishment of resources.
    """

    def __init__(self, knowledge_graph_path):
        """
        Initialize the ResourceManager with a knowledge graph.

        Args:
            knowledge_graph_path (str): Path to the JSON file containing the knowledge graph data.
        """
        self.graph = parse_knowledge_graph(knowledge_graph_path)
        self.resources = get_available_resources(self.graph)
        self.resource_nodes = self._generate_resource_nodes()

    def _generate_resource_nodes(self, num_nodes=10):
        """
        Generate a list of random resource nodes.

        Args:
            num_nodes (int): Number of resource nodes to generate. Defaults to 10.

        Returns:
            list: A list of randomly chosen resource nodes.
        """
        return [random.choice(self.resources) for _ in range(num_nodes)]

    def gather_resource(self, resource_id):
        """
        Attempt to gather a specific resource.

        Args:
            resource_id (str): The ID of the resource to gather.

        Returns:
            str or None: The gathered resource ID if successful, None otherwise.
        """
        if resource_id in self.resource_nodes:
            self.resource_nodes.remove(resource_id)  # Remove only one instance
            return resource_id
        return None

    def get_available_resource_nodes(self):
        """
        Get a copy of the current available resource nodes.

        Returns:
            list: A copy of the current available resource nodes.
        """
        return self.resource_nodes.copy()

    def replenish_resources(self, num_nodes=1):
        """
        Add new random resources to the available resource nodes.

        Args:
            num_nodes (int): Number of new resources to add. Defaults to 1.
        """
        new_resources = [random.choice(self.resources) for _ in range(num_nodes)]
        self.resource_nodes.extend(new_resources)
