from __future__ import annotations

from .armour import Armour
from .potion import Potion
from .weapon import Weapon


# Class for storing and processing all knights
class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power

        self.protection = 0

        self.weapon = []
        self.armour = []
        self.potion = []

    def get_hp(self) -> int:
        return self.hp

    def set_hp(self, hp: int) -> None:
        self.hp = hp if hp > 0 else 0

    def set_weapon(self, weapon: Weapon) -> None:
        if weapon is not None:
            self.weapon.append(weapon)

    def get_weapon_list(self) -> list[Weapon]:
        return self.weapon

    def set_armour(self, armour: Armour) -> None:
        if armour is not None:
            self.armour.append(armour)

    def get_armour_list(self) -> list[Armour]:
        return self.weapon

    def set_potion(self, potion: Potion) -> None:
        if potion is not None:
            self.potion.append(potion)

    def get_potion_list(self) -> list[Potion]:
        return self.potion

    def get_current_power(self) -> int:
        power = self.power

        for weapon in self.weapon:
            power += weapon.get_power()

        for potion in self.potion:
            power += potion.get_power()

        return power

    def get_current_protection(self) -> int:
        protection = self.protection

        for armour in self.armour:
            protection += armour.get_protection()

        for potion in self.potion:
            protection += potion.get_protection()

        return protection

    def get_current_hp(self) -> int:
        hp = self.hp

        for potion in self.potion:
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
