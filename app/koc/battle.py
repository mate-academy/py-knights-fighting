from app.koc.knight import Knight


class Battle:
    result = {}

    def begin(self, knight1: Knight, knight2: Knight) -> None:
        knight1.attack(knight2)
        knight2.attack(knight1)

        self.result[knight1.name] = knight1.hp
        self.result[knight2.name] = knight2.hp
