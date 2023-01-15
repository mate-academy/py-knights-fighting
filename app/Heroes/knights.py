from __future__ import annotations


from app.Ammunition.potions import Potion
from app.Ammunition.weapons import Weapon


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 health: int,
                 weapon: Weapon,
                 armour: list,
                 potion: Potion | None,
                 protection: int = 0
                 ) -> None:
        self.name = name
        self.power = power + weapon.power + \
            (potion.power if potion is not None else 0)
        self.health = health + \
            (potion.health if potion is not None else 0)
        self.protection = protection + \
            (potion.protection if potion is not None else 0)
        self.weapon = weapon.name
        self.armour = []
        if potion is None:
            self.potion = None
        else:
            self.potion = potion.name
        if len(armour) != 0:
            for arm in armour:
                self.protection += arm.protection
                self.armour.append(arm.part)
