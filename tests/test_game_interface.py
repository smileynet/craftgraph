"""
This module contains unit tests for the GameInterface class.
"""

import pytest
from unittest.mock import patch
from game_interface import GameInterface  # pylint: disable=import-error


@pytest.fixture
def game_interface():
    """
    Fixture to create a GameInterface instance for testing.
    """
    return GameInterface("data/knowledge_graph.json")


def test_game_interface_initialization(game_interface):
    """
    Test the initialization of the GameInterface.
    """
    assert game_interface.resource_manager is not None
    assert game_interface.inventory == {}


def test_display_available_resources(game_interface, capsys):
    """
    Test the display of available resources.
    """
    game_interface.display_available_resources()
    captured = capsys.readouterr()
    assert "Available resources:" in captured.out
    assert len(captured.out.split("\n")) > 1


def test_gather_resource(game_interface):
    """
    Test gathering a valid resource.
    """
    initial_resources = game_interface.resource_manager.get_available_resource_nodes()
    game_interface.gather_resource(1)
    assert len(game_interface.inventory) == 1
    assert sum(game_interface.inventory.values()) == 1
    assert (
        len(game_interface.resource_manager.get_available_resource_nodes())
        == len(initial_resources) - 1
    )


def test_gather_invalid_resource(game_interface, capsys):
    """
    Test gathering an invalid resource.
    """
    game_interface.gather_resource(100)
    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out


def test_display_inventory(game_interface, capsys):
    """
    Test the display of the inventory.
    """
    game_interface.inventory = {"wood": 2, "stone": 1}
    game_interface.display_inventory()
    captured = capsys.readouterr()
    assert "Inventory:" in captured.out
    assert "wood: 2" in captured.out
    assert "stone: 1" in captured.out


@patch("builtins.input", side_effect=["1", "2", "1", "3", "4"])
def test_run_game_interface(mock_input, game_interface, capsys):
    """
    Test the main game loop of the GameInterface.
    """
    game_interface.run()
    captured = capsys.readouterr()
    assert "Available resources:" in captured.out
    assert "You gathered" in captured.out
    assert "Inventory:" in captured.out
