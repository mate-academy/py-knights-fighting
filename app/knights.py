from typing import Union
from app.items import Potion, Weapon, Armour


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Union[list[Armour], None],
            weapon: Union[list[Weapon], None],
            potion: Union[list[Potion], None],
            protection: int = 0
    ) -> None:
        self.name = name
        self.protection = protection
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_effect(self, item: Union[Weapon, Armour, Potion]) -> None:
        for stat, value in item.effect.items():
            if hasattr(self, stat):
                setattr(self, stat, getattr(self, stat) + value)
