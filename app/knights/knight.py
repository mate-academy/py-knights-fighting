from __future__ import annotations

from .armour import Armour
from .potion import Potion
from .weapon import Weapon


# Class for storing and processing all knights
class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.__hp = hp
        self.__power = power

        self.__protection = 0

        self.__weapon = []
        self.__armour = []
        self.__potion = []

    def get_hp(self) -> int:
        return self.__hp

    def set_hp(self, hp: int) -> None:
        self.__hp = hp if hp > 0 else 0

    def set_weapon(self, weapon: Weapon) -> None:
        if weapon is not None:
            self.__weapon.append(weapon)

    def get_weapon_list(self) -> list[Weapon]:
        return self.__weapon

    def set_armour(self, armour: Armour) -> None:
        if armour is not None:
            self.__armour.append(armour)

    def get_armour_list(self) -> list[Armour]:
        return self.__weapon

    def set_potion(self, potion: Potion) -> None:
        if potion is not None:
            self.__potion.append(potion)

    def get_potion_list(self) -> list[Potion]:
        return self.__potion

    def get_current_power(self) -> int:
        power = self.__power

        for weapon in self.__weapon:
            power += weapon.get_power()

        for potion in self.__potion:
            power += potion.get_power()

        return power

    def get_current_protection(self) -> int:
        protection = self.__protection

        for armour in self.__armour:
            protection += armour.get_protection()

        for potion in self.__potion:
            protection += potion.get_protection()

        return protection

    def get_current_hp(self) -> int:
        hp = self.__hp

        for potion in self.__potion:
            hp += potion.get_hp()

        return hp

    def fights(self, other: Knight) -> None:
        self.set_hp(
            self.get_current_hp() + self.get_current_protection()
            - other.get_current_power()
        )
        other.set_hp(
            other.get_current_hp() + other.get_current_protection()
            - self.get_current_power()
        )
