from __future__ import annotations

from app.adapters.knight_adapter import KnightAdapter
from app.items.inventory import Inventory
from app.items.effect import Effect
from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    def __init__(self, knight_data: KnightAdapter) -> None:
        self.name = knight_data.name
        self.power = knight_data.power
        self.hp = knight_data.hp
        self.protection = knight_data.protection
        self.inventory = Inventory(knight_data.inventory_data)

        self.equiped_armour = []
        self.equiped_weapon = None

    def __str__(self) -> str:
        armour_str = "absolutely nothing"
        if self.equiped_armour:
            armour_str = ", ".join(
                str(armour_piece)
                for armour_piece in self.equiped_armour
            )

        weapon_str = "nothing"
        if self.equiped_weapon:
            weapon_str = str(self.equiped_weapon)

        return (
            f"        HEALTH\n"
            f"({self.hp_bar()})\n"
            f"Sir {self.name}\n"
            f"Armed with {weapon_str}\n"
            f"Wearing {armour_str}\n"
            f"(base protection: {self.protection})\n"
        )

    def hp_bar(self) -> str:
        return ("||" * (self.hp // 10)) + ("  " * (10 - self.hp // 10))

    def wear_armour(self) -> None:
        if self.inventory is not None:
            for item in self.inventory:
                if isinstance(item, Armour):
                    self.apply(item.effect)

    def drink_potions(self) -> None:
        if self.inventory is not None:
            for item in self.inventory:
                if isinstance(item, Potion):
                    self.apply(item.effect)

    def ready_weapon(self) -> None:
        if self.inventory is not None:
            for item in self.inventory:
                if isinstance(item, Weapon):
                    self.apply(item.effect)

    def apply(self, effect: Effect):
        ...

    def get_hit(self, power: int) -> None:
        ...

    def attack(self, other: Knight) -> None:
        ...

    def is_alive(self) -> bool:
        if self.hp <= 0:
            return False
        return True
