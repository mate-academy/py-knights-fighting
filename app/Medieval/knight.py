from __future__ import annotations
from typing import Optional

from app.Medieval.armour import Armour
from app.Medieval.potion import Potion
from app.Medieval.weapon import Weapon


class Knight:

    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Optional[Potion]) -> None:
        self.name = name
        self.power = power + weapon.power
        self.hp = hp
        self.armour = armour
        self.potion = potion
        self.weapon = weapon
        self.protection = 0
        self.apply_armour()
        self.apply_potion()

    def apply_armour(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour.protection

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.effect
            self.protection += effect.protection
            self.hp += effect.hp
            self.power += effect.power

    def __str__(self) -> str:
        return (f"{self.name}, POWER: {self.power}, "
                f"HP: {self.hp}, WEAPON: {self.weapon}, "
                f"ARMOUR: {self.armour_to_string()}")

    def duel(self, other: Knight) -> list:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0

        if other.hp <= 0:
            other.hp = 0

        return [self.hp, other.hp]

    def armour_to_string(self) -> str:
        armour_name_list = []
        for armour in self.armour:
            armour_name_list.append(f"{armour.part} - {armour.protection}")
        result = ", ".join(armour_name_list)
        return result
