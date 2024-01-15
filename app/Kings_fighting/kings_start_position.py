from __future__ import annotations
from typing import Any


class King:
    # It can be useful to check correct start parameters
    start_position = {}

    @staticmethod
    def magic_upgrades(__init__: Any) -> Any:
        def wrapper(self: King, input_dict: dict) -> Any:
            input_dict["protection"] = sum(part["protection"]
                                           for part in input_dict["armour"])
            input_dict["power"] += input_dict["weapon"]["power"]

            if input_dict["potion"]:
                potion = input_dict["potion"]["effect"]

                for name in potion.keys():
                    input_dict[name] += potion[name]

            __init__(self, input_dict)
        return wrapper

    @magic_upgrades
    def __init__(self, input_dict: dict) -> None:
        self.name = input_dict["name"]
        self.hp = input_dict["hp"]
        self.power = input_dict["power"]
        self.protection = input_dict["protection"]
        King.start_position[self.name] = self.protection

    def __sub__(self, other: King) -> King:
        self.hp -= other.power - self.protection
        return self
