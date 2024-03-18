from __future__ import annotations

from app.knight_bonuses.armour import Armour
from app.knight_bonuses.weapon import Weapon
from app.knight_bonuses.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def apply_armour(self, armour: dict) -> None:
        self.armour: list[Armour] = [
            Armour(armour_inst.get("knight"),
                   armour_inst.get("protection"))
            for armour_inst in armour
        ]
        if self.armour:
            self.protection = sum(
                armour_inst.protection
                for armour_inst in self.armour
            )
        else:
            self.protection = 0

    def apply_weapon(self, weapon: dict) -> None:
        self.weapon = Weapon(weapon.get("name"), weapon.get("power"))
        self.power += self.weapon.power

    def apply_potion(self, potion: dict) -> None:
        self.potion = Potion(potion.get("name"), potion.get("effect"))
        if self.potion.hp:
            self.hp += self.potion.hp
        if self.potion.power:
            self.power += self.potion.power
        if self.potion.protection:
            self.protection += self.potion.protection

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
