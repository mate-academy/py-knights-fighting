from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, protection: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
