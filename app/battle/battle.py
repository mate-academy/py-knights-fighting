from app.preparation.knight import Knight


class Battle:
    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

    @staticmethod
    def was_slain(knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0
