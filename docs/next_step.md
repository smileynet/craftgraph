# Next Step: Implementing the Crafting System

## Objective
Enable players to craft items using gathered resources.

## Tasks

1. **Define Crafting Recipes in Knowledge Graph**:
   - Update the knowledge graph structure to include crafting recipes.
   - Add edges between resource nodes and craftable item nodes with "craft" attributes.
   - Ensure the `parse_knowledge_graph` function can interpret these new relationships.

2. **Implement Crafting Logic**:
   - Create a new `CraftingManager` class to handle crafting operations.
   - Implement a method to check if a player has the required resources for a recipe.
   - Add functionality to consume resources and produce crafted items.

3. **Update Game Interface**:
   - Add a new method `display_crafting_options` to show available recipes.
   - Implement a `craft_item` method to allow players to craft items.
   - Integrate crafting options into the main game loop.

4. **Modify Resource Manager**:
   - Update the `ResourceManager` to handle both raw resources and crafted items.
   - Implement methods to add crafted items to the available resources.

5. **Enhance Inventory System**:
   - Modify the inventory to distinguish between raw resources and crafted items.
   - Implement methods to add and remove crafted items from the inventory.

## Implementation Plan

1. Start by updating the knowledge graph JSON file to include crafting recipes.
2. Modify the `knowledge_graph_parser.py` to parse and return crafting recipes.
3. Create `crafting_manager.py` and implement the `CraftingManager` class.
4. Update `game_interface.py` to include crafting-related methods and options.
5. Modify `resource_manager.py` to handle crafted items.
6. Update the main game loop to include crafting options.

## Testing Plan

1. Add unit tests for the new `CraftingManager` class in `test_crafting_manager.py`.
2. Update `test_knowledge_graph_parser.py` to include tests for parsing crafting recipes.
3. Modify `test_game_interface.py` to test the new crafting-related methods.
4. Update `test_resource_manager.py` to include tests for handling crafted items.

## Expected Outcome
Players should be able to:
- View available crafting recipes
- Select a recipe and craft an item if they have the required resources
- See the crafted item appear in their inventory
- Use crafted items as resources for more complex recipes

## Next Action
Begin by updating the knowledge graph JSON file to include sample crafting recipes, then move on to modifying the `knowledge_graph_parser.py` to handle these new relationships.