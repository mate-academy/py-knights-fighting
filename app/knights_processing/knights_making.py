from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int, hp: int,
            armour: list,
            weapon: dict,
            potion: None | dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @staticmethod
    def make_knight(knight: dict) -> Knight:
        return Knight(
            knight["name"],
            knight["power"],
            knight["hp"],
            knight["armour"],
            knight["weapon"],
            knight["potion"]
        )
