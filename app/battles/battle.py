from app.knights.knight import Knight


class Battle:
    def __init__(self, first: Knight, second: Knight) -> None:
        self.opponent1 = first
        self.opponent2 = second

    def rumble(self) -> dict:
        self.opponent1.strike(self.opponent2)
        self.opponent2.strike(self.opponent1)
        self.check_if_anyone_died()
        return self.calculate_results()

    def check_if_anyone_died(self) -> None:
        if self.opponent1.hp < 0:
            self.opponent1.hp = 0

        if self.opponent2.hp < 0:
            self.opponent2.hp = 0

    def calculate_results(self) -> dict:
        return {
            f"{self.opponent1}": self.opponent1.hp,
            f"{self.opponent2}": self.opponent2.hp
        }
