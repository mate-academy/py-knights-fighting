from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def init_from_dict(cls, weapon_dict: dict) -> Weapon:
        return cls(weapon_dict["name"], weapon_dict["power"])
