from typing import List, Optional, Dict


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: List["Armour"],
                 weapon: "Weapon", potion: Optional["Potion"]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_potion_effects(self) -> None:
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)

    def total_protection(self) -> int:
        return sum(armour.protection for armour in self.armour)


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
