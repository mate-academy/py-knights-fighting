from __future__ import annotations
from typing import Generator


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0

    ) -> None:
        self.display_name = name.title().replace("_", " ")
        self.internal_name = name
        self.power = power
        self.hp = hp
        self.protection = protection


def create_participants(given_data: dict) -> Generator:
    for name, characteristic in given_data.items():
        each_power = characteristic.get("power")
        each_hp = characteristic.get("hp")
        yield Knight(name, each_power, each_hp,)
