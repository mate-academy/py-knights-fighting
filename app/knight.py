from __future__ import annotations

from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: Weapon, potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for arm in self.armour:
            self.protection += arm.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        pass
