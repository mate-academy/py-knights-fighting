from app.preparing import Preparing


class Battle:
    def __init__(self, player1: Preparing, player2: Preparing) -> None:
        self.player1 = player1
        self.player2 = player2

    def battle_result(self) -> None:
        self.player1.hp -= self.player2.power - self.player1.protection
        self.player2.hp -= self.player1.power - self.player2.protection

        self.player1.hp = max(0, self.player1.hp)
        self.player2.hp = max(0, self.player2.hp)
