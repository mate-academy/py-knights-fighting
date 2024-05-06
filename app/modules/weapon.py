from __future__ import annotations


class Weapon:
    def __init__(self, weapon_item: dict) -> None:
        self.name = weapon_item["name"]
        self.damage_power = weapon_item["power"]

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "power": self.damage_power
        }

    def __repr__(self) -> str:
        return str(self.__dict__())
