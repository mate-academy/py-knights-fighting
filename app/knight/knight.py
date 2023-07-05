from __future__ import annotations
from typing import List
from app.knight.potion import Potion
from app.knight.weapon import Weapon
from app.knight.armour import Armour


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            potion: Potion = None,
            armour: List[Armour] = []
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def battle_preparation(self) -> None:
        # apply armour
        for arm in self.armour:
            self.protection += arm.protection
        # apply weapon
        self.power += self.weapon.power
        # apply potion if exist
        if self.potion is not None:
            effect = self.potion.effect
            if effect.power is not None:
                self.power += effect.power
            if effect.protection is not None:
                self.protection += effect.protection
            if effect.hp is not None:
                self.hp += effect.hp
