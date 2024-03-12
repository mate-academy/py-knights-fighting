from app.knights.characteristics import KnightsCharacteristics


class Battle:
    @staticmethod
    def one_battle(
        knight_1: KnightsCharacteristics,
        knight_2: KnightsCharacteristics
    ) -> tuple:
        def battle_damage(
            knight: KnightsCharacteristics,
            opponent: KnightsCharacteristics
        ) -> int:

            return knight.total_power() - opponent.protection()

        knight_1_hp = knight_1.total_hp()
        knight_2_hp = knight_2.total_hp()

        knight_1_hp -= battle_damage(knight_2, knight_1)
        knight_2_hp -= battle_damage(knight_1, knight_2)

        knight_1_hp = max(knight_1_hp, 0)
        knight_2_hp = max(knight_2_hp, 0)

        return knight_1_hp, knight_2_hp
