from app.battle.preparation import Knights


class Battle:
    @staticmethod
    def battle(knight1: Knights, knight2: Knights) -> None:
        knight1.hp = max(
            knight1.hp + knight1.protection - knight2.power, 0
        )
        knight2.hp = max(
            knight2.hp + knight2.protection - knight1.power, 0
        )
