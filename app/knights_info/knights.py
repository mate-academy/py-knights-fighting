from __future__ import annotations

from app.knights_info.armor import Armour
from app.knights_info.weapon import Weapon
from app.knights_info.potion import Potion


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = [Armour(armour_info["part"],
                              armour_info["protection"])
                       for armour_info in armour]
        self.weapon = Weapon(**weapon)
        if potion is not None:
            self.potion = Potion(**potion)
        else:
            self.potion = potion

    def apply_armour(self) -> None:
        protection = 0
        if self.armour:
            protection = sum(part.protection for part in self.armour)
        self.protection += protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            potion_effect = self.potion.effect
            self.power += potion_effect.get("power", 0)
            self.hp += potion_effect.get("hp", 0)
            self.protection += potion_effect.get("protection", 0)

    def battle(self, opponent: Knight) -> None:
        # first knight battle preparation
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

        # second knight battle preparation
        opponent.apply_armour()
        opponent.apply_weapon()
        opponent.apply_potion()

        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        self.hp = max(self.hp, 0)
        opponent.hp = max(opponent.hp, 0)
