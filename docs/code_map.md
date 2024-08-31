# Code Map

This code map provides a high-level overview of the CraftGraph project structure, highlighting the main classes and functions in each file.

## Source Files (src/)

### display_graph.py
Purpose: Visualize the knowledge graph structure.
- `display_graph(graph)`: Render the knowledge graph using matplotlib for visual inspection.

### game_interface.py
Purpose: Manage player interactions with the game.
- `GameInterface`: Coordinate game logic and player input/output.
  - `__init__(knowledge_graph_path)`: Initialize the game with a knowledge graph.
  - `display_available_resources()`: Show the player what resources can be gathered.
  - `gather_resource(choice)`: Allow the player to collect a chosen resource.
  - `display_inventory()`: Show the player what resources they have collected.
  - `run()`: Execute the main game loop, handling player choices.

### knowledge_graph_parser.py
Purpose: Parse and interpret the knowledge graph data.
- `parse_knowledge_graph(json_file_path)`: Convert JSON data into a NetworkX graph structure.
- `get_available_resources(graph)`: Extract resource nodes from the knowledge graph.

### resource_manager.py
Purpose: Handle resource-related operations in the game.
- `ResourceManager`: Manage the generation, collection, and replenishment of resources.
  - `__init__(knowledge_graph_path)`: Set up the resource system using a knowledge graph.
  - `_generate_resource_nodes(num_nodes=10)`: Create a set of random resource nodes.
  - `gather_resource(resource_id)`: Remove a resource from available nodes when collected.
  - `get_available_resource_nodes()`: Provide a list of resources the player can gather.
  - `replenish_resources(num_nodes=1)`: Add new resources to the available pool.

## Test Files (tests/)

### test_game_interface.py
Purpose: Verify the functionality of the GameInterface class.
- `game_interface()`: Create a GameInterface instance for testing.
- `test_game_interface_initialization(game_interface)`: Ensure proper GameInterface setup.
- `test_display_available_resources(game_interface, capsys)`: Check resource display functionality.
- `test_gather_resource(game_interface)`: Verify resource gathering mechanics.
- `test_gather_invalid_resource(game_interface, capsys)`: Ensure proper handling of invalid resource selection.
- `test_display_inventory(game_interface, capsys)`: Check inventory display functionality.
- `test_run_game_interface(mock_input, game_interface, capsys)`: Validate the main game loop behavior.

### test_knowledge_graph_parser.py
Purpose: Ensure correct parsing and interpretation of the knowledge graph.
- `test_graph_json(tmp_path)`: Create a sample knowledge graph for testing.
- `test_parse_knowledge_graph(test_graph_json)`: Verify correct parsing of knowledge graph data.
- `test_get_available_resources(test_graph_json)`: Ensure accurate extraction of resource nodes.

### test_resource_manager.py
Purpose: Validate the functionality of the ResourceManager class.
- `resource_manager()`: Create a ResourceManager instance for testing.
- `test_resource_manager_initialization(resource_manager)`: Verify proper ResourceManager setup.
- `test_generate_resource_nodes(resource_manager)`: Check random resource node generation.
- `test_gather_resource(resource_manager)`: Ensure correct resource gathering behavior.
- `test_gather_nonexistent_resource(resource_manager)`: Verify handling of non-existent resource gathering.
- `test_replenish_resources(resource_manager)`: Validate resource replenishment functionality.
