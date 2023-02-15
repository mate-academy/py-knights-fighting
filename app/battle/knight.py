from __future__ import annotations

from app.items.armour import Armour
from app.items.potion import Potion
from app.items.weapon import Weapon


class Knight:
    knight_dict = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
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
        Knight.knight_dict[name] = self

    def drink_potion(self, potion: Potion) -> None:
        """Apply potion effects"""
        positive_potion_effect = True

        for attribute, effect in potion.effect.items():
            if effect < 0:
                positive_potion_effect = False
            knight_stat = getattr(self, attribute)
            if knight_stat + effect < 0:
                knight_stat = 0
            else:
                knight_stat += effect
            setattr(self, attribute, knight_stat)

        message = f"{self.name} drinks a {potion.name} potion."
        if positive_potion_effect:
            message += " Their attributes are fortified!"
        print(message)

    def attack(self, other: Knight) -> None:
        """Attack the other knight"""
        damage = self.power - other.protection
        other.hp -= damage
        print(f"{self.name} delivers a blow! {other.name} loses {damage} HP.")

    def has_fallen(self) -> bool:
        """Check if the knight has fallen"""
        if self.hp > 0:
            return False
        return True
