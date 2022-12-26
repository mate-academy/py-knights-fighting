from app.model.knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def fight(self):
        self.first_knight.hp -= self.second_knight.power - self.first_knight.protection
        self.second_knight.hp -= self.first_knight.power - self.second_knight.protection
        self.first_knight.check_if_fell_in_battle()
        self.second_knight.check_if_fell_in_battle()
