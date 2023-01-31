from __future__ import annotations
from typing import Any
from app.player import consts


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon_power: int,
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        for item in armour:
            self.protection += item[consts.PROTECTION]

        self.power += weapon_power

    def duel(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.is_fall()
        other.is_fall()

    def is_fall(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def apply_potion(self, potion: Any) -> None:
        if potion is not None:
            for effect, value in potion["effect"].items():
                setattr(self,
                        effect,
                        getattr(self, effect) + value)
