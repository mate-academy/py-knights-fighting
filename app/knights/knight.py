from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def get_battle(self, other: Knight) -> None:
        self.hp = self.hp - other.power + self.protection
        other.hp = other.hp - self.power + other.protection

        if self.hp < 0:
            self.hp = 0

        if other.hp < 0:
            other.hp = 0
