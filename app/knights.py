from __future__ import annotations


class Knights:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def get_protection(self, value: list) -> None:
        if isinstance(value, int):
            value = [value]
        self.protection += sum(value)

    def get_power(self, power: int) -> None:
        self.power += power

    def get_hp(self, hp: int) -> None:
        self.hp += hp

    def __sub__(self, other: Knights) -> int:
        self.hp = self.hp - (other.power - self.protection)
        return max(self.hp, 0)
