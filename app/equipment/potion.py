from __future__ import annotations

from app.equipment.equipment import Equipment
from app.human.knight import Knight


class Potion(Equipment):
    def __init__(self, name: str, effects: dict[str: int]) -> None:
        super().__init__(name)
        self.effects = effects

    def apply(self, knight: Knight):
        pass
