from __future__ import annotations

from app.knight_and_items.weapon import Weapon
from app.knight_and_items.armour import Armour
from app.knight_and_items.potion import Potion


class Knight:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")
        self.hp = stats.get("hp")
        self.power = stats.get("power")

        self.armour = []
        self.protection = 0
        self.weapon = None
        self.potion = None

        self.wear_armour(stats.get("armour"))
        self.wear_weapon(stats.get("weapon"))
        self.use_potion(stats.get("potion"))

    def wear_armour(self, armours: list) -> None:
        for new_armour_dict in armours:
            new_armour = Armour(new_armour_dict)
            if not any([worn_armour.part == new_armour.part
                        for worn_armour in self.armour]):
                self.armour.append(new_armour)
                self.protection += new_armour.protection

    def wear_weapon(self, weapon: dict) -> None:
        if weapon is not None:
            self.weapon = Weapon(weapon)
            self.power += self.weapon.power

    def use_potion(self, potion: dict) -> None:
        if potion is not None:
            self.potion = Potion(potion)
            self.hp += self.potion.hp
            self.power += self.potion.power
            self.protection += self.potion.protection

    def fight(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp < 0:
            self.hp = 0
        other.hp -= self.power - other.protection
        if other.hp < 0:
            other.hp = 0
