from app.knights.knight import Knight


class Battle:
    def __init__(self, knight_1: Knight, knight_2: Knight) -> None:
        self.knight_1 = knight_1
        self.knight_2 = knight_2

    def start_battler(self) -> None:
        self.knight_1.prepare_for_battle()
        self.knight_2.prepare_for_battle()

        damage_to_k1 = max(0, self.knight_2.power - self.knight_1.protection)
        damage_to_k2 = max(0, self.knight_1.power - self.knight_2.protection)

        self.knight_1.hp -= damage_to_k1
        self.knight_2.hp -= damage_to_k2

        if self.knight_1.hp <= 0:
            self.knight_1.hp = 0
        if self.knight_2.hp <= 0:
            self.knight_2.hp = 0
