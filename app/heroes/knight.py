from __future__ import annotations
from typing import List

from app.equipment.for_battle import ArmourComponent, Weapon, Potion


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

    def put_on_armour(self) -> None:
        for armour_component in self.armour:
            self.protection += armour_component.protection

    def battle_preparations(self) -> None:
        self.put_on_armour()
        self.power += self.weapon.power
        # apply potion if exist
        if self.potion:
            self.potion.improve_hero(self)

    def strike_opponent(self, other: Knight) -> None:
        self.hp -= other.power - self.protection

        if self.hp < 0:
            self.hp = 0
