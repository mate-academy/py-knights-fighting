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

    # Apply potion effects
    def drink_potion(self, potion: Potion) -> None:
        # Bool for message printing
        positive_potion_effect = True

        for stat, effect in potion.effect.items():
            if effect < 0:
                positive_potion_effect = False
            # Get current "stat" attribute
            knight_stat = getattr(self, stat)
            if knight_stat + effect < 0:
                knight_stat = 0
            else:
                knight_stat += effect
            # Set new "stat" attribute
            setattr(self, stat, knight_stat)

        # Print message
        msg = f"{self.name} drinks a {potion.name} potion."
        if positive_potion_effect:
            msg += " Their stats are fortified!"
        print(msg)

    # Attack other Knight
    def attack(self, other: Knight) -> None:
        dmg = self.power - other.protection
        other.hp -= dmg
        print(f"{self.name} delivers a blow! {other.name} loses {dmg} HP.")

    # Check if the knight has fallen
    def has_fallen(self) -> bool:
        if self.hp > 0:
            return False
        return True
