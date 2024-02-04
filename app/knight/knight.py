from __future__ import annotations
from typing import Dict, Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Optional,
            weapon: Dict,
            potion: Dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.use_armour()
        self.use_weapon()
        if self.potion is not None:
            self.use_potion()

    def use_potion(self) -> None:
        self.power += self.potion["effect"].get("power", 0)
        self.protection += self.potion["effect"].get("protection", 0)
        self.hp += self.potion["effect"].get("hp", 0)

    def use_weapon(self) -> None:
        self.power += self.weapon["power"]

    def use_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

    def duel(self, other: Knight) -> None:
        self.hp -= max(0, other.power - self.protection)
        other.hp -= max(0, self.power - other.protection)

        self.hp = max(0, self.hp)
        other.hp = max(0, other.hp)
