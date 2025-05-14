from __future__ import annotations
from typing import Dict, Any


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        if isinstance(self.armour, list):
            for arm in self.armour:
                self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()


def prepare_knight(knights_dict: Dict[str, Any]) -> Knight:
    knight = Knight(
        name=knights_dict["name"],
        power=knights_dict["power"],
        hp=knights_dict["hp"],
        armour=knights_dict["armour"],
        weapon=knights_dict["weapon"],
        potion=knights_dict["potion"]
    )
    knight.prepare_for_battle()
    return knight
