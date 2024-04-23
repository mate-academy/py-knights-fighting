from __future__ import annotations
from app.Battle_preparation.Armor import Armor
from app.Battle_preparation.Potion import Potion


class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"] + knight["weapon"]["power"]
        self.hp = knight["hp"]
        self.potion = Potion(knight["potion"]) \
            if knight["potion"] is not None else None
        self.protection = Armor(knight["armour"]).protection()

    def use_potion(self) -> None:
        if self.potion is not None:
            self.potion.potion_effect(self)

    def fight(self, other: Knight) -> None:
        self.hp = max(self.hp - (other.power - self.protection), 0)
        other.hp = max(other.hp - (self.power - other.protection), 0)
