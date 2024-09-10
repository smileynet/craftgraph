"""
This module contains unit tests for the ResourceManager class.

It tests the initialization, resource generation, gathering, and replenishment functionalities.
"""

import pytest
from resource_manager import ResourceManager


@pytest.fixture
def resource_manager():
    """
    Fixture to create a ResourceManager instance for testing.

    Returns:
        ResourceManager: An instance of ResourceManager initialized with test data.
    """
    return ResourceManager("data/knowledge_graph.json")


def test_resource_manager_initialization(resource_manager):
    """
    Test the initialization of the ResourceManager.

    Ensures that the graph is loaded, resources are populated, and resource nodes are generated.
    """
    assert resource_manager.graph is not None
    assert len(resource_manager.resources) > 0
    assert len(resource_manager.resource_nodes) == 10


def test_get_resource_type_nodes(resource_manager):
    """
    Test the _get_resource_type_nodes method.

    Verifies that the method returns a non-empty list of resource type nodes.
    """
    resource_nodes = resource_manager._get_resource_type_nodes()
    assert len(resource_nodes) > 0
    assert all(
        resource_manager.graph.nodes[node]["attributes"]["type"] == "resource"
        for node in resource_nodes
    )


def test_generate_resource_nodes(resource_manager):
    """
    Test the _generate_resource_nodes method.

    Verifies that the correct number of nodes are generated and that they are
    valid resources from the knowledge graph.
    """
    nodes = resource_manager._generate_resource_nodes(5)
    assert len(nodes) == 5
    assert all(node in resource_manager.resources for node in nodes)


def test_gather_resource(resource_manager):
    """
    Test the gather_resource method.

    Checks if a resource can be gathered correctly, reducing its count in the
    available resources and returning the gathered resource.
    """
    initial_nodes = resource_manager.get_available_resource_nodes()
    resource_to_gather = initial_nodes[0]

    initial_count = initial_nodes.count(resource_to_gather)

    gathered = resource_manager.gather_resource(resource_to_gather)
    assert gathered == resource_to_gather

    new_nodes = resource_manager.get_available_resource_nodes()
    assert new_nodes.count(resource_to_gather) == initial_count - 1
    assert len(new_nodes) == len(initial_nodes) - 1


def test_gather_nonexistent_resource(resource_manager):
    """
    Test gathering a nonexistent resource.

    Ensures that attempting to gather a nonexistent resource returns None.
    """
    gathered = resource_manager.gather_resource("nonexistent_resource")
    assert gathered is None


def test_replenish_resources(resource_manager):
    """
    Test the replenish_resources method.

    Verifies that the specified number of resources are added to the available resources.
    """
    initial_count = len(resource_manager.get_available_resource_nodes())
    resource_manager.replenish_resources(3)
    assert len(resource_manager.get_available_resource_nodes()) == initial_count + 3


def test_get_available_resource_nodes(resource_manager):
    """
    Test the get_available_resource_nodes method.

    Verifies that the method returns a copy of the current available resource nodes.
    """
    available_nodes = resource_manager.get_available_resource_nodes()
    assert isinstance(available_nodes, list)
    assert len(available_nodes) == len(resource_manager.resource_nodes)
    assert available_nodes is not resource_manager.resource_nodes
