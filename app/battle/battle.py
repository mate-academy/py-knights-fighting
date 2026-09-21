from app.models.knight import Knight


class Battle:
    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= (
            knight_2.power - knight_1.protection
        )

        knight_2.hp -= (
            knight_1.power - knight_2.protection
        )

        knight_1.hp = max(knight_1.hp, 0)
        knight_2.hp = max(knight_2.hp, 0)
