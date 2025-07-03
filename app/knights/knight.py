from __future__ import annotations

from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection_bonus = 0

        self.power = power + weapon.power

        if self.potion:
            self.potion.effect.apply_effect(self)

    def power(self) -> int:
        return self.power + self.weapon.power

    def get_total_protection(self) -> int:
        return Armour.total_armour(self.armour) + self.protection_bonus
