from __future__ import annotations
from typing import Union

class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: Union[dict, None]
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        for piece in armour:
            self.protection += piece["protection"]

        self.power += weapon["power"]

        if potion:
            effects = potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)

    def attack(self, opponent: Knight) -> None:
        damage = max(0, self.power - opponent.protection)
        opponent.hp -= damage
        if opponent.hp <= 0:
            opponent.hp = 0