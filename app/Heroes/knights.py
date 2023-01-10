from __future__ import annotations

from app.Ammunition.armours import Armour
from app.Ammunition.potions import Potion
from app.Ammunition.weapons import Weapon


class Knight:

    knights = {}

    def __init__(self, name: str, power: int,
                 health: int, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.protection = protection
        self.weapon = None
        self.armour = []
        self.potion = None
        self.__class__.knights[self.name] = self

    def weapon_addition_stats(self, weapon: Weapon) -> None:
        Knight.knights[self.name].power += Weapon.weapons[weapon.name].power
        Knight.knights[self.name].weapon = weapon.name

    def armour_addition_stats(self, armour: list | Armour) -> None:
        for arm in armour:
            Knight.knights[self.name].armour.append(arm.part)
            Knight.knights[self.name].protection += arm.protection

    def potion_addition_stats(self, potion: Potion) -> None:
        Knight.knights[self.name].power += Potion.potions[potion.name].power
        Knight.knights[self.name].health += potion.health
        Knight.knights[self.name].protection += potion.protection
        Knight.knights[self.name].potion = potion.name

    def geather_addition_stats(self, weapon: Weapon,
                               armour: list | None,
                               potion: Potion | None) -> None:

        self.weapon_addition_stats(weapon)
        if armour is not None:
            self.armour_addition_stats(armour)
        if potion is not None:
            self.potion_addition_stats(potion)
