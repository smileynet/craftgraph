from logger import logger
import graphviz
from knowledge_graph_parser import parse_knowledge_graph


def display_graph_graphviz(graph):
    """Display the knowledge graph using graphviz."""
    logger.debug("Starting to display knowledge graph using graphviz")
    try:
        dot = graphviz.Digraph(comment="Knowledge Graph")
        dot.attr(rankdir="LR", size="8,5")

        color_map = {
            "resource": "lightgreen",
            "raw": "lightcoral",
            "tool": "lightskyblue",
            "item": "lightyellow",
        }

        logger.debug("Adding nodes to the graph")
        for node, data in graph.nodes(data=True):
            node_type = data.get("type", "unknown")
            dot.node(
                str(node),
                str(node),
                style="filled",
                fillcolor=color_map.get(node_type, "lightgrey"),
                fontsize="10",
                fontweight="bold",
            )

        logger.debug("Adding edges to the graph")
        for source, target, data in graph.edges(data=True):
            action = data.get("action", "")
            dot.edge(str(source), str(target), label=action)

        output_file = "outputs/knowledge_graph_graphviz"
        logger.debug(f"Rendering the graph to file: {output_file}")
        dot.render(output_file, format="png", cleanup=True)

        logger.debug(f"Graph saved as '{output_file}.png'")
        print(f"Graph saved as '{output_file}.png'")
    except Exception as e:
        logger.debug(f"An error occurred while displaying the graph: {str(e)}")


if __name__ == "__main__":
    try:
        logger.debug("Parsing knowledge graph from JSON file")
        graph = parse_knowledge_graph("data/knowledge_graph.json")
        display_graph_graphviz(graph)
    except Exception as e:
        logger.debug(f"An error occurred in main execution: {str(e)}")
