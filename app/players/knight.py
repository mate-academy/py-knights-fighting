from __future__ import annotations
from typing import List, Union

from app.items.armour import Armour
from app.items.potions import Potion
from app.items.weapons import Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour],
            weapon: Weapon,
            potion: Union[Potion, None],
            protection: int = 0,

    ) -> None:
        self.power = power
        self.name = name
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection
        self.potion_buff_hp = 0
        self.potion_buff_protection = 0
        self.potion_buff_power = 0

        self._base_power = power
        self._base_hp = hp,

    def apply_potion(self) -> None:
        if self.potion:
            # print("POTION HP",self.potion.effect.hp)
            # print(f"Potion of: {self.name}")
            # print(f"======================")
            self.potion_buff_hp = self.potion.effect.hp
            self.potion_buff_protection = self.potion.effect.protection
            self.potion_buff_power = self.potion.effect.power
            self.hp += self.potion_buff_hp
            self.power += self.potion_buff_power
            self.protection += self.potion_buff_protection

    def exclude_potion_effect(self) -> None:
        self.hp -= self.potion_buff_hp
        self.power -= self.potion_buff_power
        self.protection -= self.potion_buff_protection

    def apply_weapon_power(self) -> None:
        self.power += self.weapon.power

    def exclude_weapon_power(self) -> None:
        self.power -= self.weapon.power

    def apply_protection(self) -> None:
        for arm in self.armour:
            self.protection += arm.protection
        if len(self.armour) == 0:
            self.protection = 0

    def exclude_protection(self) -> None:
        self.protection = 0

    def reset_knight_state(self) -> None:
        self.hp = self._base_hp
        self.power = self._base_power

    def fight_knight(self, other: Knight) -> None:
        self.hp -= (other.power - self.protection)
        self.hp = 0 if self.hp < 0 else self.hp

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Knight: {self.name}"
