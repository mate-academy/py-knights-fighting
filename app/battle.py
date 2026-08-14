from app.knight import Knight


class Battle:

    def __init__(self) -> None:
        self.fighters = {}

    def hold_duel(self, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= max(knight2.power - knight1.protection, 0)
        knight2.hp -= max(knight1.power - knight2.protection, 0)
        knight1.hp = max(knight1.hp, 0)
        knight2.hp = max(knight2.hp, 0)
        self.fighters[knight1.name] = knight1.hp
        self.fighters[knight2.name] = knight2.hp

    def get_battle_results(self) -> dict:
        return self.fighters
