import networkx as nx
import plotly.graph_objects as go
from knowledge_graph_parser import parse_knowledge_graph
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def display_graph_plotly(graph):
    """Display the knowledge graph using Plotly."""
    logger.info("Starting to display knowledge graph using Plotly")
    try:
        # Convert the directed graph to an undirected graph for display
        simple_graph = graph.to_undirected()

        # Create a spring layout
        logger.debug("Creating spring layout for the graph")
        pos = nx.spring_layout(simple_graph, k=0.7, iterations=50)

        # Create edge trace
        logger.debug("Creating edge trace")
        edge_x, edge_y, edge_text = [], [], []
        for edge in simple_graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            # Check both directions for the edge attributes in the original directed graph
            if edge in graph.edges:
                action = graph.edges[edge]["attributes"].get("action", "")
            elif (edge[1], edge[0]) in graph.edges:
                action = graph.edges[(edge[1], edge[0])]["attributes"].get("action", "")
            else:
                action = ""
            edge_text.append(f"{edge[0]} <-> {edge[1]}: {action}")

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=1.5, color="#888"),  # Increased line width
            hoverinfo="text",
            text=edge_text,
            mode="lines",
            opacity=0.7,  # Added some transparency
        )

        # Create node trace
        logger.debug("Creating node trace")
        node_x, node_y, node_text, node_colors = [], [], [], []
        for node in simple_graph.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(
                f"Node: {node}<br>Type: {graph.nodes[node]['attributes'].get('type', 'unknown')}"
            )
            node_colors.append(graph.nodes[node]["attributes"].get("type", "unknown"))

        color_map = {
            "resource": "#8FBC8F",  # Dark Sea Green
            "tool": "#6495ED",  # Cornflower Blue
            "raw": "#FFA07A",  # Light Salmon
            "unknown": "#D3D3D3",  # Light Gray
        }

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            hoverinfo="text",
            text=list(simple_graph.nodes()),
            hovertext=node_text,
            textposition="top center",
            marker=dict(
                showscale=False,
                color=[color_map.get(c, color_map["unknown"]) for c in node_colors],
                size=20,
                line_width=2,
                line=dict(color="white", width=0.5),
            ),
        )

        # Create the figure
        logger.debug("Creating the Plotly figure")
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title="Craft Graph",
                titlefont_size=16,
                showlegend=False,
                hovermode="closest",
                margin=dict(b=20, l=5, r=5, t=40),
                annotations=[
                    dict(
                        text="",
                        showarrow=False,
                        xref="paper",
                        yref="paper",
                        x=0.005,
                        y=-0.002,
                    )
                ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
            ),
        )

        # Add edge labels
        for edge in simple_graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            if edge in graph.edges:
                action = graph.edges[edge]["attributes"].get("action", "")
            elif (edge[1], edge[0]) in graph.edges:
                action = graph.edges[(edge[1], edge[0])]["attributes"].get("action", "")
            else:
                action = ""
            fig.add_annotation(
                x=(x0 + x1) / 2,
                y=(y0 + y1) / 2,
                text=action,
                showarrow=False,
                font=dict(size=10, color="#555"),
                bgcolor="white",
                opacity=0.8,
            )

        # Add a legend
        logger.debug("Adding legend to the figure")
        for node_type, color in color_map.items():
            fig.add_trace(
                go.Scatter(
                    x=[None],
                    y=[None],
                    mode="markers",
                    marker=dict(size=10, color=color),
                    legendgroup=node_type,
                    showlegend=True,
                    name=node_type.capitalize(),
                )
            )

        # Update layout for legend
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        # Show the plot
        logger.info("Displaying the Plotly figure")
        fig.show()

        # Write to file using Kaleido
        logger.info("Writing the figure to a file using Kaleido")
        try:
            fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            fig.write_image(
                "outputs/knowledge_graph_kaleido.png", engine="kaleido", scale=2
            )
            logger.info("Successfully wrote the figure to knowledge_graph.png")
        except Exception as e:
            logger.exception(f"Error writing figure to file: {str(e)}")
    except Exception as e:
        logger.exception(f"Error creating or displaying the plot: {str(e)}")


if __name__ == "__main__":
    try:
        file_path = "data/knowledge_graph.json"
        logger.info("Parsing knowledge graph from JSON file")
        graph = parse_knowledge_graph(file_path)
        display_graph_plotly(graph)
    except Exception as e:
        logger.exception(f"Error in main execution: {str(e)}")
