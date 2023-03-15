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

    def apply_armour(self) -> int:
        protection = sum(i.protection for i in self.armour)
        self.protection = protection

    def apply_weapon(self) -> int:
        power = self.power + self.weapon.power
        self.power = power

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion.effect.items():
                if stat == "hp":
                    self.hp += value
                if stat == "power":
                    self.power += value
                if stat == "protection":
                    self.protection += value
