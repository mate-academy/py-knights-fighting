from __future__ import annotations

from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour: list[Armour] = []
        self.weapon: Weapon = None
        self.potion: Potion = None

    def set_protection(self, armours: list[Armour]) -> None:
        self.protection += sum(armour.protection for armour in armours)

    def increase_power(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def set_effect(self, potion: Potion) -> None:
        if potion:
            self.hp += potion.effect.get("hp", 0)
            self.power += potion.effect.get("power", 0)
            self.protection += potion.effect.get("protection", 0)

    def fight(self, opponent: Knight) -> None:
        self.hp = max(self.hp - (opponent.power - self.protection), 0)
        opponent.hp = max(opponent.hp - (self.power - opponent.protection), 0)

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0
