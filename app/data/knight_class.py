from __future__ import annotations
from typing import List, Dict


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def grab_weapon(self, weapon: dict) -> int:
        self.power = self.power + weapon["power"]
        return self.power

    def suit_up(self, armour: List[Dict]) -> int:
        self.protection = sum([armour["protection"] for armour in armour])
        return self.protection

    def drink_potion(self, potion: dict | None) -> None:
        if potion:
            for key, value in potion["effect"].items():
                self.__dict__[key] += value

    def duel(self, rival: Knight) -> None:
        self.hp -= rival.power - self.protection
        rival.hp -= self.power - rival.protection

        if self.hp <= 0:
            self.hp = 0
        if rival.hp <= 0:
            rival.hp = 0
