from app.knight import Knight


class Battle:
    @classmethod
    def two_knights_battle(cls, knights: list[Knight]):
        for i in range(len(knights)):
            knights[i].hp -= \
                knights[(i + 1) % len(knights)].power - knights[i].protection
            Battle.fix_hp_if_fell(knights[i])

    @staticmethod
    def fix_hp_if_fell(knight: Knight):
        if knight.hp < 0:
            knight.hp = 0
