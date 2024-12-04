from typing import List, Optional
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


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

    def apply_equipment(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(
            armour_piece.apply() for armour_piece in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon.apply()

    def apply_potion(self) -> None:
        if self.potion:
            effects = self.potion.apply()
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)

    def receive_damage(self, damage: int) -> None:
        damage_taken = max(0, damage - self.protection)
        self.hp = max(0, self.hp - damage_taken)

    def is_alive(self) -> bool:
        return self.hp > 0
