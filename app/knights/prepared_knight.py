from __future__ import annotations


class PreparedKnight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def duel(self, other: PreparedKnight) -> int:
        self.hp -= (other.power - self.protection)

        if self.hp < 0:
            self.hp = 0

        return self.hp
