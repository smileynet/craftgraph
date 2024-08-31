import json
import pytest
import networkx as nx
from CraftGraph.knowledge_graph_parser import parse_knowledge_graph, get_available_resources

def test_parse_knowledge_graph(tmp_path):
    """
    Test the parse_knowledge_graph function to ensure it correctly parses
    a JSON file into a NetworkX directed graph.
    """
    # Create a temporary JSON file with test data
    json_data = {
        "nodes": [
            {"id": "wood", "attributes": {"type": "resource"}},
            {"id": "plank", "attributes": {"type": "item"}},
            {"id": "stone", "attributes": {"type": "resource"}}
        ],
        "edges": [
            {"source": "wood", "target": "plank", "attributes": {"action": "craft"}}
        ]
    }
    json_file = tmp_path / "test_graph.json"
    json_file.write_text(json.dumps(json_data))


    # Parse the JSON file
    graph = parse_knowledge_graph(json_file)

    # Get available resources
    resources = get_available_resources(graph)

    # Assertions to verify the resources
    assert "wood" in resources, "Resources should include 'wood'"
    assert "stone" in resources, "Resources should include 'stone'"
    assert "plank" not in resources, "Resources should not include 'plank'"
    assert isinstance(graph, nx.DiGraph), "Graph should be a directed graph"
    assert graph.has_node("wood"), "Graph should have a node 'wood'"
    assert graph.has_node("plank"), "Graph should have a node 'plank'"
    assert graph.has_edge("wood", "plank"), "Graph should have an edge from 'wood' to 'plank'"
    assert graph.nodes["wood"]["type"] == "resource", "Node 'wood' should have type 'resource'"
    assert graph.nodes["plank"]["type"] == "item", "Node 'plank' should have type 'item'"
    assert graph["wood"]["plank"]["action"] == "craft", "Edge from 'wood' to 'plank' should have action 'craft'"

def test_get_available_resources(tmp_path):
    """
    Test the parse_knowledge_graph function to ensure it correctly parses
    a JSON file into a NetworkX directed graph.
    """
    # Create a temporary JSON file with test data
    json_data = {
        "nodes": [
            {"id": "wood", "attributes": {"type": "resource"}},
            {"id": "plank", "attributes": {"type": "item"}}
        ],
        "edges": [
            {"source": "wood", "target": "plank", "attributes": {"action": "craft"}}
        ]
    }
    json_file = tmp_path / "test_graph.json"
    json_file.write_text(json.dumps(json_data))

    # Parse the JSON file
    graph = parse_knowledge_graph(json_file)

    # Assertions to verify the graph structure
    assert isinstance(graph, nx.DiGraph), "Graph should be a directed graph"
    assert graph.has_node("wood"), "Graph should have a node 'wood'"
    assert graph.has_node("plank"), "Graph should have a node 'plank'"
    assert graph.has_edge("wood", "plank"), "Graph should have an edge from 'wood' to 'plank'"
    assert graph.nodes["wood"]["type"] == "resource", "Node 'wood' should have type 'resource'"
    assert graph.nodes["plank"]["type"] == "item", "Node 'plank' should have type 'item'"
    assert graph["wood"]["plank"]["action"] == "craft", "Edge from 'wood' to 'plank' should have action 'craft'"
