from app.artifacts.knight import Knight


class Battle:
    pass


class BattleGround:
    def __init__(self) -> None:
        self.knights = {}

    def add_knight(self, knight: Knight) -> None:
        self.knights[knight.name] = knight

    def fight(self, knight1_name: str, knight2_name: str) -> None:
        knight1 = self.knights[knight1_name]
        knight2 = self.knights[knight2_name]

        knight1_stats = knight1.get_stats()
        knight2_stats = knight2.get_stats()

        knight1_hp = (knight1_stats.hp
                      - knight2_stats.power
                      + knight1_stats.protection)
        knight2_hp = (knight2_stats.hp
                      - knight1_stats.power
                      + knight2_stats.protection)

        knight1.hp = knight1_hp if knight1_hp > 0 else 0
        knight2.hp = knight2_hp if knight2_hp > 0 else 0

    def results(self) -> dict:
        return {knight.name: knight.hp for knight in self.knights.values()}
