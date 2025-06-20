from typing import List, Optional
from app.equipment import ArmourPart, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: Optional[List[ArmourPart]] = None,
        weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        self.power = self.calculate_power()
        self.hp = self.calculate_hp()
        self.protection = self.calculate_protection()

    def calculate_protection(self) -> int:
        base_protection = sum(part.protection for part in self.armour)
        potion_protection = self.potion.effect.get("protection", 0)\
            if self.potion else 0
        return base_protection + potion_protection

    def calculate_power(self) -> int:
        base = self.base_power + (self.weapon.power if self.weapon else 0)
        potion_power = self.potion.effect.get("power", 0) if self.potion else 0
        return base + potion_power

    def calculate_hp(self) -> int:
        potion_hp = self.potion.effect.get("hp", 0) if self.potion else 0
        return self.base_hp + potion_hp
