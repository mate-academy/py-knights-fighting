from knights.knight_preparation import Preparation
from knights.knight import Knight


class Action:

    @staticmethod
    def preparation(knight: Knight) -> None:
        Preparation.apply_armour(knight)
        Preparation.apply_weapon(knight)
        Preparation.apply_potion(knight)

    @staticmethod
    def battle(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        if first_knight.hp <= 0:
            first_knight.hp = 0

        if second_knight.hp <= 0:
            second_knight.hp = 0
