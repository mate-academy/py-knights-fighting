from app.knights.knight import Knight


class Battle:

    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def fight(self) -> int:
        self.first_knight.hp -= (self.second_knight.power
                                 - self.first_knight.protection)
        self.second_knight.hp -= (self.first_knight.power
                                  - self.second_knight.protection)

        if self.first_knight.hp <= 0:
            self.first_knight.hp = 0
            return 2
        elif self.second_knight.hp <= 0:
            self.second_knight.hp = 0
            return 1
        else:
            return 0

    def __str__(self) -> str:
        return f"{self.first_knight} and {self.second_knight.name}"
