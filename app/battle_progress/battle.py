
from app.battle_preparation.knights import Knight


class Battle:
    @staticmethod
    def check_hp(knight: Knight) -> int:
        return knight.hp if knight.hp > 0 else 0

    @staticmethod
    def fight(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power - first_knight.protection
        second_knight.hp -= first_knight.power - second_knight.protection

        first_knight.hp = Battle.check_hp(first_knight)
        second_knight.hp = Battle.check_hp(second_knight)

    @staticmethod
    def battle_result(knights: list) -> dict:
        return {knight.name: knight.hp for knight in knights}
