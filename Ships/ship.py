import random

from Weapons.AncientMiningDroneWeapon import AncientMiningDroneWeapon
from Weapons.Lasers import Lasers
from Weapons.MassDriver import MassDriver
from Weapons.Missiles import Missiles


class Ship:
    def __init__(self, weapon, level=1, shields=1, armor=1, hull=1):
        self.shields = shields
        self.armor = armor
        self.hull = hull
        self.level = level
        self.weapon = self.weapon_selection(weapon)

    def weapon_selection(self, weapon):
        if weapon == "Missiles":
            return Missiles(self.level)
        if weapon == "MassDriver":
            return MassDriver(self.level)
        if weapon == "Lasers":
            return Lasers(self.level)
        if weapon == "AncientMiningDroneWeapon":
            return AncientMiningDroneWeapon()

    def fire(self):
        """
        aici calculezi modifiers and shit. In take damage vezi cat damage se face efectiv
        :return:
        """
        pass

    def take_damage(self, attacking_ship):
        """
        returns the damage it received
        receives the weapon that it will receive damage from
        :return:
        """
        roll = random.randint(1, attacking_ship.weapon.accuracy)
        full_damage = False
        damage_done = 0

        """
        Verify what weapon the targeting ship is using. 
        """
        if attacking_ship.weapon.target == "Armor":
            if self.armor == 0:
                full_damage = True
        elif attacking_ship.weapon.target == "Shield":
            if self.shields == 0:
                full_damage = True

        """
        Check the amount of damage done, based on the weapon above.
        """
        if roll <= attacking_ship.weapon.accuracy:
            if full_damage:
                if roll > attacking_ship.weapon.damaged:
                    damage_done = attacking_ship.weapon.damaged
                else:
                    damage_done = roll
            else:
                if roll > attacking_ship.weapon.undamaged:
                    damage_done = attacking_ship.weapon.undamaged
                else:
                    damage_done = roll
        """
        Check if the ship died, updated the values of shield/armor/hull
        """
        if damage_done >= self.shields:
            damage_done = damage_done - self.shields
            self.shields = 0
        else:
            self.shields = self.shields - damage_done
            damage_done = 0

        if damage_done >= self.armor:
            damage_done = damage_done - self.armor
            self.armor = 0
        else:
            self.armor = self.armor - damage_done
            damage_done = 0

        if damage_done >= self.hull:
            return "BOOM"
        else:
            self.hull = self.hull - damage_done

        return "ALIVE"
