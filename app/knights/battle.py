def pvp(knight_left, knight_right):

    knight_left.hp -= knight_right.power - knight_left.dr
    knight_right.hp -= knight_left.power - knight_right.dr

    if knight_left.hp <= 0:
        knight_left.hp = 0
    if knight_right.hp <= 0:
        knight_right.hp = 0
