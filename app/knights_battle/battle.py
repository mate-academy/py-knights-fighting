from app.knights_battle.knight import Knight


def battle_between_two(knight_1: Knight, knight_2: Knight) -> None:
    hp_1 = knight_1.total_hp() + knight_1.total_protection()
    hp_2 = knight_2.total_hp() + knight_2.total_protection()
    hp_1 -= knight_2.total_power()
    hp_2 -= knight_1.total_power()
    knight_1.hp = max(0, hp_1)
    knight_2.hp = max(0, hp_2)
