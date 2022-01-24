class Battle:

    def __init__(self, knight_1, knight_2):
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def start_battle(self):
        while True:
            if self.knight_1.hp <= 0:
                self.knight_1 = 0
                print(f"Win {self.knight_2}")
                break
            if self.knight_2.hp <= 0:
                self.knight_2 = 0
                print(f"Win {self.knight_1}")
                break

            self.knight_1.hp -= self.knight_2.power - self.knight_1.protection
            self.knight_2.hp -= self.knight_1.power - self.knight_2.protection
