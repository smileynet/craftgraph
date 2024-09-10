"""
This module contains unit tests for the GameInterface class.
"""

from unittest.mock import patch

import pytest

from game import GameInterface


@pytest.fixture
def game():
    """
    Fixture to create a GameInterface instance for testing.
    """
    return GameInterface("data/knowledge_graph.json")


def test_game_interface_initialization(game):
    """
    Test the initialization of the GameInterface.
    """
    assert game.resource_manager is not None
    assert game.inventory == {}


def test_display_available_resources(game, capsys):
    """
    Test the display of available resources.
    """
    game.display_available_resources()
    captured = capsys.readouterr()
    assert "Available resources:" in captured.out
    assert len(captured.out.split("\n")) > 1


def test_gather_resource(game, capsys):
    """
    Test gathering a valid resource.
    """
    initial_resources = game.resource_manager.get_available_resource_nodes()
    game.gather_resource(1)
    captured = capsys.readouterr()
    assert "You gathered" in captured.out
    assert len(game.inventory) == 1
    assert sum(game.inventory.values()) == 1
    assert (
        len(game.resource_manager.get_available_resource_nodes())
        == len(initial_resources) - 1
    )


def test_gather_invalid_resource(game, capsys):
    """
    Test gathering an invalid resource.
    """
    game.gather_resource(100)
    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out


def test_display_inventory(game, capsys):
    """
    Test the display of the inventory.
    """
    game.inventory = {"wood": 2, "stone": 1}
    game.display_inventory()
    captured = capsys.readouterr()
    assert "Inventory:" in captured.out
    assert "wood: 2" in captured.out
    assert "stone: 1" in captured.out


@patch("builtins.input", side_effect=["1", "2", "1", "3", "4"])
def test_run_game_interface(mock_input, game, capsys):
    """
    Test the main game loop of the GameInterface.
    """
    game.run()
    captured = capsys.readouterr()
    assert "Available resources:" in captured.out
    assert "You gathered" in captured.out
    assert "Inventory:" in captured.out


def test_gather_resource_failure(game, capsys):
    """
    Test gathering a resource that fails to be gathered.
    """
    with patch.object(game.resource_manager, "gather_resource", return_value=None):
        game.gather_resource(1)
        captured = capsys.readouterr()
        assert "Failed to gather resource." in captured.out


@patch("builtins.input", side_effect=["invalid", "4"])
def test_run_game_interface_invalid_input(mock_input, game, capsys):
    """
    Test the main game loop with invalid input.
    """
    game.run()
    captured = capsys.readouterr()
    assert "Invalid choice. Please try again." in captured.out


@patch("builtins.input", side_effect=["2", "invalid", "4"])
def test_run_game_interface_invalid_gather_input(mock_input, game, capsys):
    """
    Test the main game loop with invalid input for resource gathering.
    """
    game.run()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter a number." in captured.out
