from __future__ import annotations
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(self, knight_conf: dict) -> None:
        self.name = knight_conf["name"]
        self.power = knight_conf["power"]
        self.hp = knight_conf["hp"]
        self.protection = 0
        self.opponent = None
        self.armour = knight_conf["armour"]
        self.weapon = Weapon(knight_conf["weapon"])
        self.potion = Potion(knight_conf["potion"])

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_armour(self) -> None:
        if not self.armour == []:
            for unit in range(len(self.armour)):
                self.protection += Armour(self.armour[unit]).protection

    def apply_potion(self) -> None:
        if self.potion.effect is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def assign_opponent(self, other: Knight) -> None:
        self.opponent = other
        other.opponent = self
