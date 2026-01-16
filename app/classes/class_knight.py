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
                if arm.get("protection") is not None:
                    self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        if isinstance(self.weapon, dict):
            if isinstance(self.weapon.get("power"), (int, float)):
                self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        if isinstance(self.potion, dict):
            effect = self.potion.get("effect", {})
            if isinstance(effect, dict):
                self.power += effect.get("power", 0)
                self.protection += effect.get("protection", 0)
                self.hp += effect.get("hp", 0)

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
