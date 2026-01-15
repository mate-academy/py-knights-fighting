from __future__ import annotations
from app.Knights_fighting.addition_tools import magic_upgrades


class Knight:
    start_position = {}

    @magic_upgrades
    def __init__(self, input_dict: dict) -> None:
        self.name = input_dict["name"]
        self.hp = input_dict["hp"]
        self.power = input_dict["power"]
        self.protection = input_dict["protection"]
        Knight.start_position[self.name] = self.protection

    def __sub__(self, other: Knight) -> Knight:
        self.hp -= other.power - self.protection
        return self
