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

    def get_battle(self, other: Knight) -> str:
        self.hp = self.hp - other.power + self.protection
        other.hp = other.hp - self.power + other.protection

        if self.hp < 0:
            self.hp = 0

        if other.hp < 0:
            other.hp = 0

        result_of_battle = f"Result of battle {self.name} vs {other.name}:\n" \
                           f"{self.name} has {self.hp} hp\n" \
                           f"{other.name} has {other.hp} hp\n"
        return result_of_battle
