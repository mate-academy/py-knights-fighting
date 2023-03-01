class Fight:
    def __init__(self, knight1, knight2):
        self.knight1 = knight1
        self.knight2 = knight2
        self.one_to_one()

    def one_to_one(self):
        self.knight1.hp += self.knight1.protection
        self.knight1.hp -= self.knight2.power
        if self.knight1.hp < 0:
            self.knight1.hp = 0

        self.knight2.hp += self.knight2.protection
        self.knight2.hp -= self.knight1.power
        if self.knight2.hp < 0:
            self.knight2.hp = 0
