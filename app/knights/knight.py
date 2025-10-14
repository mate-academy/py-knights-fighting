from typing import List, Dict, Optional
from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion

class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Dict],
        weapon: Dict,
        potion: Optional[Dict],
    ) -> None:
        self.name: str = name
        self.base_power: int = int(power)
        self.base_hp: int = int(hp)
        self.armour_raw = armour or []
        self.weapon = Weapon(weapon or {})
        self.potion_raw = potion

        self.protection: int = sum(int(a.get("protection", 0)) for a in self.armour_raw)

        self.power: int = self.base_power + self.weapon.power

        self.hp: int = self.base_hp

        if self.potion_raw:
            potion_obj = Potion(self.potion_raw)
            potion_obj.apply_effect(self)

    def attack(self, enemy: "Knight") -> int:
        return self.power - enemy.protection

    def take_damage(self, damage: int) -> None:
        self.hp -= int(damage)
