from __future__ import annotations


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    # for making sum() for instances
    def __radd__(self, other: Armour | int) -> int:
        if isinstance(other, int):
            return self.protection + other
        return self.protection + other.protection

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "protection": self.protection
        }

    def __repr__(self) -> str:
        return str(self.__dict__())
