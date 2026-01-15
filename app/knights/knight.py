from __future__ import annotations
from typing import List, Dict

from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Dict[str, str | int]],
            weapon: Dict[str, str | int],
            potion: Dict[str, str | Dict[str, int]]

    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Armour.from_list(armour)
        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None
        self.protection = 0
        self.__dress_armor()
        self.__wield_weapon()
        self.__drink_potion()

    def __dress_armor(self) -> None:
        if self.armour:
            self.protection += sum(arm.protection for arm in self.armour)

    def __wield_weapon(self) -> None:
        self.power += self.weapon.power

    def __drink_potion(self) -> None:
        if self.potion:
            for effect, activity in self.potion.effect.items():
                self.__dict__[effect] += activity
