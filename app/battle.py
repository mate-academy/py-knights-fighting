from app.knights.knights_config import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> None:
        self.knight1.hp -= self.knight2.power - self.knight1.protection
        self.knight2.hp -= self.knight1.power - self.knight2.protection

        self.knight1.hp = max(0, self.knight1.hp)
        self.knight2.hp = max(0, self.knight2.hp)

    @staticmethod
    def battle(duels: list[tuple[Knight, Knight]]) -> dict[str, int]:
        result = {}
        for knight1, knight2 in duels:
            fight = Battle(knight1, knight2)
            fight.fight()

            result[knight1.name] = knight1.hp
            result[knight2.name] = knight2.hp

        return result
