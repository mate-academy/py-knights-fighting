from equiption.armour import Armour
from equiption.potion import Potion
from equiption.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list = None,
                 weapon: dict = None,
                 potion: dict = None) -> None:

        self.name = name

        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.power = power + self.weapon.power

        self.hp = hp

        self.armour = Armour(armour)
        self.protection = (self.armour.helmet_protection
                           + self.armour.boots_protection
                           + self.armour.breastplate_protection)

        if potion is not None:
            pot = Potion(potion)
            self.potion = pot
            self.apply_potion(pot)

    def apply_potion(self, potion: Potion) -> None:
        self.hp += potion.hp_boost
        self.power += potion.power_boost
        self.protection += potion.protection_boost
