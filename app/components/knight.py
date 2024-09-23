from __future__ import annotations

from app.components.weapon import Weapon
from app.components.potion import Potion


class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list = [], weapon: Weapon = {},
                 potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __repr__(self) -> str:
        return str(self.__dict__)

    def get_protection(self) -> int:
        protection = sum(armour.protection for armour in
                         self.armour)
        if self.potion:
            protection += self.potion.effect.protection or 0
            self.hp += self.potion.effect.hp

        return protection

    def get_power(self) -> int:
        power = self.power + self.weapon.power
        if self.potion:
            power += self.potion.effect.power

        return power

    def fight(self, other: Knight) -> None:
        first_knight_power = self.get_power()
        first_knight_protection = self.get_protection()
        second_knight_power = other.get_power()
        second_knight_protection = other.get_protection()

        self.hp -= second_knight_power - first_knight_protection
        other.hp -= first_knight_power - second_knight_protection

    def death_check(self) -> None:
        if self.hp <= 0:
            self.hp = 0
