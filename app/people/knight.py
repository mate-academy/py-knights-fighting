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
            if hasattr(item, "power"):
                setattr(self, "power", self.power + item.power)
            if hasattr(item, "hp"):
                setattr(self, "hp", self.hp + item.hp)
            if hasattr(item, "protection"):
                setattr(self, "hp", self.hp + item.protection)

    def fight(self, knight: Knight) -> None:
        self.hp = max(0, self.hp - knight.power)
        knight.hp = max(0, knight.hp - self.power)
