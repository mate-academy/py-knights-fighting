from app.data.battle_data import BattleData
from app.fighters.knight import Knight


class Battle:
    def __init__(self, battle_data: BattleData):
        self.knights = set(
            Knight(knight_data)
            for knight_data
            in battle_data.knights_data
        )

    @staticmethod
    def fight(first_knight: Knight, second_knight: Knight):
        ...

    @staticmethod
    def check_win_conditions(first_knight: Knight, second_knight: Knight):
        ...

    def __str__(self):
        return str(self.knights)