from __future__ import annotations

from app.entities.armour import Armour
from app.entities.weapon import Weapon
from app.core.potion import Potion


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Potion = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for armour_item in self.armour:
            if armour_item is not None:
                self.protection += armour_item.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            if self.potion.effect.power is not None:
                self.power += self.potion.effect.power
            if self.potion.effect.protection is not None:
                self.protection += self.potion.effect.protection
            if self.potion.effect.hp is not None:
                self.hp += self.potion.effect.hp

    @classmethod
    def init_from_dict(cls, knight_dict: dict) -> Knight:
        return cls(knight_dict["name"],
                   knight_dict["power"],
                   knight_dict["hp"],
                   [Armour.init_from_dict(armour)
                    for armour in knight_dict["armour"]],
                   Weapon.init_from_dict(knight_dict["weapon"]),
                   Potion.init_from_dict(knight_dict["potion"]))
