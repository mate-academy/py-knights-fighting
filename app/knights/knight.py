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
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power += self.weapon.power

        if self.potion:
            self.apply_potion()

    def apply_potion(self) -> None:
        effect = self.potion.effect
        for stat in ["power", "protection", "hp"]:
            stat_effect = getattr(effect, stat, 0)
            if stat_effect:
                setattr(self, stat, getattr(self, stat) + stat_effect)

    def battle(self, opponent: Knight) -> None:
        self.hp -= max(0, opponent.power - self.protection)
        if self.hp < 0:
            self.hp = 0
