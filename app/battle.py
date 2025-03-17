from __future__ import annotations


class Knight:
    knight_list = []

    def __init__(self, name: str, power: int,
                 hp: int, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def knight_battle(self: Knight, other: Knight) -> dict:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0

        return {
            self.name: self.hp,
            other.name: other.hp}
