from typing import Optional, List
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: List[Armour],
        weapon: Weapon,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.hp = base_hp
        self.power = base_power
        self.protection = Armour.total_protection(armour)
        self.power += weapon.power
        if potion:
            self.apply_potion(potion)

    def apply_potion(self, potion: Potion) -> None:
        self.hp += potion.effect.get("hp", 0)
        self.power += potion.effect.get("power", 0)
        self.protection += potion.effect.get("protection", 0)

    def take_damage(self, amount: int) -> None:
        self.hp -= max(0, amount)
        if self.hp < 0:
            self.hp = 0
