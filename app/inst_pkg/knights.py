from __future__ import annotations


class Knight:

    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 protection: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def __sub__(self, other: Knight) -> Knight:
        self.hp = self.hp + self.protection - other.power
        if self.hp < 0:
            self.hp = 0
        other.hp = other.hp + other.protection - self.power
        if other.hp < 0:
            other.hp = 0
