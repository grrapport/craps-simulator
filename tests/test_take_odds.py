import pytest
from src.bet_types.take_odds import TakeOdds


def test_take_odds():
    odds = TakeOdds(10, "double", 6)
    odds.evaluate(1, 1, 2) == 0
    assert odds.amount == 20
    assert odds.payoff == 24
    assert odds.evaluate(3, 4, 7) == -20
    odds = TakeOdds(10, "345", 10)
    assert odds.amount == 30
    assert odds.payoff == 60
    assert odds.evaluate(5, 5, 10) == 60
    odds = TakeOdds(10, "10", 5)
    assert odds.amount == 100
    assert odds.payoff == 150
    assert odds.evaluate(3, 2, 5) == 150

