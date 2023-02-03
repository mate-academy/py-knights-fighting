from __future__ import annotations

from app.battle_preparation.armour import Armour
from app.battle_preparation.potion import Potion
from app.battle_preparation.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Armour(armour)
        self.weapon = Weapon(weapon)
        self.potion = Potion(potion)
        self.protection = self.armour.protection

    @classmethod
    def dict_read(cls, dict_knights: dict) -> Knight:
        return Knight(**dict_knights)

    def apply_power(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.hp += self.potion.hp
            self.power += self.potion.power
            self.protection += self.potion.protection
