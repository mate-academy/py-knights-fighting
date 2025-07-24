from app.units.knight import Knight


class Battle:
    def __init__(self) -> None:
        pass

    pairs = []

    @classmethod
    def set_pair(cls, knight1: Knight, knight2: Knight) -> tuple:
        pair = (knight1, knight2)
        cls.pairs.append(pair)

        return pair

    @classmethod
    def show_pairs(cls) -> None:
        print("Pairs: ")

        for pair in cls.pairs:
            print(f"{pair[0].name} — {pair[1].name}")

    @classmethod
    def fight(cls) -> None:
        for pair in cls.pairs:
            knight1 = pair[0]
            knight2 = pair[1]

            damage_to_knight1 = max(0, knight2.power - knight1.protection)
            damage_to_knight2 = max(0, knight1.power - knight2.protection)

            knight1.hp -= damage_to_knight1
            knight2.hp -= damage_to_knight2

            Battle.check_hp()

    @classmethod
    def check_hp(cls) -> None:
        for pair in cls.pairs:
            for knight in pair:
                if knight.hp < 0:
                    knight.hp = 0
