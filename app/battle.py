from typing import List

from app.knight import Knight


class Battle:
    battle_info = {}

    @staticmethod
    def battle_preparation(knight_config: dict) -> List[Knight]:
        return [Knight(knight) for knight in knight_config.values()]

    @classmethod
    def battle(cls, knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

        if knight_1.hp < 0:
            knight_1.hp = 0

        if knight_2.hp < 0:
            knight_2.hp = 0

        cls.battle_info[knight_1.name] = knight_1.hp
        cls.battle_info[knight_2.name] = knight_2.hp
