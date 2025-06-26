from app.knights.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def start_battle(self) -> dict:
        self.knight_1.hp -= (
            max(0, (self.knight_2.power - self.knight_1.protection)))
        if self.knight_1.hp < 0:
            self.knight_1.hp = 0
        self.knight_2.hp -= (
            max(0, (self.knight_1.power - self.knight_2.protection)))
        if self.knight_2.hp < 0:
            self.knight_2.hp = 0
        return {
            self.knight_1.name: self.knight_1.hp,
            self.knight_2.name: self.knight_2.hp,
        }
