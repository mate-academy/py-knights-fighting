from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def calculate_stats(self) -> Knight:
        self.protection = sum(value["protection"] for value in self.armour)
        self.power += self.weapon["power"]
        if self.potion:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)
        return self

    def take_damage(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0
