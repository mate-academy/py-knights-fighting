from app.knight_setup.battle_preparation import Knight


class Battle:
    @staticmethod
    def vs(fighter_1: Knight, fighter_2: Knight) -> None:
        fighter_1.hp -= fighter_2.power - fighter_1.protection
        fighter_2.hp -= fighter_1.power - fighter_2.protection
        fighter_1.hp = max(0, fighter_1.hp)
        fighter_2.hp = max(0, fighter_2.hp)

    @staticmethod
    def battle_results(knights: list[Knight]) -> dict:
        return {knight.name: knight.hp
                for knight in knights}
