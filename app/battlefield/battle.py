from app.knights.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def battle(self) -> None:
        self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
        self.knight_2.hp -= self.knight_1.power - self.knight_2.protection

        if self.knight_1.hp <= 0:
            self.knight_1.hp = 0
        if self.knight_2.hp <= 0:
            self.knight_2.hp = 0


if __name__ == "__main__":
    knight_1 = Knight(name="Lancelot", power=80, hp=100)
    knight_2 = Knight(name="red", power=45, hp=75)
    battle = Battle(knight_1, knight_2)
    battle.battle()
    print(knight_1.hp, knight_2.hp)
