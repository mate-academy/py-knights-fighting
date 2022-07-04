from knight.knight import Knight


class Battle:

    def __init__(self, knight1: Knight, knight2: Knight):
        self.knight1, self.knight2 = knight1, knight2

    def attack(self):
        self.knight1.hp -= self.knight2.power - self.knight1.protection
        self.knight2.hp -= self.knight1.power - self.knight2.protection
        if self.knight1.hp < 0:
            self.knight1.hp = 0
        if self.knight2.hp < 0:
            self.knight2.hp = 0
