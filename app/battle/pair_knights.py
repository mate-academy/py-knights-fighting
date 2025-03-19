from typing import AnyStr


class PairKnights:

    @staticmethod
    def battle_pair_result(knight1: AnyStr, knight2: AnyStr) -> [int, int]:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        if knight1.hp <= 0:
            knight1.hp = 0
        if knight2.hp <= 0:
            knight2.hp = 0
        return knight1.hp, knight2.hp
