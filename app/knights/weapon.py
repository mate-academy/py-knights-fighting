from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.knights.knight import Knight


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def total_damage(self, knight: Knight) -> int:
        return self.power + knight.power
