from app.knight.knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def combat(self) -> dict:
        self.first_knight.hp -= (self.second_knight.power
                                 - self.first_knight.protection)
        self.second_knight.hp -= (self.first_knight.power
                                  - self.second_knight.protection)

        self.first_knight.hp = max(self.first_knight.hp, 0)
        self.second_knight.hp = max(self.second_knight.hp, 0)

        return {
            self.first_knight.name: self.first_knight.hp,
            self.second_knight.name: self.second_knight.hp
        }
