from app.Knights.Knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def prepare_knights(self) -> None:
        self.first_knight.preparing_of_knight()
        self.second_knight.preparing_of_knight()

    def conduct_battle(self) -> None:
        self.prepare_knights()
        self.first_knight.hp -= (
            self.second_knight.power - self.first_knight.armour
        )
        self.second_knight.hp -= (
            self.first_knight.power - self.second_knight.armour
        )

        self.first_knight.hp = max(0, self.first_knight.hp)
        self.second_knight.hp = max(0, self.second_knight.hp)
