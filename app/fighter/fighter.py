from typing import Optional

from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Fighter:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Optional[Potion]) -> None:
        self.name = name
        self.power = power
        self.protection = 0
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        for armor in self.armour:
            self.protection += armor.protection

    def equip_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def drink_potion(self) -> None:
        if self.potion:
            self.hp += self.potion.effect.hp
            self.power += self.potion.effect.power
            self.protection += self.potion.effect.protection
