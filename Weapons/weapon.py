import random


class Weapon:
    def __init__(self, level=1):
        self.level = level
        self.damaged = 1
        self.undamaged = 1
        self.range = ["Short"]
        self.target = "Armor"
        self.accuracy = 10
        self.calculate_damage()

    def calculate_damage(self):
        pass
