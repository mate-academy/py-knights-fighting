from app.knights import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def fight(self) -> None:
        self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
        self.knight_2.hp -= self.knight_1.power - self.knight_2.protection

        if self.knight_1.hp <= 0:
            self.knight_1.hp = 0

        if self.knight_2.hp <= 0:
            self.knight_2.hp = 0
