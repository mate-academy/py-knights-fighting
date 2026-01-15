from typing import List, Optional
from .armour import Armour
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: Optional[List[Armour]] = None,
                 weapon: Optional[Weapon] = None,
                 potion: Optional[Potion] = None
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armour else []
        self.weapon = weapon
        self.potion = potion
        self.apply_effects()

    def apply_effects(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(armour.protection for armour in self.armour)

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)

    def total_power(self) -> int:
        return self.power

    def total_protection(self) -> int:
        total_armour_protection = sum(
            armour.protection for armour in self.armour
        )
        potion_protection_boost = self.potion.effect.get(
            "protection", 0) if self.potion else 0
        return total_armour_protection + potion_protection_boost
