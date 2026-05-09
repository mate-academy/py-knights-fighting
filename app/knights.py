from __future__ import annotations
from app.ammo.weapon import Weapon
from app.ammo.potion import Potion
from app.ammo.armour import Armour


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Armour,
        weapon: Weapon,
        potion: Potion | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.potion.use_potion(self)
            self.potion = None

    def damage(self) -> int:
        return self.power + self.weapon.power
