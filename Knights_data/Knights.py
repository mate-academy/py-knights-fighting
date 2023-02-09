from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: dict, potions: dict) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.protection = self.wearing_armour(armour)
        self.potion = potions
        self.potions_apply()

    @staticmethod
    def wearing_armour(armours: list) -> int:
        if armours:
            return sum(armour["protection"] for armour in armours)
        return 0

    def potions_apply(self) -> None:
        if self.potion:
            if self.potion["effect"]["hp"] is not None:
                self.hp += self.potion["effect"]["hp"]
            if self.potion["effect"]["power"] is not None:
                self.power += self.potion["effect"]["power"]
            if self.potion["effect"].get("protection") is not None:
                self.protection += self.potion["effect"]["protection"]

    def __sub__(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        self.hp_check(other)

    def hp_check(self, other: Knight) -> None:
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0

    def __repr__(self):
        return f"hp: {self.hp}, power: {self.power}, protection: {self.protection}\n"
