from __future__ import annotations

from typing import TYPE_CHECKING

from app.equipment.equipment import Equipment

if TYPE_CHECKING:
    from app.hero import Hero


class Weapon(Equipment):
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power

    def apply_effect(self, hero: Hero) -> None:
        hero.power += self.power
