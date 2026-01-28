from __future__ import annotations

from app.item.Item import Item


class Inventory:
    def __init__(self, items: list[Item]) -> None:
        self.items = items
