from app.knights.knight import Knight


class Fight:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        knight1.hp = knight1.check_hp()
        knight2.hp = knight2.check_hp()
