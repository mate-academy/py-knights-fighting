from __future__ import annotations

from app.knight_info.armour import KnightArmour
from app.knight_info.potion import KnightPotion
from app.knight_info.weapon import KnightWeapon


class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def total_strength(
            self,
            armours: list,
            weapon: dict,
            potion: dict
    ) -> Knight:
        if potion is not None:
            knight_potion = KnightPotion(potion["name"], potion["effect"])
            self.hp += knight_potion.get_hp()
            self.power += knight_potion.get_power()
            self.protection += knight_potion.get_protection()

        knight_weapon = KnightWeapon(weapon["name"], weapon["power"])
        knight_armour = KnightArmour()

        self.power += knight_weapon.power
        self.protection += knight_armour.total_armour(armours)

        return self

    def knight_info(self) -> None:
        print(self.name, self.hp, self.power, self.protection)


def get_knight(knights_config: dict) -> list:
    knights = []

    for knight_key, knight_value in knights_config.items():
        current_knight = Knight(
            knight_value["name"],
            knight_value["hp"],
            knight_value["power"]
        )

        current_knight.total_strength(
            knight_value["armour"],
            knight_value["weapon"],
            knight_value["potion"]
        )
        current_knight.knight_info()

        knights.append(current_knight)

    return knights
