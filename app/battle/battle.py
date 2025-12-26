from app.knight.knight import Knight


class Battle:
    def __init__(self, knight_one: Knight, knight_two: Knight) -> None:
        self.knight_one = knight_one
        self.knight_two = knight_two

    def fight(self) -> dict:
        self.knight_one.hp -= \
            self.knight_two.power - self.knight_one.protection
        self.knight_two.hp -= \
            self.knight_one.power - self.knight_two.protection

        self.knight_one.hp = max(self.knight_one.hp, 0)
        self.knight_two.hp = max(self.knight_two.hp, 0)

        return {
            self.knight_one.name: self.knight_one.hp,
            self.knight_two.name: self.knight_two.hp
        }
