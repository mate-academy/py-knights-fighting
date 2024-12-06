from app.adapters.battle_config import BattleConfig
from app.fighters.knight import Knight


class Battle:
    def __init__(self, battle_data: BattleConfig) -> None:
        self.knights = set(
            Knight(knight_data)
            for knight_data
            in battle_data.knight_datas
        )
        self.pair_count = len(self.knights) // 2
        self.current_pair = 0

    def __str__(self) -> str:
        return str(self.knights)

    def fight_preparations(self):
        for knight in self.knights:
            knight.equip_all_armour()
            knight.equip_best_weapon()
            knight.drink_best_potion()

    def next_pair(self):
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
