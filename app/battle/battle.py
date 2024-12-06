from app.adapters.battle_adapter import BattleAdapter
from app.fighters.knight import Knight


class Battle:
    def __init__(self, battle_data: BattleAdapter) -> None:
        self.knights = set(
            Knight(knight_data)
            for knight_data
            in battle_data.knight_datas
        )

    def __str__(self) -> str:
        return str(self.knights)

    @staticmethod
    def prepare(first_knight: Knight, second_knight: Knight):
        ...

    @staticmethod
    def fight(first_knight: Knight, second_knight: Knight) -> None:
        while first_knight.is_alive() and second_knight.is_alive():
            first_knight.attack(second_knight)

            Battle.is_battle_over(first_knight, second_knight)

            second_knight.attack(first_knight)

            Battle.is_battle_over(first_knight, second_knight)

    @staticmethod
    def is_battle_over(
            first_knight: Knight,
            second_knight: Knight
    ) -> bool:
        return first_knight.is_alive() and second_knight.is_alive()
