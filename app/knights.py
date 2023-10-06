from __future__ import annotations
from app.equipments.armour import Armour
from app.equipments.potion import Potion
from app.equipments.weapon import Weapon
from typing import Optional


class Knights:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armours: list[Armour],
            potion: Optional[Potion] = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours if armours else []
        self.weapon = weapon
        self.potion = potion

    def get_hp(self) -> int:
        hp_potion = 0
        if self.potion:
            hp_potion = self.potion.get_hp()
        return self.hp + hp_potion

    def get_power(self) -> int:
        power_potion = 0
        if self.potion:
            power_potion = self.potion.get_power()
        return self.power + power_potion + self.weapon.power

    def get_protection(self) -> int:
        protection_potion = 0
        armours_protection = 0

        if self.potion:
            protection_potion = self.potion.get_protection()

        for armour in self.armours:
            armours_protection += armour.protection

        return protection_potion + armours_protection

    def battle_khights(self, other: Knights) -> dict:
        hp_battre = {}
        hp_battre[self.name] = (self.get_hp() - other.get_power()
                                + self.get_protection())
        hp_battre[other.name] = (other.get_hp() - self.get_power()
                                 + other.get_protection())
        for key, hp in hp_battre.items():
            if hp < 0:
                hp_battre[key] = 0

        return hp_battre
