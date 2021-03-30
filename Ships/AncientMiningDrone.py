from Ships.ship import Ship


class AncientMiningDrone(Ship):
    def __init__(self):
        super().__init__(weapon="AncientMiningDroneWeapon")
        self.shields = 0
        self.armor = 4
        self.hull = 5

