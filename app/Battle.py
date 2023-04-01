from app.Knights import Knights


class Battle:
    @staticmethod
    def competition(knight1: Knights, knight2: Knights) -> None:
        knight1.hp -= knight2.power - knight1.protection
        knight2.hp -= knight1.power - knight2.protection

        # check if someone fell in battle
        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0
