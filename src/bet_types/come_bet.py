"""
Bet class for come bets
"""
from .bet import Bet
from .take_odds import TakeOdds


class Come(Bet):
    def __init__(self, amount, odds=None):
        super().__init__(amount)
        self.point = None
        self.come_out = True
        self.odds_strategy = odds
        self.odds = None

    def evaluate(self, dice_1, dice_2, roll_total):
        if self.come_out:
            if roll_total in [7, 11]:
                return self.amount
            elif roll_total in [2, 3, 12]:
                self.active = False
                return -self.amount
            else:
                self.point = roll_total
                self.odds = TakeOdds(self.amount, self.odds_strategy, self.point)
                self.come_out = False
                return 0
        if not self.come_out:
            if roll_total == 7:
                self.active = False
                result = self.odds.evaluate(dice_1, dice_2, roll_total) - self.amount
                return result
            if roll_total == self.point:
                result = self.odds.evaluate(dice_1, dice_2, roll_total) + self.amount
                self.come_out = True
                self.odds = None
                return result
        return 0

