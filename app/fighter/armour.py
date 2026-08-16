from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from knight import Knight


class Armour:
    def __init__(
            self,
            name: str = "",
            protection: int = 0
    ) -> None:
        self.name = name
        self.protection = protection

    def equip_armour_to_knight(self, unit: Knight) -> None:
        unit.protection += self.protection
