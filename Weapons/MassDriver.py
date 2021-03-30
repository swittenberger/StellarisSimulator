from Weapons.weapon import Weapon


class MassDriver(Weapon):
    def __init__(self, level):
        super().__init__(level)
        self.damaged = 2
        self.undamaged = 1
        self.range = ["Medium", "RapidFire"]
        self.target = "Armor"
        self.accuracy = 7
        self.calculate_damage()

    def calculate_damage(self):
        if self.level == 2:
            self.undamaged = 2
            self.damaged = 3
        if self.level == 3:
            self.undamaged = 3
            self.damaged = 4
        if self.level == 5:
            self.undamaged = 4
            self.damaged = 7

