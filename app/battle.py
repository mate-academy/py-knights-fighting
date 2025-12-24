from app.knights import Knights

class Battle:
    def __init__(self, knight1, knight2):
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self):
        k1_damage = max(0, self.knight1.power - self.knight2.protection)
        k2_damage = max(0, self.knight2.power - self.knight1.protection)

        self.knight2.hp -= k1_damage
        self.knight1.hp -= k2_damage

        if self.knight2.hp <= 0:
            self.knight2.hp = 0
        if self.knight1.hp <= 0:
            self.knight1.hp = 0
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp
        }
