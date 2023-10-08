from app.preparations_for_batle.create_knights import Knight


class BattleKnights:

    @staticmethod
    def check_hp(knight: Knight) -> int:
        return knight.hp if knight.hp > 0 else 0

    @staticmethod
    def battle(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        first_knight.hp = BattleKnights.check_hp(first_knight)
        second_knight.hp = BattleKnights.check_hp(second_knight)

    @staticmethod
    def battle_result(knights: list) -> dict:
        return {
            knights[0].name: knights[0].hp,
            knights[1].name: knights[1].hp,
            knights[2].name: knights[2].hp,
            knights[3].name: knights[3].hp,
        }
