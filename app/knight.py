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

    def battle_round(self, other: Knight) -> None:
        self.hp -= (other.power - self.protection)
        if self.hp < 0:
            self.hp = 0
