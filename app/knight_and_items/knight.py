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

        # wear armour
        for new_armour_dict in stats.get("armour"):
            new_armour = Armour(new_armour_dict)
            if not any([worn_armour.part == new_armour.part
                        for worn_armour in self.armour]):
                self.armour.append(new_armour)
                self.protection += new_armour.protection

        # wear weapon
        if stats.get("weapon") is not None:
            self.weapon = Weapon(stats.get("weapon"))
            self.power += self.weapon.power

        # use potion
        if stats.get("potion") is not None:
            self.potion = Potion(stats.get("potion"))
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
