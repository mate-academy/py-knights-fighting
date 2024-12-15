from typing import List, Dict, Optional


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
        armour: List[Armour],
        weapon: Weapon,
        potion: Optional[Potion],
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.base_hp = base_hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_total_protection(self) -> int:
        return sum(piece.protection for piece in self.armour)

    def get_total_power(self) -> int:
        total_power = self.base_power + self.weapon.power
        if self.potion:
            total_power += self.potion.effect.get("power", 0)
        return total_power

    def get_total_hp(self) -> int:
        total_hp = self.base_hp
        if self.potion:
            total_hp += self.potion.effect.get("hp", 0)
        return total_hp
