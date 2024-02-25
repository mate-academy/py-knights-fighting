from __future__ import annotations
from typing import List

from app.equipment.knight import ArmourComponent, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armour: List[ArmourComponent] = None,
        potion: Potion | None = None
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

    def battle_preparations(self) -> None:
        for armour_component in self.armour:
            self.protection += armour_component.protection
        self.power += self.weapon.power
        # apply potion if exist
        if self.potion:
            for effect, value in self.potion.effect.items():
                if hasattr(self, effect):
                    # set new value if self have effect instance
                    setattr(self, effect, getattr(self, effect) + value)

    def strike_opponent(self, other: Knight) -> None:
        self.hp -= other.power - self.protection

        if self.hp < 0:
            self.hp = 0
