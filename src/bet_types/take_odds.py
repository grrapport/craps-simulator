from .bet import Bet


class TakeOdds(Bet):
    def __init__(self, base_amount, multiplier, point):
        self.multiplier = multiplier
        self.point = point
        self.amount = self.evaluate_multiplier() * base_amount
        self.payoff = self.get_payoff(self.point) * self.amount
        super().__init__(self.amount)

    def evaluate(self, dice_1, dice_2, roll_total):
        if roll_total == self.point:
            self.active = False
            return self.payoff
        if roll_total == 7:
            self.active = False
            return -self.amount
        return 0

    def evaluate_multiplier(self):
        if self.multiplier == "single":
            return 1
        if self.multiplier == "double":
            return 2
        if self.multiplier == "345":
            if self.point in [6, 8]:
                return 5
            if self.point in [5, 9]:
                return 4
            if self.point in [4, 10]:
                return 3
        if self.multiplier == "10":
            return 10
        if self.multiplier == "100":
            return 100

    @staticmethod
    def get_payoff(point):
        if point in [6, 8]:
            return 6/5
        if point in [5, 9]:
            return 3/2
        if point in [4, 10]:
            return 2

