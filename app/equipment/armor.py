from __future__ import annotations

from typing import TYPE_CHECKING

from app.equipment.equipment import Equipment

if TYPE_CHECKING:
    from app.hero import Hero


class Armor(Equipment):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name)
        self.protection = protection

    def apply_effect(self, hero: Hero) -> None:
        hero.protection += self.protection
