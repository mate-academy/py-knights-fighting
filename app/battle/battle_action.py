from app.knights_person.knight import Knight


class Battle:

    @staticmethod
    def battle(
            knight_1: str,
            knight_2: str,
            knight_stats: dict
    ) -> tuple[Knight, Knight]:
        knight_1 = Knight(knight_stats[(knight_1.lower()).replace(" ", "_")])
        knight_2 = Knight(knight_stats[(knight_2.lower()).replace(" ", "_")])

        Knight.preparations(knight_1)
        Knight.preparations(knight_2)

        # Knight1 vs Knight2:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

        # check if someone fell in battle
        if knight_1.hp <= 0:
            knight_1.hp = 0

        if knight_2.hp <= 0:
            knight_2.hp = 0

        return knight_1, knight_2
