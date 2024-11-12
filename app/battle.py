from app.knights.knight import Knight


class Battle:

    @staticmethod
    def fight(knight1: Knight,
              knight2: Knight,
              knight3: Knight,
              knight4: Knight) -> dict:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection
        knight3.hp -= knight4.power - knight3.protection
        knight4.hp -= knight3.power - knight4.protection

        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0
        if knight3.hp < 0:
            knight3.hp = 0
        if knight4.hp < 0:
            knight4.hp = 0

        return {
            knight1.name: knight1.hp,
            knight2.name: knight2.hp,
            knight3.name: knight3.hp,
            knight4.name: knight4.hp
        }
