from typing import List

from app.knights.knights import Knight


class Battle:

    @staticmethod
    def start_battle(knights: List[Knight]) -> None:

        lancelot, arthur, mordred, red_knight = knights

        # first fight
        lancelot.hp -= mordred.power - lancelot.protection
        mordred.hp -= lancelot.power - mordred.protection

        # second fight
        arthur.hp -= red_knight.power - arthur.protection
        red_knight.hp -= arthur.power - red_knight.protection

        for knight in knights:
            Battle.check_hp(knight)

    @staticmethod
    def check_hp(knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0
