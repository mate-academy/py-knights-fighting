from __future__ import annotations

from app.knight_abilities.potion import Potion
from app.knight_abilities.weapon import Weapon
from app.knight_abilities.armor import Armour


class Knight:
    def __init__(self, name: str, dic_info: dict) -> None:
        self.dic_info = dic_info
        self.knight_info = self.dic_info[name]
        self.name = self.knight_info["name"]
        self.power = self.knight_info["power"]
        self.hp = self.knight_info["hp"]
        self.protection = 0

    def apply_potion(self) -> None:
        if self.knight_info["potion"]:
            potion = Potion(self.knight_info["potion"]["name"],
                            self.knight_info["potion"]["effect"])
            self.power += potion.power

            self.hp += potion.hp
            self.protection += potion.protection

    def improv_power(self) -> None:
        weapon = Weapon(self.knight_info["weapon"]["name"],
                        self.knight_info["weapon"]["power"])
        self.power += weapon.power

    def create_list_of_armour(self) -> list:
        list_of_arm = []
        for armour in self.knight_info["armour"]:
            arm = Armour(armour["part"], armour["protection"])
            list_of_arm.append(arm)
        return list_of_arm

    def improv_protect(self) -> None:
        if self.create_list_of_armour():
            for armour in self.create_list_of_armour():
                self.protection += armour.protection

    def fight(self, other_knight: Knight) -> dict:
        self.hp -= other_knight.power - self.protection
        other_knight.hp -= self.power - other_knight.protection
        return {self.name: max(self.hp, 0),
                other_knight.name: max(other_knight.hp, 0)}

    def prepare_for_tournament(self) -> None:
        self.improv_protect()
        self.improv_power()
        self.apply_potion()
