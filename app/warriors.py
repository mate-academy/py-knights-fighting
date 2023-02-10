from __future__ import annotations
from typing import List

from app.items import Weapon, Armour, Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list,
            potion: dict,
            protection: int = 0,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.weapon = self.weapon_up(weapon)
        self.armour = self.armour_up(armour)
        self.potion = self.use_potion(potion)

    def armour_up(self, armours: list) -> List[Armour] | None:
        equip = []
        for armour in armours:
            armour = Armour(part=armour["part"],
                            protection=armour["protection"])
            equip.append(armour)
            self.protection += armour.protection
        return equip

    def weapon_up(self, weapon: dict) -> Weapon:
        weapon = Weapon(name=weapon["name"], power=weapon["power"])
        self.power += weapon.power
        return weapon

    def use_potion(self, potion: dict) -> Potion:
        if potion:
            potion = Potion(name=potion["name"], effects=potion["effect"])
            self.hp += potion.hp
            self.power += potion.power
            self.protection += potion.protection
            return potion

    def strike_enemy(self, enemy: Knight) -> None:
        enemy.hp = max(0, enemy.hp + enemy.protection - self.power)
