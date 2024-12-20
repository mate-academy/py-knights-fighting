from typing import List, Optional


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[List[Armour]] = None,
        weapon: Optional[Weapon] = None,
        potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        self.calculate_stats()

    def calculate_stats(self) -> None:
        self.protection = sum(a.protection for a in self.armour)
        self.power = self.base_power + (self.weapon.power
                                        if self.weapon else 0)
        self.hp = self.base_hp

        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


class Battle:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> dict:
        knight1_damage = max(0, knight2.power - knight1.protection)
        knight2_damage = max(0, knight1.power - knight2.protection)

        knight1.take_damage(knight1_damage)
        knight2.take_damage(knight2_damage)

        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp
        }
