from app.fighters.knight import Knight


class Battle:

    @staticmethod
    def update_hp(knight_1: Knight, knight_2: Knight) -> None:
        stats_1 = knight_1.calculate_stats()
        stats_2 = knight_2.calculate_stats()
        knight_1.hp = max(stats_1["hp"]
                          - (stats_2["power"] - stats_1["protection"]), 0)
        knight_2.hp = max(stats_2["hp"]
                          - (stats_1["power"] - stats_2["protection"]), 0)

    @staticmethod
    def battle_result(knights: list[Knight]) -> dict:
        return {knight.name: knight.hp for knight in knights}
