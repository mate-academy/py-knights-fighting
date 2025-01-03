from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, protection: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def battle(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        if first_knight.hp < 0:
            first_knight.hp = 0
        if second_knight.hp < 0:
            second_knight.hp = 0
