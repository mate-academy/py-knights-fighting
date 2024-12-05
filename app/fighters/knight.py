from __future__ import annotations

from app.data.knight_data import KnightData
from app.items.armour import Armour
from app.items.item import Item
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(self, knight_data: KnightData) -> None:
        self.name = knight_data.name
        self.hp = knight_data.hp
        self.protection = knight_data.protection
        self.armour = knight_data.armour
        self.weapon = knight_data.weapon
        self.potion = knight_data.potion

    def __str__(self):
        armour_str = "absolutely nothing"
        if self.armour:
            armour_str = ", ".join(
                str(armour_piece)
                for armour_piece in self.armour
            )

        potion_str = "no"
        if self.potion:
            potion_str = str(self.potion)

        weapon_str = "nothing"
        if self.weapon:
            weapon_str = str(self.weapon)

        return (
            f"        HEALTH\n"
            f"({self.hp_bar()})\n"
            f"Sir {self.name}\n"
            f"Armed with {weapon_str}\n"
            f"Has {potion_str} potion\n"
            f"Wearing {armour_str}\n"
            f"(base protection: {self.protection})\n"
        )

    def hp_bar(self) -> str:
        return ("||" * (self.hp // 10)) + ("  " * (10 - self.hp // 10))

    def apply(self, item: Item):
        if isinstance(item, Potion):
            ...
        elif isinstance(item, Armour):
            ...
        elif isinstance(item, Weapon):
            ...

    def attack(self, other: Knight):
        ...

