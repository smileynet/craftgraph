import json
import logging

from resource_manager import ResourceManager

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class GameInterface:
    """
    Provides a command-line interface for interacting with the game.

    This class manages the game's main loop, resource gathering, and inventory display.
    """

    def __init__(self, knowledge_graph_path):
        """
        Initialize the GameInterface with a ResourceManager.

        Args:
            knowledge_graph_path (str): Path to the JSON file containing the knowledge graph data.
        """
        logger.info(
            f"Initializing GameInterface with knowledge graph: {knowledge_graph_path}"
        )
        try:
            self.resource_manager = ResourceManager(knowledge_graph_path)
            self.inventory = {}
            logger.info("GameInterface initialized successfully")
        except FileNotFoundError:
            logger.error(f"Knowledge graph file not found at {knowledge_graph_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in {knowledge_graph_path}")
            raise

    def get_gatherable_resources(self):
        """
        Get the list of resources that can be gathered (excluding craftable items).

        Returns:
            list: A list of gatherable resource IDs.
        """
        all_resources = self.resource_manager.get_available_resource_nodes()
        return [r for r in all_resources if not self.resource_manager.is_craftable(r)]

    def display_available_resources(self):
        """
        Display the list of available gatherable resources to the player.
        """
        resources = self.get_gatherable_resources()
        logger.debug(f"Displaying {len(resources)} available gatherable resources")
        print("Available resources:")
        for i, resource in enumerate(resources, 1):
            print(f"{i}. {resource}")

    def gather_resource(self, choice):
        """
        Attempt to gather a resource based on the player's choice.

        Args:
            choice (int): The index of the resource to gather, as displayed to the player.
        """
        resources = self.get_gatherable_resources()
        try:
            if 1 <= choice <= len(resources):
                resource = resources[choice - 1]
                logger.info(f"Attempting to gather resource: {resource}")
                gathered = self.resource_manager.gather_resource(resource)
                if gathered:
                    self.inventory[resource] = self.inventory.get(resource, 0) + 1
                    logger.info(f"Resource gathered successfully: {resource}")
                    print(f"You gathered {resource}!")
                else:
                    logger.warning(f"Failed to gather resource: {resource}")
                    print("Failed to gather resource.")
            else:
                logger.warning(f"Invalid resource choice: {choice}")
                print("Invalid choice.")
        except Exception as e:
            logger.exception(
                f"An error occurred while gathering the resource: {str(e)}"
            )
            print(f"An error occurred while gathering the resource: {str(e)}")

    def display_inventory(self):
        """
        Display the player's current inventory.
        """
        logger.debug("Displaying player inventory")
        print("Inventory:")
        for item, count in self.inventory.items():
            print(f"{item}: {count}")

    def run(self):
        """
        Run the main game loop, allowing the player to interact with the game.
        """
        logger.info("Starting the main game loop")
        while True:
            # Display the main menu
            print("\n1. View available resources")
            print("2. Gather resource")
            print("3. View inventory")
            print("4. Quit")
            choice = input("Enter your choice: ")
            logger.debug(f"Player chose option: {choice}")

            # Process the player's choice
            if choice == "1":
                self.display_available_resources()
            elif choice == "2":
                self.display_available_resources()
                try:
                    resource_choice = int(
                        input("Enter the number of the resource to gather: ")
                    )
                    self.gather_resource(resource_choice)
                except ValueError:
                    logger.warning("Invalid input for resource gathering")
                    print("Invalid input. Please enter a number.")
            elif choice == "3":
                self.display_inventory()
            elif choice == "4":
                logger.info("Player chose to quit the game")
                break
            else:
                logger.warning(f"Invalid menu choice: {choice}")
                print("Invalid choice. Please try again.")

        logger.info("Game loop ended")


if __name__ == "__main__":
    # Create and run the game interface
    try:
        filepath = "data/knowledge_graph.json"
        logger.info("Starting the game")
        game = GameInterface(filepath)
        game.run()
    except Exception as e:
        logger.exception(f"An error occurred while starting the game: {str(e)}")
        print(f"An error occurred while starting the game: {str(e)}")
