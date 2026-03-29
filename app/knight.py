from __future__ import annotations
from dataclasses import dataclass
from app.potion import Potion


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: dict
    weapon: dict
    potion: dict | None
    protection: int = 0

    def apply_armour(self, gear: dict) -> None:
        self.protection += gear["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: Potion) -> None:
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]
