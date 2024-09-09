import networkx as nx
from knowledge_graph_parser import parse_knowledge_graph
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

try:
    import pygraphviz as pgv

    PYGRAPHVIZ_AVAILABLE = True
    logger.info("PyGraphviz is available")
except ImportError:
    PYGRAPHVIZ_AVAILABLE = False
    logger.warning("PyGraphviz is not available. Some features may be limited.")


def display_graph_pygraphviz(graph):
    """Display the knowledge graph using PyGraphviz."""
    if not PYGRAPHVIZ_AVAILABLE:
        logger.error(
            "PyGraphviz is not available. Please install it to use this feature."
        )
        return

    logger.info("Starting to display knowledge graph using PyGraphviz")
    try:
        agraph = nx.nx_agraph.to_agraph(graph)
        logger.debug("Converted NetworkX graph to AGraph")

        color_map = {
            "resource": "lightgreen",
            "raw": "lightcoral",
            "tool": "lightskyblue",
            "item": "lightyellow",
        }

        logger.debug("Configuring node attributes")
        for node in agraph.nodes():
            node_type = graph.nodes[node].get("type", "unknown")
            node.attr["style"] = "filled"
            node.attr["fillcolor"] = color_map.get(node_type, "lightgrey")
            node.attr["fontsize"] = "10"
            node.attr["fontweight"] = "bold"

        logger.debug("Configuring edge attributes")
        for edge in agraph.edges():
            edge.attr["label"] = graph.edges[edge[0], edge[1]].get("action", "")

        logger.debug("Updating graph attributes")
        agraph.graph_attr.update(overlap="false", splines="true", rankdir="LR", K="0.6")

        logger.info("Laying out the graph")
        agraph.layout(prog="dot")

        output_file = "outputs/knowledge_graph_pygraphviz.png"
        logger.info(f"Drawing the graph to file: {output_file}")
        agraph.draw(output_file)

        logger.info(f"Graph saved as '{output_file}'")
        print(f"Graph saved as '{output_file}'")
    except Exception as e:
        logger.exception(f"An error occurred while displaying the graph: {str(e)}")


if __name__ == "__main__":
    try:
        logger.info("Parsing knowledge graph from JSON file")
        graph = parse_knowledge_graph("data/knowledge_graph.json")
        display_graph_pygraphviz(graph)
    except Exception as e:
        logger.exception(f"An error occurred in main execution: {str(e)}")
