from typing import List
from app.stats.armour import Armour
from app.stats.weapon import Weapon
from app.stats.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Armour],
        weapon: Weapon,
        potion: Potion,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        for _ in self.armour:
            self.protection += self.protection
        self.power += self.weapon.power
        if self.potion:
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
