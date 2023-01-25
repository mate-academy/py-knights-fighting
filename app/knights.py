from __future__ import annotations
from typing import Optional


class Knights:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def use_potion(self, potions: Optional[dict] = None) -> None:
        if potions is not None:
            if "hp" in potions["effect"]:
                self.hp += potions["effect"]["hp"]
            if "power" in potions["effect"]:
                self.power += potions["effect"]["power"]
            if "protection" in potions["effect"]:
                self.protection += potions["effect"]["protection"]

    def use_armour(self, armours: Optional[dict] = None) -> None:
        if armours is not None:
            for armor in armours:
                self.protection += armor["protection"]

    def use_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def correct_hp(self) -> None:
        if self.hp < 0:
            self.hp = 0

    def fight(self, other: Knights) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.correct_hp()
        other.correct_hp()
