"""
This file contains the parent class for all bet types
It will feature some essential methods and parameters
"""


class Bet:
    def __init__(self, amount):
        self.amount = amount
        self.active = True

    def evaluate(self, dice_1, dice_2, roll_total):
        raise NotImplementedError

