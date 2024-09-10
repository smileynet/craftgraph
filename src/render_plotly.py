from logger import logger
import networkx as nx
import plotly.graph_objects as go
from knowledge_graph_parser import parse_knowledge_graph


def create_spring_layout(nx_graph):
    logger.debug("Creating spring layout for the graph")
    return nx.spring_layout(nx_graph, k=0.7, iterations=50)


def create_edge_trace(nx_graph, pos):
    logger.debug("Creating edge trace")
    edge_x, edge_y, edge_text = [], [], []
    for edge in nx_graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        action = nx_graph.edges[edge]["attributes"].get("action", "")
        edge_text.append(f"{edge[0]} <-> {edge[1]}: {action}")

    return go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1.5, color="#888"),
        hoverinfo="text",
        text=edge_text,
        mode="lines",
        opacity=0.7,
    )


def create_node_trace(nx_graph, pos):
    logger.debug("Creating node trace")
    node_x, node_y, node_text, node_colors = [], [], [], []
    for node in nx_graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(
            f"Node: {node}<br>Type: {nx_graph.nodes[node]['attributes'].get('type', 'unknown')}"
        )
        node_colors.append(nx_graph.nodes[node]["attributes"].get("type", "unknown"))

    color_map = {
        "resource": "#8FBC8F",
        "tool": "#6495ED",
        "raw": "#FFA07A",
        "unknown": "#D3D3D3",
    }

    return go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        hoverinfo="text",
        text=list(nx_graph.nodes()),
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


def create_figure(edge_trace, node_trace):
    logger.debug("Creating the Plotly figure")
    return go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="Craft Graph",
            titlefont=dict(size=16),
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


def add_edge_labels(fig, nx_graph, pos):
    for edge in nx_graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        action = nx_graph.edges[edge]["attributes"].get("action", "")
        fig.add_annotation(
            x=(x0 + x1) / 2,
            y=(y0 + y1) / 2,
            text=action,
            showarrow=False,
            font=dict(size=10, color="#555"),
            bgcolor="white",
            opacity=0.8,
        )


def add_legend(fig):
    logger.debug("Adding legend to the figure")
    color_map = {
        "resource": "#8FBC8F",
        "tool": "#6495ED",
        "raw": "#FFA07A",
        "unknown": "#D3D3D3",
    }
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
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )


def save_figure(fig):
    logger.debug("Writing the figure to a file using Kaleido")
    try:
        fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
        fig.write_image(
            "outputs/knowledge_graph_kaleido.png", engine="kaleido", scale=2
        )
        logger.debug("Successfully wrote the figure to knowledge_graph.png")
    except Exception as error:
        logger.debug(f"Error writing figure to file: {str(error)}")


def display_graph_plotly(nx_graph):
    """Display the knowledge graph using Plotly."""
    logger.debug("Starting to display knowledge graph using Plotly")
    try:
        simple_graph = nx_graph.to_undirected()
        pos = create_spring_layout(simple_graph)
        edge_trace = create_edge_trace(simple_graph, pos)
        node_trace = create_node_trace(simple_graph, pos)
        fig = create_figure(edge_trace, node_trace)
        add_edge_labels(fig, nx_graph, pos)
        add_legend(fig)
        fig.show()
        save_figure(fig)
    except Exception as error:
        logger.debug(f"Error creating or displaying the plot: {str(error)}")


if __name__ == "__main__":
    try:
        file_path = "data/knowledge_graph.json"
        logger.debug("Parsing knowledge graph from JSON file")
        graph = parse_knowledge_graph(file_path)
        display_graph_plotly(graph)
    except Exception as e:
        logger.debug(f"Error in main execution: {str(e)}")
