from __future__ import annotations

from app.equipment.equipment import Equipment
from app.human.knight import Knight


class Weapon(Equipment):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power

    def apply(self, knight: Knight) -> None:
        pass
