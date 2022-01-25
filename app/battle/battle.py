"""
This module contains class Battle, which used by main.py module
to create "battles" between two knights. Class doesn`t have instance
methods, only one staticmethod which takes two instances of knights
and returns result of battle - final "hp" of each knight to compare.
"""


class Battle:
    @staticmethod
    def get_result(knight_1, knight_2):
        first_knight_hp = knight_1.get_hp()
        second_knight_hp = knight_2.get_hp()
        first_knight_hp -= knight_2.get_power() - knight_1.get_protection()
        second_knight_hp -= knight_1.get_power() - knight_2.get_protection()

        if first_knight_hp <= 0:
            first_knight_hp = 0

        if second_knight_hp <= 0:
            second_knight_hp = 0

        return {
            knight_1.knight["name"]: first_knight_hp,
            knight_2.knight["name"]: second_knight_hp
        }
