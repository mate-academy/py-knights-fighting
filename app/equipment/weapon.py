from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def create_weapon(cls, weapon: dict) -> Weapon:
        return cls(weapon["name"], weapon["power"])
