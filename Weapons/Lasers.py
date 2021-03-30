from Weapons.weapon import Weapon


class Lasers(Weapon):
    def __init__(self, level):
        super().__init__(level)
        self.damaged = 3
        self.undamaged = 2
        self.range = ["Short"]
        self.target = "Armor"
        self.accuracy = 9
        self.calculate_damage()

    def calculate_damage(self):
        if self.level == 2:
            self.undamaged = 3
            self.damaged = 4
        if self.level == 3:
            self.undamaged = 4
            self.damaged = 5
