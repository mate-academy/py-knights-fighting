from app.knights.knight import Knight


class Round:
    def __init__(self, player1: Knight, player2: Knight) -> None:
        self.player1 = player1
        self.player2 = player2

    def round(self) -> tuple:
        self.player1.hp -= self.player2.power - self.player1.protection
        self.player2.hp -= self.player1.power - self.player2.protection
        if self.player1.hp < 0:
            self.player1.hp = 0
        if self.player2.hp < 0:
            self.player2.hp = 0
        return self.player1, self.player2
