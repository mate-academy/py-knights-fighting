from app.knights.knights_base import Knight


class Battle:
    @staticmethod
    def battle_moves(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        for knight in [knight_1, knight_2]:
            if knight.hp < 0:
                knight.hp = 0
