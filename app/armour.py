from __future__ import annotations


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    def __iadd__(self, other: Armour) -> int:
        self = self.protection + other.protection
        return self
