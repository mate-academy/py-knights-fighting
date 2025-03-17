from __future__ import annotations


class Knight:
    knight_list = []

    def __init__(self, name: str, power: int,
                 hp: int, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
