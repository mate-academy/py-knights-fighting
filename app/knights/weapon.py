from __future__ import annotations


# Class for storing and processing all weapons
class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def change(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def get_power(self) -> int:
        return self.power

    @staticmethod
    def create_weapon(info: dict) -> Weapon:
        return Weapon(info["name"], int(info["power"]))
