from __future__ import annotations


class Knight:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
        self.hp = data["hp"]
        self.weapon = data["weapon"]
        self.armour = data["armour"]
        self.potion = data["potion"]
