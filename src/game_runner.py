"""
Class and utilities for running the game
"""
import random


class GameRunner:
    def __init__(self):
        self.roll_num = 0
        self.come_out = True
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

    def end(self):
        self.active = False

