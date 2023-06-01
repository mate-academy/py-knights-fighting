from app.knights.knight import Knight


class Battle:
    @staticmethod
    def battle(knight1: Knight, knight2: Knight) -> None:
        knight1.take_damage(knight2.power)
        knight2.take_damage(knight1.power)
