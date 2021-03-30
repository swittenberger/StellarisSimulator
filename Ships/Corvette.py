from Ships.ship import Ship


class Corvette(Ship):
    def __init__(self, weapon, level=1, shields=1, armor=1, hull=1):
        super().__init__(weapon, level, shields, armor, hull)
