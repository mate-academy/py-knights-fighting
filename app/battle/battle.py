from app.people.knight import Knight


class Battle:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1_damage = knight2.power - knight1.protection
        knight2_damage = knight1.power - knight2.protection

        knight1.hp -= knight1_damage
        knight2.hp -= knight2_damage

        if knight1.hp < 0:
            knight1.hp = 0

        if knight2.hp < 0:
            knight2.hp = 0
