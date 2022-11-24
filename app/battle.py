from app.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def conduct_battle(self) -> None:
        self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
        self.knight_1.hp = self.check_hp(self.knight_1.hp)
        self.knight_2.hp -= self.knight_1.power - self.knight_2.protection
        self.knight_2.hp = self.check_hp(self.knight_2.hp)

    @staticmethod
    def check_hp(hp: int) -> int:
        if hp <= 0:
            hp = 0

        return hp
