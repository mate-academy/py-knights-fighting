from __future__ import annotations
from typing import List

from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: List[Armour],
        weapon: Weapon,
        potion: Potion,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.prepare_knight()

    def __str__(self) -> str:
        return (
            f"Knight {self.name}: "
            f"power: {self.power}, "
            f"HP: {self.hp}"
            f"protection: {self.protection}"
        )

    def prepare_knight(self) -> None:
        self.protection += sum(armour.protection for armour in self.armour)

        self.power += self.weapon.power

        if not self.potion:
            return
        effects = ("power", "hp", "protection")
        for effect in effects:
            if effect in self.potion.effect:
                potion = getattr(self, effect)
                setattr(self, effect, potion + self.potion.effect[effect])

    @classmethod
    def create_knight(cls, knight_data: dict) -> Knight:
        armour = [
            Armour(**armour_data)
            for armour_data in knight_data.pop("armour")
        ]

        weapon = Weapon(**knight_data.pop("weapon"))

        potion_data = knight_data.pop("potion")
        potion = Potion(**potion_data) if potion_data else None

        return cls(
            **knight_data,
            armour=armour,
            weapon=weapon,
            potion=potion,
        )

    def fight(self, other: Knight) -> None:
        self.hp = max(0, self.hp - (other.power - self.protection))
        other.hp = max(0, other.hp - (self.power - other.protection))
