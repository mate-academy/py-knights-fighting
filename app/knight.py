from __future__ import annotations
from typing import Optional


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: Optional[dict] = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def knights_config(self) -> None:
        if self.armour:
            self.protection = sum([part.get("protection")
                                   for part in self.armour])
        self.power += self.weapon.get("power")
        if self.potion:
            if self.potion.get("effect").get("hp"):
                self.hp += self.potion.get("effect").get("hp")
            if self.potion.get("effect").get("power"):
                self.power += self.potion.get("effect").get("power")
            if self.potion.get("effect").get("protection"):
                self.protection += self.potion.get("effect").get("protection")

    def after_battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
