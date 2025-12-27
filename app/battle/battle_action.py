from app.knight.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def do_battle(self) -> None:
        self.knight1.hp -= self.knight2.power - self.knight1.protection
        self.knight2.hp -= self.knight1.power - self.knight2.protection

        self.knight1.hp = self.hp_to_zero(self.knight1.hp)
        self.knight2.hp = self.hp_to_zero(self.knight2.hp)

    @staticmethod
    def hp_to_zero(hp: int) -> int:
        return 0 if hp < 0 else hp
