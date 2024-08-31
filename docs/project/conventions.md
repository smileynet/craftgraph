# CraftGraph Conventions

## Knowledge Graphs
- **Library**: Use the `networkx` library for creating and managing knowledge graphs, implemented in `src/CraftGraph/knowledge_graph_parser.py`.
- **Structure**: Define resources and crafting recipes as nodes and edges within the graph.
- **Best Practices**:
  - Ensure that each node represents a unique resource or item.
  - Use directed edges to represent dependencies or crafting recipes.
  - Keep the graph updated with any new resources or recipes added to the game.

## General Coding Conventions
- Follow the project's overall coding conventions as outlined in the main documentation.
- Ensure code readability and maintainability by adhering to established best practices.
