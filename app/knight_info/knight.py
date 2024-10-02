from __future__ import annotations

from app.knight_info.armour import Armour, total_armour
from app.knight_info.potion import Potion
from app.knight_info.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            weapon: dict,
            armour: list,
            potion: dict
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.weapon = Weapon(**weapon)
        self.armour = [Armour(**part_armour) for part_armour in armour]

        if potion is not None:
            self.potion = Potion(**potion)
            self.hp += self.potion.get_hp()
            self.power += self.potion.get_power()
            self.protection += self.potion.get_protection()

        self.power += self.weapon.power
        self.protection += total_armour(self.armour)

    def knight_info(self) -> None:
        print(self.name, self.hp, self.power, self.protection)


def get_knight(knights_config: dict) -> list:
    knights = []

    for knight_key, knight_value in knights_config.items():
        current_knight = Knight(**knight_value)

        current_knight.knight_info()
        knights.append(current_knight)

    return knights
