from __future__ import annotations
from typing import List, Optional
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Armour]
    weapon: Weapon
    potion: Optional[Potion]
    hp: int
    power: int
    protection: int

    def __init__(self, name: str, power: int, hp: int,
                 armour: List[dict], weapon: dict,
                 potion: Optional[dict] = None) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = [Armour(**a) for a in armour] if armour else []
        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None

        # ці значення виставляються при підготовці
        self.hp = hp
        self.power = power
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if not self.potion:
            return
        for stat, value in self.potion.effect.items():
            setattr(self, stat, getattr(self, stat) + value)

    def prepare_for_battle(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, damage: int) -> None:
        self.hp -= max(damage, 0)
        if self.hp <= 0:
            self.hp = 0
