from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.knights import Knight


class Potion:
    def __init__(
        self,
        hp: int | None,
        power: int | None,
        protection: int | None
    ) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    def use_potion(self, knight: "Knight") -> None:
        if self.hp is not None:
            knight.hp += self.hp
        if self.power is not None:
            knight.power += self.power
        if self.protection is not None:
            knight.armour.add_protection(self.protection)
