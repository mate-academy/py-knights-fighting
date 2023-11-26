from app.contestants.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def battle_start(self) -> None:
        self.knight_1.health_points -= (
            self.knight_2.power - self.knight_1.protection
        )
        self.knight_2.health_points -= (
            self.knight_1.power - self.knight_2.protection
        )

    def check_if_fell(self) -> None:
        if self.knight_1.health_points <= 0:
            self.knight_1.health_points = 0

        if self.knight_2.health_points <= 0:
            self.knight_2.health_points = 0
