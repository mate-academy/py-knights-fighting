from __future__ import annotations


from app.Ammunition.potions import Potion
from app.Ammunition.weapons import Weapon


class Knight:

    def __init__(
        self,
        name: str,
        power: int,
        health: int,
        weapon: Weapon,
        armour: list,
        potion: Potion | None,
        protection: int = 0
    ) -> None:
        self.name = name
        self.power = power + weapon.power
        self.health = health
        self.protection = protection
        self.weapon = weapon.name
        self.armour = []
        self.potion = potion
        for arm in armour:
            self.protection += arm.protection
            self.armour.append(arm.part)

    def potion_increasing(self) -> None:
        if self.potion:
            stats = ("power", "health", "protection")
            for stat in stats:
                setattr(
                    self,
                    stat,
                    getattr(self, stat) + getattr(self.potion, stat, 0))
        else:
            self.potion = None
