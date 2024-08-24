from __future__ import annotations

from typing import TYPE_CHECKING

from app.equipment.equipment import Equipment

if TYPE_CHECKING:
    from app.hero import Hero


class Potion(Equipment):
    def __init__(self, name: str, effect: dict) -> None:
        super().__init__(name)
        self.effect = effect

    def apply_effect(self, hero: Hero) -> None:
        for stat, value in self.effect.items():
            setattr(hero, stat, getattr(hero, stat) + value)
