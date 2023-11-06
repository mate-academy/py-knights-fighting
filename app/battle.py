from app.knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.knight_1 = first_knight
        self.knight_2 = second_knight

    def start(self) -> None:
        hp_1 = self.knight_1.hp - (
            self.knight_2.power - self.knight_1.protection
        )
        hp_2 = self.knight_2.hp - (
            self.knight_1.power - self.knight_2.protection
        )
        self.knight_1.set_hp(hp_1)
        self.knight_2.set_hp(hp_2)
