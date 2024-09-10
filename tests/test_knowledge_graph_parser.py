"""
This module contains unit tests for the knowledge_graph_parser module.

It tests the functionality of parsing knowledge graphs and retrieving available resources and tools.
"""

import json

import networkx as nx
import pytest

from knowledge_graph_parser import get_available_resources, parse_knowledge_graph


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
            {"id": "stone", "attributes": {"type": "resource"}},
            {"id": "iron", "attributes": {"type": "resource"}},
            {"id": "tree", "attributes": {"type": "raw"}},
            {"id": "stone_axe", "attributes": {"type": "tool"}},
        ],
        "edges": [
            {"source": "tree", "target": "wood", "attributes": {"action": "chop"}},
            {
                "source": "wood",
                "target": "stone_axe",
                "attributes": {"action": "craft"},
            },
            {
                "source": "stone",
                "target": "stone_axe",
                "attributes": {"action": "craft"},
            },
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
    assert graph.has_node("stone")
    assert graph.has_node("iron")
    assert graph.has_node("tree")
    assert graph.has_node("stone_axe")
    assert graph.has_edge("tree", "wood")
    assert graph.has_edge("wood", "stone_axe")
    assert graph.has_edge("stone", "stone_axe")
    assert graph.nodes["wood"]["attributes"]["type"] == "resource"
    assert graph.nodes["stone_axe"]["attributes"]["type"] == "tool"
    assert graph["tree"]["wood"]["attributes"]["action"] == "chop"
    assert graph["wood"]["stone_axe"]["attributes"]["action"] == "craft"


def test_get_available_resources(test_graph_json):
    """
    Test the get_available_resources function.

    This test verifies that the function correctly identifies and returns
    only the resource and tool nodes from the knowledge graph.
    """
    graph = parse_knowledge_graph(test_graph_json)
    resources_and_tools = get_available_resources(graph)

    assert "wood" in resources_and_tools
    assert "stone" in resources_and_tools
    assert "iron" in resources_and_tools
    assert "stone_axe" in resources_and_tools
    assert "tree" not in resources_and_tools
    assert len(resources_and_tools) == 4


def test_parse_knowledge_graph_file_not_found():
    """
    Test the parse_knowledge_graph function with a non-existent file.

    This test ensures that the function raises a FileNotFoundError when
    given a path to a non-existent file.
    """
    with pytest.raises(FileNotFoundError):
        parse_knowledge_graph("non_existent_file.json")


def test_parse_knowledge_graph_invalid_json(tmp_path):
    """
    Test the parse_knowledge_graph function with an invalid JSON file.

    This test ensures that the function raises a JSONDecodeError when
    given a file with invalid JSON content.
    """
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("{invalid json content}")

    with pytest.raises(json.JSONDecodeError):
        parse_knowledge_graph(invalid_json_file)
