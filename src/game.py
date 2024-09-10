from logger import logger
from resource_manager import ResourceManager


class GameInterface:
    def __init__(self, knowledge_graph_path):
        logger.debug(
            f"Initializing GameInterface with knowledge graph: {knowledge_graph_path}"
        )
        self.resource_manager = ResourceManager(knowledge_graph_path)
        self.inventory = {}
        logger.debug("GameInterface initialized successfully")

    def display_available_resources(self):
        logger.debug("Displaying available resources")
        resources = self.resource_manager.get_available_resource_nodes()
        print("Available resources:")
        for i, resource in enumerate(resources, 1):
            print(f"{i}. {resource}")

    def gather_resource(self, choice):
        logger.debug(f"Attempting to gather resource at index: {choice}")
        resources = self.resource_manager.get_available_resource_nodes()
        if 1 <= choice <= len(resources):
            resource = resources[choice - 1]
            gathered = self.resource_manager.gather_resource(resource)
            if gathered:
                self.inventory[resource] = self.inventory.get(resource, 0) + 1
                logger.debug(f"Resource gathered successfully: {resource}")
                print(f"You gathered {resource}!")
            else:
                logger.debug(f"Failed to gather resource: {resource}")
                print("Failed to gather resource.")
        else:
            logger.debug(f"Invalid resource choice: {choice}")
            print("Invalid choice.")

    def display_inventory(self):
        logger.debug("Displaying player inventory")
        print("Inventory:")
        for item, count in self.inventory.items():
            print(f"{item}: {count}")

    def run(self):
        logger.debug("Starting the main game loop")
        while True:
            print("\n1. View available resources")
            print("2. Gather resource")
            print("3. View inventory")
            print("4. Quit")
            choice = input("Enter your choice: ")
            logger.debug(f"Player chose option: {choice}")

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
                    logger.debug("Invalid input for resource gathering")
                    print("Invalid input. Please enter a number.")
            elif choice == "3":
                self.display_inventory()
            elif choice == "4":
                logger.debug("Player chose to quit the game")
                break
            else:
                logger.debug(f"Invalid menu choice: {choice}")
                print("Invalid choice. Please try again.")

        logger.debug("Game loop ended")


# If you have a main block, keep it as is
if __name__ == "__main__":
    # Your existing main block code
    pass
