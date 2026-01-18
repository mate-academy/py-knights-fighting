from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.entities.knight import Knight


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply(self, knight: Knight) -> None:
        for key, value in self.effect.items():
            if key == "hp":
                knight.hp += value
            elif key == "power":
                knight.power += value
            elif key == "protection":
                knight.protection += value
