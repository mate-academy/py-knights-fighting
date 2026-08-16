from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from knight import Knight


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def drink_potion(self, unit: Knight) -> None:
        if unit.potion:
            hp = self.effect.get("hp")
            power = self.effect.get("power")
            protection = self.effect.get("protection")

            if hp is not None:
                unit.hp += hp

            if power is not None:
                unit.power += power

            if protection is not None:
                unit.protection += protection
