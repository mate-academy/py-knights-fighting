from __future__ import annotations

from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def apply(self, *items: Armour | Weapon | Potion) -> None:
        for item in items:
            if isinstance(item, Armour):
                self.hp += item.protection
            elif isinstance(item, Weapon):
                self.power += item.power
            elif isinstance(item, Potion):
                self.hp += item.protection
                self.hp += item.hp
                self.power += item.power

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power
        knight.hp -= self.power
        if self.hp <= 0:
            self.hp = 0
        if knight.hp <= 0:
            knight.hp = 0
