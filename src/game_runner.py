"""
Class and utilities for running the game
Right now, game runner continues for one shooter
after a shooter is done,
active is set to False
"""
import random


class GameRunner:
    def __init__(self):
        self.roll_num = 0
        self.come_out = True
        self.point = None
        self.last_roll = None
        self.last_roll_dice_1 = None
        self.last_roll_dice_2 = None
        self.active = True

    def roll(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        self.roll_num += 1
        self.last_roll = dice_1 + dice_2
        self.last_roll_dice_1 = dice_1
        self.last_roll_dice_2 = dice_2
        if self.come_out:
            if self.last_roll in [2, 3, 7, 11, 12]:
                return
            else:
                self.come_out = False
                self.point = self.last_roll
        else:
            if self.last_roll == 7:
                self.come_out = True
                self.end()
            if self.last_roll == self.point:
                self.point = None
                self.come_out = True

    def end(self):
        self.active = False

