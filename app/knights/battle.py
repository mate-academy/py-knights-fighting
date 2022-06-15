def pvp(knight_left, knight_right):

    knight_left.hp -= knight_right.power - knight_left.protection
    knight_right.hp -= knight_left.power - knight_right.protection

    if knight_left.hp <= 0:
        knight_left.hp = 0
    if knight_right.hp <= 0:
        knight_right.hp = 0
