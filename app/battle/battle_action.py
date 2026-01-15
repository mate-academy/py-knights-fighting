from app.person_knights.knights import Knights


class Battle:

    @staticmethod
    def medieval_battle(
            knight_1: str,
            knight_2: str,
            knights_config: dict
    ) -> tuple[Knights, Knights]:

        knight_1 = Knights(
            knights_config[(knight_1.lower()).replace(" ", "_")]
        )
        knight_2 = Knights(
            knights_config[(knight_2.lower()).replace(" ", "_")]
        )

        Knights.battle_preparations(knight_1)
        Knights.battle_preparations(knight_2)

        # 1 Lancelot vs Mordred:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection

        # check if someone fell in battle
        if knight_1.hp <= 0:
            knight_1.hp = 0

        if knight_2.hp <= 0:
            knight_2.hp = 0

        return knight_1, knight_2
