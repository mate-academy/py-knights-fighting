from .knights import Knight


class KnightsBattle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def make_a_battle(self) -> None:
        self.first_knight.hp -= (self.second_knight.power
                                 - self.first_knight.protection)
        self.second_knight.hp -= (self.first_knight.power
                                  - self.second_knight.protection)

    def check_results(self) -> None:
        if self.first_knight.hp <= 0:
            self.first_knight.hp = 0

        if self.second_knight.hp <= 0:
            self.second_knight.hp = 0
