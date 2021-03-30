class Combat:
    def __init__(self, side_a: list, side_b: list):
        """
        Calculates the result of a combat
        :param side_a: List of ships you want to use for side A
        :param side_b: List of ships you want to use for side B
        """
        self.side_a = side_a
        self.side_b = side_b
        self.ranges = ["Long", "Medium", "Short", "RapidFire"]

    def execute(self):
        number_of_ships_a = 0
        number_of_ships_b = 0
        ship_a_results = dict()
        counter = 0
        # Go through each range and fire

        for fire_range in self.ranges:
            for attack in range(1, len(self.side_a)):
                if fire_range in self.side_a[attack].weapon.range:
                    pass
