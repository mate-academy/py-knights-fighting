from typing import List, Optional, Dict


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: Dict[str, int]) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        base_power: int,
        base_hp: int,
        armour: Optional[List[Armour]],
        weapon: Weapon,
        potion: Optional[Potion],
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        # Derived stats after applying equipment and potion
        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0

    def apply_equipment_and_potion(self) -> None:
        # Apply armour protection
        self.protection = sum(a.protection for a in self.armour)

        # Apply weapon power
        self.power += self.weapon.power

        # Apply potion effects if any
        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)
