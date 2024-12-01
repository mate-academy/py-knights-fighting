from typing import List, Optional
from .armour import Armour
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour],
            weapon: Weapon,
            potion: Optional[Potion] = None
    ) -> None:
        self.name: str = name
        self.base_power: int = power
        self.base_hp: int = hp
        self.armour: List[Armour] = armour
        self.weapon: Weapon = weapon
        self.potion: Optional[Potion] = potion
        self.protection: int = 0
        self.power: int = self.base_power
        self.hp: int = self.base_hp
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armour_piece in self.armour:
            self.protection += armour_piece.apply()

    def apply_weapon(self) -> None:
        self.power += self.weapon.apply()

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion.apply()
            if "power" in effects:
                self.power += effects["power"]
            if "protection" in effects:
                self.protection += effects["protection"]
            if "hp" in effects:
                self.hp += effects["hp"]

    def receive_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
