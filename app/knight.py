from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.stat_calculate()

    def stat_calculate(self) -> None:
        self.armour_calculate()
        self.weapon_calculate()
        self.potion_calculate()

    def armour_calculate(self) -> None:
        for armour in self.armour:
            self.protection += armour.get("protection", 0)

    def weapon_calculate(self) -> None:
        self.power += self.weapon.get("power", 0)

    def potion_calculate(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0
        other.hp -= self.power - other.protection
        if other.hp <= 0:
            other.hp = 0
