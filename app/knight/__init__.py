from __future__ import annotations
from typing import Callable, Tuple


def each_other(func: Callable) -> Callable:
    def inner(self: Knight, other: Knight) -> Tuple[Callable, Callable]:
        return func(self, other), func(other, self)

    return inner


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = (
            knight["hp"]
            + self.potion_exchange(knight["potion"], "hp")
        )
        self.power = (
            knight["power"]
            + self.potion_exchange(knight["potion"], "power")
            + knight["weapon"]["power"]
        )
        self.protection = (
            sum(part["protection"] for part in knight["armour"])
            + self.potion_exchange(knight["potion"], "protection")
        )

    @staticmethod
    def potion_exchange(potion: dict | None, key: str) -> int:
        if potion:
            return potion["effect"].get(key, 0)
        return 0

    @each_other
    def fight(self, other: Knight) -> None:
        attack = (other.power - self.protection)
        self.hp -= attack
        if self.hp <= 0:
            self.hp = 0
