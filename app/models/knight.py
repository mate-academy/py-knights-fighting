from typing import Callable, List

from app.models.tool_model import Armour, Potion, Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def preparation(self) -> None:
        if self.armour:
            for arm in self.armour:
                self.protection += arm.protection

        if self.weapon:
            self.power += self.weapon.power

        if self.potion:
            drank = self.potion.drink()
            self.hp += drank[0]
            self.power += drank[1]
            self.protection += drank[2]

    def __isub__(self, other: Callable) -> Callable:
        """Battle between knights"""
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.hp = max(self.hp, 0)
        other.hp = max(other.hp, 0)
        return self
