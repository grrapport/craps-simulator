import pytest
from src.game_runner import GameRunner


def test_game_runner_roll():
    game = GameRunner()
    game.roll()
    assert game.last_roll <= 12
    assert game.last_roll >= 2



