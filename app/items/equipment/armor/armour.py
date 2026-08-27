from __future__ import annotations


class Armour:
    def __init__(self, data: dict) -> None:
        self.armour_part_name = data["part"]
        self.protection = data["protection"]
