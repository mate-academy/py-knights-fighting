from __future__ import annotations

import database as db
from app.equipments.armour import Armour
from app.equipments.potion import Potion


class Knights:

    all_knights = []
    result = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon_power: int
    ) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon_power = weapon_power
        self.power += self.weapon_power
        Knights.all_knights.append(self)

    def get_protection(self) -> None:
        """
        add additional protection for instances class
        :return: None
        """
        for index, armors in enumerate(db.knights_armour):
            for armor in armors:
                if armor == self.name:
                    armour = Armour(armors[self.name])
                    self.protection = armour.get_protection_value()

    def get_potion(self) -> None:
        """
        change main properties for instances class
        :return: None
        """
        for potion in db.knights_potion:
            for key, value in potion.items():
                if key == self.name:
                    knight_potion = Potion(key, value)
                    knight_potion.__iadd__(self)

    def __sub__(self, other: Knights) -> None:
        """
        calculates remainder health points after fight
        :param other: instance class Knights
        :return:
        """
        self.hp -= other.power - self.protection
        if self.hp > 0:
            Knights.result[self.name] = self.hp
        else:
            Knights.result[self.name] = 0
