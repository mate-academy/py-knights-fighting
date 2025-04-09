from __future__ import annotations
from typing import List, Optional

from app.camelot.armour import Armour
from app.camelot.weapon import Weapon
from app.camelot.potion import Potion


class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour_pieces: List[Armour] = []
        self.weapon: Optional[Weapon] = None
        self.potion: Optional[Potion] = None

    def on_armor(self, armour: Armour) -> int:
        self.armour_pieces.append(armour)
        self.protection += armour.get_protection()
        return self.protection

    def take_weapon(self, weapon: Weapon) -> int:
        self.weapon = weapon
        self.power += weapon.get_power()
        return self.power

    def drink_potion(self, potion: Optional[Potion]) -> None:
        if potion is not None:
            self.potion = potion
            effects = potion.get_effect()

            if "hp" in effects:
                self.hp += effects["hp"]
            if "power" in effects:
                self.power += effects["power"]
            if "protection" in effects:
                self.protection += effects["protection"]

    def get_battle_stats(self) -> dict:
        return {
            "name": self.name,
            "power": self.power,
            "hp": self.hp,
            "protection": self.protection
        }

    def __str__(self) -> str:
        return f"{self.name}" \
               f"\nHP: {self.hp}" \
               f"\nPower: {self.power}" \
               f"\nProtection: {self.protection}"
