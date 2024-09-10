from logger import logger
import random
from knowledge_graph_parser import get_available_resources, parse_knowledge_graph


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
        try:
            logger.debug(
                f"Initializing ResourceManager with graph: {knowledge_graph_path}"
            )
            self.graph = parse_knowledge_graph(knowledge_graph_path)
            self.resources = get_available_resources(self.graph)
            if not self.resources:
                logger.debug("No resources found in the knowledge graph")
                raise ValueError("No resources found in the knowledge graph")
            self.resource_nodes = self._generate_resource_nodes()
            logger.debug("ResourceManager initialized successfully")
        except Exception as e:
            logger.debug(f"Error initializing ResourceManager: {str(e)}")
            raise

    def _generate_resource_nodes(self, num_nodes=10):
        """
        Generate a list of random resource nodes.

        Args:
            num_nodes (int): Number of resource nodes to generate. Defaults to 10.

        Returns:
            list: A list of randomly chosen resource nodes.
        """
        try:
            logger.debug(f"Generating {num_nodes} resource nodes")
            return [random.choice(self.resources) for _ in range(num_nodes)]
        except IndexError:
            logger.debug("No resources available to generate nodes")
            return []

    def gather_resource(self, resource_id):
        """
        Attempt to gather a specific resource.

        Args:
            resource_id (str): The ID of the resource to gather.

        Returns:
            str or None: The gathered resource ID if successful, None otherwise.
        """
        try:
            if resource_id in self.resource_nodes:
                self.resource_nodes.remove(resource_id)  # Remove only one instance
                logger.debug(f"Resource gathered: {resource_id}")
                return resource_id
            logger.debug(f"Failed to gather resource: {resource_id} (not available)")
            return None
        except Exception as e:
            logger.debug(f"Error gathering resource: {str(e)}")
            return None

    def get_available_resource_nodes(self):
        """
        Get a copy of the current available resource nodes.

        Returns:
            list: A copy of the current available resource nodes.
        """
        logger.debug("Retrieving available resource nodes")
        return self.resource_nodes.copy()

    def replenish_resources(self, num_nodes=1):
        """
        Add new random resources to the available resource nodes.

        Args:
            num_nodes (int): Number of new resources to add. Defaults to 1.
        """
        try:
            logger.debug(f"Replenishing {num_nodes} resources")
            new_resources = [random.choice(self.resources) for _ in range(num_nodes)]
            self.resource_nodes.extend(new_resources)
            logger.debug(f"Resources added: {new_resources}")
        except IndexError:
            logger.debug("No resources available to replenish")
        except Exception as e:
            logger.debug(f"Error replenishing resources: {str(e)}")

    def is_craftable(self, resource_id):
        """
        Check if a resource is craftable.

        Args:
            resource_id (str): The ID of the resource to check.

        Returns:
            bool: True if the resource is craftable, False otherwise.
        """
        try:
            # Check if there are any incoming edges with the 'craft' action
            incoming_edges = self.graph.in_edges(resource_id, data=True)
            return any(
                edge[2]["attributes"].get("action") == "craft"
                for edge in incoming_edges
            )
        except Exception as e:
            logger.debug(f"Error checking if resource is craftable: {str(e)}")
            return False


if __name__ == "__main__":
    try:
        # Example usage
        resource_manager = ResourceManager("data/knowledge_graph.json")
        logger.debug(
            f"Available resources: {resource_manager.get_available_resource_nodes()}"
        )

        # Try gathering a resource
        resource_to_gather = resource_manager.get_available_resource_nodes()[0]
        gathered = resource_manager.gather_resource(resource_to_gather)
        logger.debug(f"Gathered resource: {gathered}")

        # Replenish resources
        resource_manager.replenish_resources(2)
        logger.debug(
            f"Resources after replenishment: {resource_manager.get_available_resource_nodes()}"
        )
    except Exception as e:
        logger.debug(f"An error occurred: {str(e)}")
