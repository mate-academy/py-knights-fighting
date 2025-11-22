from __future__ import annotations
from typing import Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: Optional[dict],
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.preparation_to_battle()

    def apply_armour(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:

        if self.potion is not None:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def preparation_to_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def battle(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

    def check_is_fall(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def execute_duel(self, opponent: Knight) -> None:

        self.battle(opponent)

        self.check_is_fall()
        opponent.check_is_fall()
