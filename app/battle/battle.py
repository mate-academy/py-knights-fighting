from app.units.knight import Knight


class Battle:
    def __init__(self) -> None:
        self.pairs = []

    def set_pair(self, knight1: Knight, knight2: Knight) -> tuple:
        pair = (knight1, knight2)
        self.pairs.append(pair)
        return pair

    def show_pairs(self) -> None:
        print("Pairs: ")
        for pair in self.pairs:
            print(f"{pair[0].name} — {pair[1].name}")

    def fight(self) -> None:
        pairs_for_this_battle = list(self.pairs)
        self.pairs = []

        for pair in pairs_for_this_battle:
            knight1 = pair[0]
            knight2 = pair[1]

            damage_to_knight1 = max(0, knight2.power - knight1.protection)
            damage_to_knight2 = max(0, knight1.power - knight2.protection)

            knight1.hp -= damage_to_knight1
            knight2.hp -= damage_to_knight2

        self._check_hp(pairs_for_this_battle)

    def _check_hp(self, fought_pairs: list) -> None:
        for pair in fought_pairs:
            for knight in pair:
                if knight.hp < 0:
                    knight.hp = 0
