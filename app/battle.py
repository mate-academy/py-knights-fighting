# battle.py
class Battle:
    def __init__(self, knight1, knight2):
        self.knight1 = knight1
        self.knight2 = knight2

    def conduct(self):
        self.knight1.prepare_for_battle()
        self.knight2.prepare_for_battle()

        self.knight1.hp -= max(0, self.knight2.power - self.knight1.protection)
        self.knight2.hp -= max(0, self.knight1.power - self.knight2.protection)

        self.knight1.hp = max(0, self.knight1.hp)
        self.knight2.hp = max(0, self.knight2.hp)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
