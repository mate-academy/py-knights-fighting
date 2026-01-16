from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def from_dict(cls, data: dict) -> Weapon:
        return cls(data["name"], data["power"])
