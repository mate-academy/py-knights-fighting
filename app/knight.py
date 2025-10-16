from typing import List, Dict, Any, Optional

from .equipment.armour import Armour
from .equipment.weapon import Weapon
from .equipment.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict[str, Any]],
        weapon: Dict[str, Any],
        potion: Optional[Dict[str, Any]],
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        if self.armour:
            for armour_data in self.armour:
                armour = Armour(armour_data["part"], armour_data["protection"])
                armour.apply(self)

    def apply_weapon(self) -> None:
        if self.weapon:
            weapon = Weapon(self.weapon["name"], self.weapon["power"])
            weapon.apply(self)

    def apply_potion(self) -> None:
        if self.potion:
            potion = Potion(self.potion["name"], self.potion["effect"])
            potion.apply(self)
