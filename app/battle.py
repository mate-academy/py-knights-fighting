from typing import List

from app.knights.knights import Knight


class Battle:

    @staticmethod
    def start_battle(knights: List[Knight]) -> None:

        # first fight
        knights[0].hp -= knights[2].power - knights[0].protection
        knights[2].hp -= knights[0].power - knights[2].protection

        # second fight
        knights[1].hp -= knights[3].power - knights[1].protection
        knights[3].hp -= knights[1].power - knights[3].protection

        for knight in knights:
            Battle.check_hp(knight)

    @staticmethod
    def check_hp(knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0
