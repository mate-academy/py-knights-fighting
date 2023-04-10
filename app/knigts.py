from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: list[dict]) -> None:
        if armour:
            for part in armour:
                self.protection += part.get("protection", 0)

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power", 0)

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            effect = potion.get("effect")
            for key, value in effect.items():
                setattr(self, key, getattr(self, key) + value)

    @classmethod
    def battle(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0
