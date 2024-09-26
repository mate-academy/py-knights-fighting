from app.entities.armour import Armour
from app.entities.weapon import Weapon
from app.entities.potion import Potion
from typing import List, Optional


class Knight:
    def __init__(self, name: str, base_power: int, base_hp: int,
                 armour: List[Armour], weapon: Weapon,
                 potion: Optional[Potion] = None) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        # Calculate initial values
        self.update_attributes()

    def update_attributes(self) -> None:
        self.protection = self.calculate_protection()
        self.power = self.calculate_power()
        self.hp = self.calculate_hp()

    def calculate_protection(self) -> int:
        protection = sum(a.protection for a in self.armour)
        if self.potion:
            protection += self.potion.effect.get("protection", 0)
        return protection

    def calculate_power(self) -> int:
        power = self.base_power + self.weapon.power
        if self.potion:
            power += self.potion.effect.get("power", 0)
        return power

    def calculate_hp(self) -> int:
        hp = self.base_hp
        if self.potion:
            hp += self.potion.effect.get("hp", 0)
        return hp

    def __repr__(self) -> str:
        return (f"Knight(name={self.name}, power={self.power}, hp={self.hp}, "
                f"protection={self.protection})")
