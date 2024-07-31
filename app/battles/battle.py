from app.knights.knight import Knight


class Battle:
    def __init__(self, first: Knight, second: Knight):
        self.opponent1 = first
        self.opponent2 = second

    def rumble(self):

        self.opponent1.strike(self.opponent2)
        self.opponent2.strike(self.opponent1)
        self.check_if_anyone_died()
        return self.return_results()

    def check_if_anyone_died(self):
        if self.opponent1.hp < 0:
            self.opponent1.hp = 0

        if self.opponent2.hp < 0:
            self.opponent2.hp = 0

    def return_results(self):
        return {
            f"{self.opponent1}": self.opponent1.hp,
            f"{self.opponent2}": self.opponent2.hp
        }
