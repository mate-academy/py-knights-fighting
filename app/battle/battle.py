from app.knight_setup.battle_preparation import Knight


def calculate_final_hp(fighter: Knight) -> None:
    if fighter.hp <= 0:
        fighter.hp = 0


class Battle:
    @staticmethod
    def vs(fighter_1: Knight, fighter_2: Knight) -> None:
        fighter_1.hp -= fighter_2.power - fighter_1.protection
        fighter_2.hp -= fighter_1.power - fighter_2.protection
        calculate_final_hp(fighter_1)
        calculate_final_hp(fighter_2)

    @staticmethod
    def battle_results(knights: list[Knight]) -> dict:
        return {knight.name: knight.hp
                for knight in knights}
