from __future__ import annotations
from app.knight import Knight


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name,
        self.power = power

    def apply_weapon(self, knight: Knight) -> None:
        knight.power += self.power
