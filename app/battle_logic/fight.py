from app.battle_preparation.knight import Knight


class Fight:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first = first_knight
        self.second = second_knight

    def begin_battle(self) -> None:
        self.first.hp -= self.second.power - self.first.protection
        self.second.hp -= self.first.power - self.second.protection
        if self.first.hp < 0:
            self.first.hp = 0
        if self.second.hp < 0:
            self.second.hp = 0
