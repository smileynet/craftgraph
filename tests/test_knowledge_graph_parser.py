"""
This module contains unit tests for the knowledge_graph_parser module.

It tests the functionality of parsing knowledge graphs and retrieving available resources.
"""

import json
import pytest
import networkx as nx
from knowledge_graph_parser import parse_knowledge_graph, get_available_resources


@pytest.fixture
def test_graph_json(tmp_path):
    """
    Fixture to create a temporary JSON file containing test graph data.

    Returns:
        Path: Path to the temporary JSON file.
    """
    json_data = {
        "nodes": [
            {"id": "wood", "attributes": {"type": "resource"}},
            {"id": "plank", "attributes": {"type": "item"}},
            {"id": "stone", "attributes": {"type": "resource"}},
        ],
        "edges": [
            {"source": "wood", "target": "plank", "attributes": {"action": "craft"}}
        ],
    }
    json_file = tmp_path / "test_graph.json"
    json_file.write_text(json.dumps(json_data))
    return json_file


def test_parse_knowledge_graph(test_graph_json):
    """
    Test the parse_knowledge_graph function.

    This test ensures that the function correctly parses a JSON file into a NetworkX DiGraph,
    including proper node and edge creation with attributes.
    """
    graph = parse_knowledge_graph(test_graph_json)

    assert isinstance(graph, nx.DiGraph)
    assert graph.has_node("wood")
    assert graph.has_node("plank")
    assert graph.has_node("stone")
    assert graph.has_edge("wood", "plank")
    assert graph.nodes["wood"]["type"] == "resource"
    assert graph.nodes["plank"]["type"] == "item"
    assert graph["wood"]["plank"]["action"] == "craft"


def test_get_available_resources(test_graph_json):
    """
    Test the get_available_resources function.

    This test verifies that the function correctly identifies and returns
    only the resource nodes from the knowledge graph.
    """
    graph = parse_knowledge_graph(test_graph_json)
    resources = get_available_resources(graph)

    assert "wood" in resources
    assert "stone" in resources
    assert "plank" not in resources
    assert len(resources) == 2
