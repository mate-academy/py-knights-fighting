from typing import List, Optional
from app.knights.models.armour import Armour
from app.knights.models.weapon import Weapon
from app.knights.models.potion import Potion


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: List[Armour],
                 weapon: Weapon,
                 potion: Optional[Potion]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()

    def calculate_protection(self) -> int:
        return sum(armour.protection for armour in self.armour)

    def apply_potion(self) -> None:
        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power
