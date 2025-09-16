from __future__ import annotations


class Fighters:
    list_fighters = []

    def __init__(self, name: str, hp: int, power: int,
                 protection: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
        Fighters.list_fighters.append(self)

    @staticmethod
    def clear_registry() -> None:
        Fighters.list_fighters.clear()

    @classmethod
    def get_by_name(cls, name: str) -> Fighters:
        for fighter in cls.list_fighters:
            if fighter.name.lower() == name.lower():
                return fighter

    def battle_vs(self, other: Fighters) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

    @staticmethod
    def check_damage() -> None:
        for element in Fighters.list_fighters:
            if element.hp <= 0:
                element.hp = 0

    @classmethod
    def print_result(cls) -> dict:
        dict_result = {}

        for fighter in Fighters.list_fighters:
            dict_result[fighter.name] = fighter.hp

        return dict_result
