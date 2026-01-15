from app.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> None:
        self.knight2.take_damage(self.knight1.power - self.knight2.protection)
        self.knight1.take_damage(self.knight2.power - self.knight1.protection)
