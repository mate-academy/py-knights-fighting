from __future__ import annotations
from typing import Literal, Optional


class Item:
    def __init__(
            self,
            name: str,
            item_class: Literal["weapon", "armour", "potion"],
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.item_class = item_class
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def create_from_dict(
            cls,
            item_class: Literal["weapon", "armour", "potion"],
            item: Optional[dict]
    ) -> Optional[Item]:
        if not item:
            return None
        name = item.get("name") or item.get("part")
        if item_class == "potion":
            item = item["effect"]
        power = item.get("power", 0)
        hp = item.get("hp", 0)
        protection = item.get("protection", 0)

        return cls(
            name,
            item_class,
            power,
            hp,
            protection
        )
