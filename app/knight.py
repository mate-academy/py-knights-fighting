from __future__ import annotations

from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def get_power(self) -> int:
        return self.power + self.weapon.power

    def get_protection(self) -> int:
        return (
            self.protection + sum(armour.protection for armour in self.armours)
        )

    def use_potion(self) -> None:
        if not self.potion:
            return

        for key, value in self.potion.effect.items():
            if key == "power":
                self.power += value
            elif key == "hp":
                self.hp += value
            elif key == "protection":
                self.protection += value

    def duel_battle(self: Knight, other: Knight) -> None:
        self.hp -= other.get_power() - self.get_protection()
        if self.hp < 0:
            self.is_dead()

    def is_dead(self) -> None:
        self.hp = 0
