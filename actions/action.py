from knights.knight_preparation import Preparation
from knights.knight import Knight


class Action:

    @staticmethod
    def preparation(knight: Knight) -> None:
        Preparation.apply_armour(knight)
        Preparation.apply_weapon(knight)
        Preparation.apply_potion(knight)

    @staticmethod
    def check_hp(hp: int) -> int:
        if hp <= 0:
            hp = 0
        return hp

    @staticmethod
    def battle(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        first_knight.hp = Action.check_hp(first_knight.hp)
        second_knight.hp = Action.check_hp(second_knight.hp)
