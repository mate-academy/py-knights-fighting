from __future__ import annotations

from app.item.Item import Item


class Armour(Item):
    def __init__(self, name: str, protection_bonus: int) -> None:
        super().__init__(name, 0, 0, protection_bonus)
