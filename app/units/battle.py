from app.units.knight import Knight


class Battle:

    @staticmethod
    def execute(knight_1: Knight, knight_2: Knight) -> dict:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        if knight_1.hp <= 0:
            knight_1.hp = 0
        if knight_2.hp <= 0:
            knight_2.hp = 0
        return {
            knight_1.name: knight_1.hp,
            knight_2.name: knight_2.hp,
        }
