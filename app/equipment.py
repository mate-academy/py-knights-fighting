from __future__ import annotations


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, parts: list) -> None:
        self.protection = self._total_protection(parts)

    @staticmethod
    def _total_protection(armour_parts: list) -> int:
        protection = 0
        for part in armour_parts:
            protection += part["protection"]
        return protection


class Potion:
    def __init__(self, potion: dict) -> None:
        self.name = potion["name"]
        self.effect = potion["effect"]
