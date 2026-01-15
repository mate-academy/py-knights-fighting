from __future__ import annotations
from app.potion.potion import Potion
from app.armour.armour_part import ArmourPart
from app.weapon.weapon import Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[ArmourPart],
            weapon: Weapon,
            potion: Potion | None = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour.copy()
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            if hasattr(self.potion.effect, "power"):
                self.power += self.potion.effect.power

            if hasattr(self.potion.effect, "protection"):
                self.protection += self.potion.effect.protection

            if hasattr(self.potion.effect, "hp"):
                self.hp += self.potion.effect.hp

    def attack(self, other_knight: Knight) -> None:
        other_knight.hp -= (self.power - other_knight.protection)

        if other_knight.hp <= 0:
            other_knight.hp = 0
