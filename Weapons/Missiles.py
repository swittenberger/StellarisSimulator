from Weapons.weapon import Weapon


class Missiles(Weapon):
    def __init__(self, level):
        super().__init__(level)
        self.damaged = 4
        self.undamaged = 3
        self.range = ["Long"]
        self.target = "Armor"
        self.accuracy = 10
        self.calculate_damage()

    def calculate_damage(self):
        if self.level == 2:
            self.undamaged = 4
            self.damaged = 5
