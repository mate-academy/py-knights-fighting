from __future__ import annotations
from typing import Union


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: Union[None, dict]) -> None:
        self.protection = None
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def create_instance_from_dict(knight: dict) -> Knight:
        knight_instance = Knight(name=knight["name"],
                                 power=knight["power"],
                                 hp=knight["hp"],
                                 armour=knight["armour"],
                                 weapon=knight["weapon"],
                                 potion=knight["potion"])
        return knight_instance

    def apply_features(self) -> Knight:
        # apply armour
        self.protection = 0
        for armour in self.armour:
            self.protection += armour["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
        return self

    def battle(self, opponent: Knight) -> Knight:
        self.hp -= opponent.power - self.protection
        self.hp = 0 if self.hp <= 0 else self.hp
        return self

