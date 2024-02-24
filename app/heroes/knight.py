from __future__ import annotations
from typing import List

from app.equipment.armour_component import ArmourComponent
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armour: List[ArmourComponent] = None,
        potion: Potion = None
    ) -> None:
        if armour is None:
            armour = []
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = 0

    def battle_preparations(self) -> Knight:
        for armour_component in self.armour:
            self.protection += armour_component.protection
        self.power += self.weapon.power
        # apply potion if exist
        if self.potion:
            for effect, value in self.potion.effect.items():
                if hasattr(self, effect):
                    setattr(self, effect, getattr(self, effect) + value)
        return self
