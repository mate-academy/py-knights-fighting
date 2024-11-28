from app.knight import Knight


class Battle:
    def __init__(self) -> None:
        pass

    @staticmethod
    def battle_knights(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

        if knight_1.hp <= 0:
            knight_1.hp = 0

        if knight_2.hp <= 0:
            knight_2.hp = 0
