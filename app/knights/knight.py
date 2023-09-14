from __future__ import annotations

from typing import Optional
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Optional[Potion] = None
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(a.part, a.protection) for a in armour]
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power += self.weapon.power

        if self.potion:
            self.apply_potion()

    def apply_potion(self) -> None:
        if self.potion.effect.power:
            self.power += self.potion.effect.power

        if self.potion.effect.protection:
            self.protection += self.potion.effect.protection

        if self.potion.effect.hp:
            self.hp += self.potion.effect.hp

    def battle(self, opponent: Knight) -> None:
        self.hp -= max(0, opponent.power - self.protection)
        if self.hp < 0:
            self.hp = 0
