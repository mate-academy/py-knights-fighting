class Battle:
    def __init__(self, opponents: list) -> None:
        self.opponents = opponents

    def fight(self) -> None:
        for knight_1, knight_2 in self.opponents:
            knight_1.hp -= knight_2.power - knight_1.protection
            knight_2.hp -= knight_1.power - knight_2.protection

            if knight_1.hp <= 0:
                knight_1.hp = 0

            if knight_2.hp <= 0:
                knight_2.hp = 0

    def get_results(self) -> dict:
        results = {}

        for knight_1, knight_2 in self.opponents:
            results[knight_1.name] = knight_1.hp
            results[knight_2.name] = knight_2.hp
        return results
