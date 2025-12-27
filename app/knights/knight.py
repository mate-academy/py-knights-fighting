from typing import Optional

from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon


class DieException(Exception):
    pass


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armours: list[Armour] = []
        self.potion: Optional[Potion] = None

        if self.weapon and weapon.power < 0:
            raise ValueError("Weapon strength cannot be negative")

    def __str__(self) -> str:
        return self.name

    def use_potion(self, potion: Potion) -> None:
        self.potion = potion

    def wear_armour(self, armour: Armour) -> None:
        self.armours.append(armour)

    def protection(self) -> int:
        return sum([
            armour.protection for armour in self.armours
        ]) + (self.potion.get_effect("protection") if self.potion else 0)

    def total_hp(self) -> int:
        return sum([
            self.hp,
            self.potion.get_effect("hp") if self.potion else 0
        ])

    def total_power(self) -> int:
        return sum([
            self.power,
            self.potion.get_effect("power") if self.potion else 0,
            self.weapon.power
        ])
