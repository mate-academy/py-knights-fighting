from app.Knight.potion import Potion
from app.Knight.weapon import Weapon
from app.Knight.armour import ArmourPart
from typing import Optional


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[ArmourPart],
            weapon: Weapon,
            potion: Optional[Potion]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def calculate_stats(self) -> None:
        self.power += self.weapon.power
        for shield in self.armour:
            self.protection += shield.protection
        if self.potion is not None:
            self.hp += self.potion.effect.get("hp", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.power += self.potion.effect.get("power", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(damage - self.protection, 0)
        if self.hp <= 0:
            self.hp = 0
