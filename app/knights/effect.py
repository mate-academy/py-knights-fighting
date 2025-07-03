from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.knights.knight import Knight


class Effect:
    def __init__(self, power: int, hp: int, protection: int) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply_effect(self, knight: Knight) -> None:
        knight.power += self.power
        knight.hp += self.hp
        knight.protection_bonus += self.protection
