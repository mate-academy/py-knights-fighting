from app.knights.knight import Knights


class Round:
    def __init__(self, player1: Knights, player2: Knights) -> None:
        self.player1 = player1
        self.player2 = player2

    def round(self) -> tuple:
        self.player1.hp -= self.player2.power - self.player1.protection
        self.player2.hp -= self.player1.power - self.player2.protection

        return self.player1, self.player2
