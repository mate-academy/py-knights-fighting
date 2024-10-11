from typing import List
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour] | None,
            weapon: Weapon,
            potion: Potion | None,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self) -> None:
        if self.armour is not None:
            for item in self.armour:
                item.apply(self)

    def apply_weapon(self) -> None:
        self.weapon.apply(self)

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.potion.apply(self)
