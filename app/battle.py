from app.knights import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight):
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self):
        damage_to_1 = max(0, self.knight2.power - self.knight1.protection)
        damage_to_2 = max(0, self.knight1.power - self.knight2.protection)

        self.knight1.receive_damage(damage_to_1)
        self.knight2.receive_damage(damage_to_2)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
