class Battle:
    @staticmethod
    def battle(knight1: [int, int, int], knight2: [int, int, int]) -> None:
        knight1.hp = (
            knight1.hp + knight1.protection - knight2.power
            if knight1.hp + knight1.protection > knight2.power else 0
        )
        knight2.hp = (
            knight2.hp + knight2.protection - knight1.power
            if knight2.hp + knight2.protection > knight1.power else 0
        )
