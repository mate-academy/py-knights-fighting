from models.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight):
        self.k1 = knight1
        self.k2 = knight2

    def fight(self) -> dict:
        self.k1.hp -= max(self.k2.power - self.k1.protection, 0)
        self.k2.hp -= max(self.k1.power - self.k2.protection, 0)

        self.k1.hp = max(self.k1.hp, 0)
        self.k2.hp = max(self.k2.hp, 0)

        return {
            self.k1.name: self.k1.hp,
            self.k2.name: self.k2.hp,
        }
