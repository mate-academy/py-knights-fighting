from app.knights.knights_init import Knight


def fight(knight_1: Knight, knight_2: Knight) -> tuple[Knight, Knight]:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    # check if someone fell in battle
    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0

    return knight_1, knight_2
