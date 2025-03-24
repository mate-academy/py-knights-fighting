from __future__ import annotations
from typing import Optional

from app.Armour import Armour
from app.Potion import Potion
from app.Weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.__name: str = name

        self.__base_power: int = power
        self.__base_hp: int = hp
        self.__base_protection: int = 0

        self.__armours: list[Armour] = []
        self.__weapon: Optional[Weapon] = None
        self.__potion: Optional[Potion] = None

        self.__current_power: int = self.__base_power
        self.__current_protection: int = self.__base_protection
        self.__current_hp: int = self.__base_hp

    @property
    def name(self) -> str:
        return self.__name

    @property
    def power(self) -> int:
        return self.__current_power

    @property
    def hp(self) -> int:
        return self.__current_hp

    @hp.setter
    def hp(self, value: int) -> None:
        self.__current_hp = max(0, value)

    @property
    def protection(self) -> int:
        return self.__current_protection

    @property
    def armours(self) -> list[Armour]:
        return self.__armours

    @property
    def weapon(self) -> Weapon:
        return self.__weapon

    @property
    def potion(self) -> Potion:
        return self.__potion

    def prepare_for_fight(self) -> None:
        self.apply_weapon()
        self.apply_armours()
        self.apply_potion()

    def apply_weapon(self) -> None:
        self.__current_power = self.__base_power
        if self.weapon:
            self.__current_power += self.weapon.power

    def apply_armours(self) -> None:
        self.__current_protection = self.__base_protection
        if self.armours:
            self.__current_protection += sum(armour.protection
                                             for armour in self.armours)

    def apply_potion(self) -> None:
        self.__current_hp = self.__base_hp
        if self.potion:
            self.__current_power += self.potion.effect.power
            self.__current_hp += self.potion.effect.hp
            self.__current_protection += self.potion.effect.protection

    def add_armour(self, armour: Armour) -> None:
        self.__armours.append(armour)

    def add_armours(self, armours: list[Armour]) -> None:
        for armour in armours:
            self.add_armour(armour)

    def equip_weapon(self, weapon: Weapon) -> None:
        self.__weapon = weapon

    def equip_potion(self, potion: Potion) -> None:
        self.__potion = potion

    def fight_with(self, enemy: Knight) -> None:
        if self.__is_able_to_fight() and enemy.__is_able_to_fight():

            damage_to_self = max(0, enemy.power - self.protection)
            damage_to_enemy = max(0, self.power - enemy.protection)

            self.hp -= damage_to_self
            enemy.hp -= damage_to_enemy

    def summary(self) -> dict:
        return {self.name: self.hp}

    def __is_able_to_fight(self) -> bool:
        if self.hp <= 0:
            return False
        return True

    def __repr__(self) -> str:
        return (f"Knight(name='{self.name}', "
                f"base_hp={self.__base_hp}, "
                f"base_power={self.__base_power}, "
                f"base_protection={self.__base_protection}, "
                f"hp={self.hp}, "
                f"power={self.power}, "
                f"protection={self.protection}, "
                f"armours={self.armours}, "
                f"weapon={self.weapon}, "
                f"potion={self.potion}")
