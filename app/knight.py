from typing import List, Dict


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
    def __init__(self, name: str, power: int, hp: int, armour: List[Armour],
                 weapon: Weapon, potion: Potion) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.apply_equipment()
        self.power = None
        self.protection = None

    def apply_equipment(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power = self.base_power + self.weapon.power

        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(damage - self.protection, 0)
        if self.hp < 0:
            self.hp = 0
