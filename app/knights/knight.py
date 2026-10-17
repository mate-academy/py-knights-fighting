from __future__ import annotations
from copy import deepcopy


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.power = power
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.protection = sum(
            item["protection"] for item in self.armour
        )

        self.power = self.base_power + self.weapon["power"]

        if self.potion is not None:
            effects = self.potion["effect"]

            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)

    @classmethod
    def create_knight(cls, data: dict) -> Knight:
        data = deepcopy(data)

        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data["potion"],
        )
