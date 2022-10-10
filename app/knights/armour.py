from __future__ import annotations


# Class for storing and processing all armours
class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.__protection = protection

    def change(self, part: str, protection: int) -> None:
        self.part = part
        self.__protection = protection

    def get_protection(self) -> int:
        return self.__protection

    @staticmethod
    def create_armour(info: dict) -> Armour:
        return Armour(info["part"], int(info["protection"]))
