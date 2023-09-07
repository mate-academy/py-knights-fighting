from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_attributes(
            self, armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        for unit in armour:
            self.protection += unit["protection"]
        self.power += weapon["power"]
        if potion:
            for attribute, value in potion["effect"].items():
                self.__dict__[attribute] += value

    def perform_battle(self, opponent: Knight) -> None:
        opponent.hp -= self.power - opponent.protection
        self.hp -= opponent.power - self.protection

        if opponent.hp <= 0:
            opponent.hp = 0
        if self.hp <= 0:
            self.hp = 0
