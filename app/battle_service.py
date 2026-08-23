from app.knight import Knight


class Battle:
    @staticmethod
    def fight(knight_1: Knight, knight_2: Knight) -> None:
        hp_1 = knight_1.hp
        hp_2 = knight_2.hp

        knight_1.hp = max(
            0,
            hp_1 - (
                knight_2.power
                - knight_1.protection
            )
        )

        knight_2.hp = max(
            0,
            hp_2 - (
                knight_1.power
                - knight_2.protection
            )
        )
