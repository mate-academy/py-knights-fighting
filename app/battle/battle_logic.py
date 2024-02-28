from app.knights.characteristics import KnightsCharacteristics


class Battle:
    @staticmethod
    def one_battle(
        knight_1: KnightsCharacteristics,
        knight_2: KnightsCharacteristics
    ) -> tuple:
        knight_1_hp = knight_1.total_hp()
        knight_2_hp = knight_2.total_hp()

        knight_1_hp -= knight_2.total_power() - knight_1.protection()
        knight_2_hp -= knight_1.total_power() - knight_2.protection()

        if knight_1_hp <= 0:
            knight_1_hp = 0

        if knight_2_hp <= 0:
            knight_2_hp = 0

        return knight_1_hp, knight_2_hp
