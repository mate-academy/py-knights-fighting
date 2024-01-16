from __future__ import annotations
from app.Kings_fighting.addition_tools import magic_upgrades


class King:
    # It can be useful to check correct start parameters
    start_position = {}

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
