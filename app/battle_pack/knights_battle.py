from app.knights_pack.knights_data import Knight


class KnightsBattle:

    @staticmethod
    def battle(kn_1: Knight, kn_2: Knight) -> None:
        kn_1.knight_hp -= kn_2.knight_power - kn_1.knight_protection
        kn_2.knight_hp -= kn_1.knight_power - kn_2.knight_protection
        if kn_1.knight_hp <= 0:
            kn_1.knight_hp = 0
        if kn_2.knight_hp <= 0:
            kn_2.knight_hp = 0
