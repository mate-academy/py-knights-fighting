from __future__ import annotations

from app.knights_file.potion import Potion
from app.knights_file.armour import Armour
from app.knights_file.weapon import Weapon


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
        self.protection = 0
        self.armour = []
        if armour != []:
            for arm in armour:
                self.armour.append(Armour(arm["part"], arm["protection"]))
                self.protection += arm["protection"]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.power += weapon["power"]
        if potion is not None:
            self.potion = Potion(potion["name"], potion["effect"])
            list_effect = ["power", "hp", "protection"]
            for num in range(0, len(list_effect)):
                if list_effect[num] in self.potion.effect:
                    self.list_effect[num] += (
                        self.potion.effect)[list_effect[num]]
        else:
            self.potion = potion

    def battle_vs(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp <= 0:
            self.hp = 0
