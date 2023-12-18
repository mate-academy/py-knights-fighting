from app.knights import Knight


class Battle:
    @staticmethod
    def single_battle(knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        knight1.hp = Battle.update_hp(knight1)
        knight2.hp = Battle.update_hp(knight2)

    @staticmethod
    def update_hp(knight: Knight) -> int:
        if knight.hp < 0:
            knight.hp = 0
        return knight.hp

    @staticmethod
    def result_dict(knights: list[Knight]) -> dict:
        return {knight.name: knight.hp for knight in knights}
