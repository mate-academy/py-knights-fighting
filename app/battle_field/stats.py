from typing import Union


class Stats:
    def __init__(self, hp: int, power: int, protection: int) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    def __add__(self, other: "Stats") -> "Stats":
        return Stats(self.hp + other.hp, self.power + other.power, self.protection + other.protection)

    def __str__(self) -> str:
        return f"hp: {self.hp}, power: {self.power}, protection: {self.protection}"

    def add_hp(self, hp: int) -> None:
        self.hp += hp

    def add_power(self, power: int) -> None:
        self.power += power

    def add_protection(self, protection: int) -> None:
        self.protection += protection
