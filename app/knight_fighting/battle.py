from .knight import Knight


class Battle:
    def __init__(self, first: Knight, second: Knight) -> None:
        self.first = first
        self.second = second
        self.winner = None

    def simulate_battle(self) -> None:
        self.first.hp -= self.second.power - self.first.protection
        self.second.hp -= self.first.power - self.second.protection

        if self.first.hp <= 0:
            self.winner = self.second.name
            self.first.hp = 0

        if self.second.hp <= 0:
            self.winner = self.first.name
            self.second.hp = 0

        if self.first.hp == 0 and self.second.hp == 0:
            self.winner = None

    def get_winner(self) -> str:
        if self.winner:
            return f"The winner is {self.winner}!"
        else:
            return "There is no winner in the battle"
