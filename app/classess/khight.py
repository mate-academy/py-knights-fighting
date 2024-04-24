from __future__ import annotations


class Knight:
    knights = []

    def __init__(self, name: str, power: int, protection: int,
                 hp: int) -> None:
        self.name = name
        self. power = power
        self.hp = hp
        self.protection = protection
        Knight.knights.append(self)

    def battle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0

    @classmethod
    def reset(cls) -> None:
        if len(cls.knights) == 4:
            cls.knights = []
