
from typing import List
from .armor import Armor
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armor],
            weapon: Weapon,
            potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> int:
        total_protection = sum([piece.protection for piece in self.armour])
        return total_protection

    def apply_weapon(self) -> int:
        return self.power + self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.get_effect()
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.armour += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]
