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

    @classmethod
    def completed_stats(cls) -> None:
        for name in cls.knights:
            print(f"The knight's name: {name}")
            print(f"Power: {cls.knights[name].power}")
            print(f"Health: {cls.knights[name].health}")
            print(f"Protection: {cls.knights[name].protection}")
            print(f"Weapon: {cls.knights[name].weapon}")
            print(f"Armour: {cls.knights[name].armour}")
            print(f"Used potion: {cls.knights[name].potion}")
            print("-" * 20)


# lancelot = Knight("Lancelot", power=35, health=100)
# lancelot.geather_addition_stats(Weapon.weapons["Metal Sword"], None, None)
# artur = Knight("Artur", power=45, health=75)
# artur.geather_addition_stats(Weapon.weapons["Two-handed Sword"],
#                              [Armour.armours["helmet"],
#                              Armour.armours["breastplate20"],
#                              Armour.armours["boots"]], None)
# mordred = Knight("Mordred", power=30, health=90)
# mordred.geather_addition_stats(Weapon.weapons["Poisoned Sword"],
#                                [Armour.armours["breastplate15"],
#                                 Armour.armours["boots"]],
#                                Potion.potions["Berserk"])
# red_knight = Knight("Red Knight", power=40, health=70)
# red_knight.geather_addition_stats(Weapon.weapons["Sword"],
#                                   [Armour.armours["breastplate25"]],
#                                   Potion.potions["Blessing"])
