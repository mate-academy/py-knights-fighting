from app.knights.knight import Knight


class Battle:
    def __init__(self, first_knight: Knight, second_knight: Knight) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    @staticmethod
    def check_hp(hp: int) -> int:
        if hp <= 0:
            return 0
        return hp

    def battle(self) -> dict:
        self.first_knight.battle_preparation()
        self.second_knight.battle_preparation()

        self.first_knight.hp -= (self.second_knight.power
                                 - self.first_knight.protection)

        self.second_knight.hp -= (self.first_knight.power
                                  - self.second_knight.protection)

        self.first_knight.hp = Battle.check_hp(self.first_knight.hp)
        self.second_knight.hp = Battle.check_hp(self.second_knight.hp)

        return {
            self.first_knight.name: self.first_knight.hp,
            self.second_knight.name: self.second_knight.hp
        }
