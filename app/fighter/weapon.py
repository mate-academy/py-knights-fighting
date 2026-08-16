from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from knight import Knight


class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon.get("name")
        self.power = weapon.get("power")

    def equip_to_knight(self, unit: Knight) -> None:
        unit.power += self.power
