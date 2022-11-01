from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @staticmethod
    def create_weapon(weapon: dict) -> Weapon:
        return Weapon(weapon["name"], weapon["power"])
