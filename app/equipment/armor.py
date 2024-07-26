from __future__ import annotations

from app.equipment.equipment import Equipment
from app.human.knight import Knight


class Armor(Equipment):
    def __init__(self, part: str, power: int) -> None:
        super().__init__(part)
        self.power = power

    def apply(self, knight: Knight) -> None:
        pass
