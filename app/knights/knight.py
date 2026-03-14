from __future__ import annotations
from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = Armour.from_dict(knight["armour"])
        self.weapon = Weapon.from_dict(knight["weapon"])
        self.potion = Potion.from_dict(knight["potion"])

    def prepare_for_battle(self) -> None:
        self.protection = 0
        for armour in self.armour:
            self.protection += armour.protection

        self.power += self.weapon.power

        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        knight.hp -= self.power - knight.protection

        if self.hp <= 0:
            self.hp = 0

        if knight.hp <= 0:
            knight.hp = 0
