from app.structuring_the_knight_personality import Knight


class BattleOfTwoKnight:
    @staticmethod
    def battle_action_phase(knight_1: Knight, knight_2: Knight) -> None:

        damage_for_first_knight = knight_2.power - knight_1.protection
        damage_for_second_knight = knight_1.power - knight_2.protection
        knight_1.hp -= max(0, damage_for_first_knight)
        knight_2.hp -= max(0, damage_for_second_knight)

    @staticmethod
    def result_after_battle(knight: Knight) -> None:

        knight.hp = max(0, knight.hp)
