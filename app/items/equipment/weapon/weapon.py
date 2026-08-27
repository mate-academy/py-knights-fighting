from __future__ import annotations


class Weapon:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.power = data["power"]
