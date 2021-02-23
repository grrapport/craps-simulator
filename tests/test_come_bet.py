import pytest
from src.bet_types.come_bet import Come


def test_come_bet():
    bet = Come(10, None)
    assert bet.evaluate(3, 3, 6) == 0
    assert bet.evaluate(4, 3, 7) == -10
    bet = Come(10, "345")
    assert bet.evaluate(3, 3, 6) == 0
    assert bet.evaluate(4, 2, 6) == 70
