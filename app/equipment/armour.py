from __future__ import annotations


class Armour:
    armours: [Armour] = []

    def __init__(self, part: str, protection: int = 0) -> None:
        self.part = part
        self.protection = protection
        Armour.armours.append(self)
