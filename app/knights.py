from __future__ import annotations
from app.equipment.consumable import Potion


class Knight:

    knights = {}

    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            defence: int
    ) -> None:

        self.name = name
        self.hp = hp
        self.power = power
        self.protection = defence
        self.knights.update({self.name: self})

    def drank_pot(self, potion: Potion) -> None:
        print(potion.name, potion.effects)
        for attribute, value in potion.effects.items():
            new_value = self.__getattribute__(attribute) + value
            self.__setattr__(attribute, new_value)
        print(f"{self.name} drank potion of {potion.name}, and now his stats"
              f" {self.hp, self.power, self.protection}")
