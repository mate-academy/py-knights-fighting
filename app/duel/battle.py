from app.knight.knight import Knight


class Battle:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1_damage = max(0, knight2.power - knight1.protect)
        knight1.hp = max(0, knight1.hp - knight1_damage)

        knight2_damage = max(0, knight1.power - knight2.protect)
        knight2.hp = max(0, knight2.hp - knight2_damage)
