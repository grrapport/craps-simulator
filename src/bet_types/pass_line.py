"""
Bet class for pass line bets
"""
from .bet import Bet


class PassLine(Bet):
    def __init__(self, amount, come_out, point=None):
        super().__init__(amount)
        self.come_out = come_out
        self.point = point
        if self.come_out is False and self.point is None:
            raise Exception("Not come out roll, but no point defined")

    def evaluate(self, dice_1, dice_2, roll_total):
        if self.come_out:
            if roll_total in [7, 11]:
                print("hit 7 or 11, win 10")
                return self.amount
            elif roll_total in [2, 3, 12]:
                print("craps, lose 10")
                self.active = False
                return -self.amount
            else:
                self.point = roll_total
                print("point is " + str(self.point))
                self.come_out = False
                return 0
        if not self.come_out:
            if roll_total == 7:
                self.active = False
                print("Seven out, loses 10")
                return -self.amount
            if roll_total == self.point:
                print("hit the point win 10")
                return self.amount
        return 0


