from app.battle_preparations.armor import Armour


class Fight:
    def __init__(self, knight_1: Armour, knight_2: Armour) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def fight(self) -> None:

        self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
        self.knight_2.hp -= self.knight_1.power - self.knight_2.protection

        if self.knight_1.hp < 0:
            self.knight_1.hp = 0
        if self.knight_2.hp < 0:
            self.knight_2.hp = 0
