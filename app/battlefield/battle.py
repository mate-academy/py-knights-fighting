from app.knights.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    @staticmethod
    def if_die(knight: Knight) -> None:
        if knight.hp <= 0:
            knight.hp = 0

    def battle(self) -> None:

        self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
        self.if_die(self.knight_1)

        self.knight_2.hp -= self.knight_1.power - self.knight_2.protection
        self.if_die(self.knight_2)
