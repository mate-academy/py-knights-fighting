from __future__ import annotations

from app.equipment.armour import Armour
from app.potion.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armours: list[Armour] = None, weapon: Weapon = None,
                 potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours if armours is not None else []
        self.weapon = weapon
        self.potion = potion

    def get_power(self) -> int:
        power = self.power
        if self.weapon is not None:
            power += self.weapon.get_power()
        if self.potion is not None:
            power += self.potion.get_power()
        return power

    def get_protection(self) -> int:
        protection = sum(armour.protection for armour in self.armours)
        if self.potion is not None:
            protection += self.potion.get_protection()
        return protection

    def get_hp(self) -> int:
        health = self.hp
        if self.potion is not None:
            health += self.potion.get_hp()
        return health
