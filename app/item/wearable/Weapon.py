from __future__ import annotations

from app.item.Item import Item


class Weapon(Item):
    def __init__(self, name: str, power_bonus: int) -> None:
        super().__init__(name, 0, power_bonus, 0)
