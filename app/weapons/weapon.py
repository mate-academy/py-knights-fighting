from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def create_weapon(cls, weapon_config: dict) -> Weapon:
        if weapon_config:
            return cls(weapon_config["name"], weapon_config["power"])
        return None

    def __str__(self) -> str:
        return f"{self.name}(Damage: {self.power})"
