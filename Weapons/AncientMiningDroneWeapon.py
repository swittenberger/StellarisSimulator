from Weapons.weapon import Weapon


class AncientMiningDroneWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.accuracy = 8
        self.undamaged = 3
        self.damaged = 5
        self.target = "Shield"
        self.range = ["Long", "Medium", "Short", "RapidFire"]

