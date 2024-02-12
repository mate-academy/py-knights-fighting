from app.kingdom.knight_prepare import Knights


class Battle:
    battle_result = {}

    @classmethod
    def battle_round(cls,
                     inst_knight_1: Knights,
                     inst_knight_2: Knights) -> None:
        # 1 Lancelot vs Mordred:
        inst_knight_1.hp -= inst_knight_2.power - inst_knight_1.protection
        inst_knight_2.hp -= inst_knight_1.power - inst_knight_2.protection

        # check if someone fell in battle
        if inst_knight_1.hp <= 0:
            inst_knight_1.hp = 0

        if inst_knight_2.hp <= 0:
            inst_knight_2.hp = 0

        cls.battle_result[inst_knight_1.name] = inst_knight_1.hp
        cls.battle_result[inst_knight_2.name] = inst_knight_2.hp
