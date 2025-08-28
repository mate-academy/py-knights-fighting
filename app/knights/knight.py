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

    def drink_potion(self, potion: Potion) -> None:
        self.potion = potion

        if self.potion and self.hp + potion.hp < 0:
            raise DieException("Knight died using a potion!")

    def wear_armour(self, armour: Armour) -> None:
        self.armours.append(armour)

    def protection(self) -> int:
        return sum([
            armour.protection for armour in self.armours
        ]) + (self.potion.protection if self.potion else 0)

    def total_hp(self) -> int:
        return sum([self.hp, self.potion.hp if self.potion else 0])

    def total_power(self) -> int:
        return sum([
            self.power,
            self.potion.power if self.potion else 0,
            self.weapon.power
        ])
