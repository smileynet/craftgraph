from resource_manager import ResourceManager


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
        self.resource_manager = ResourceManager(knowledge_graph_path)
        self.inventory = {}

    def display_available_resources(self):
        """
        Display the list of available resources to the player.
        """
        resources = self.resource_manager.get_available_resource_nodes()
        print("Available resources:")
        for i, resource in enumerate(resources, 1):
            print(f"{i}. {resource}")

    def gather_resource(self, choice):
        """
        Attempt to gather a resource based on the player's choice.

        Args:
            choice (int): The index of the resource to gather, as displayed to the player.
        """
        resources = self.resource_manager.get_available_resource_nodes()
        if 1 <= choice <= len(resources):
            resource = resources[choice - 1]
            gathered = self.resource_manager.gather_resource(resource)
            if gathered:
                self.inventory[resource] = self.inventory.get(resource, 0) + 1
                print(f"You gathered {resource}!")
            else:
                print("Failed to gather resource.")
        else:
            print("Invalid choice.")

    def display_inventory(self):
        """
        Display the player's current inventory.
        """
        print("Inventory:")
        for item, count in self.inventory.items():
            print(f"{item}: {count}")

    def run(self):
        """
        Run the main game loop, allowing the player to interact with the game.
        """
        while True:
            # Display the main menu
            print("\n1. View available resources")
            print("2. Gather resource")
            print("3. View inventory")
            print("4. Quit")
            choice = input("Enter your choice: ")

            # Process the player's choice
            if choice == "1":
                self.display_available_resources()
            elif choice == "2":
                self.display_available_resources()
                resource_choice = int(
                    input("Enter the number of the resource to gather: ")
                )
                self.gather_resource(resource_choice)
            elif choice == "3":
                self.display_inventory()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Create and run the game interface
    game = GameInterface("data/knowledge_graph.json")
    game.run()
