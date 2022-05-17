def versus(knight_1, knight_2):
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection


def check_if_die(knight):
    if knight.hp <= 0:
        knight.hp = 0
