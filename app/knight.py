from __future__ import annotations

from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armours: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = self.set_armours(armours)
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = self.set_potion(potion)
        self.protection = 0

    @staticmethod
    def set_armours(armours: list) -> list:
        all_armours = []

        if armours:
            for armour in armours:
                all_armours.append(
                    Armour(armour["part"], armour["protection"])
                )

        return all_armours

    @staticmethod
    def set_potion(potion: dict) -> Potion:
        if potion:
            return Potion(potion["name"], potion["effect"])
        return None

    def use_potion(self) -> None:
        if self.potion:
            for key, value in self.potion.effect.items():
                if key == "power":
                    self.power += value
                elif key == "hp":
                    self.hp += value
                elif key == "protection":
                    self.protection += value

    def __repr__(self) -> str:
        return (
            f"Knight: {self.name}; "
            f"Power: {self.power}; "
            f"HP: {self.hp}; "
            f"Armour: {self.armour}; "
            f"Weapon: {self.weapon}; "
            f"Potion: {self.potion}; "
            f"Protection: {self.protection}"
        )
