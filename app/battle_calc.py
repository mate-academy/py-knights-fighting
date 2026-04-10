from app.knight import Knight


def battle_calc(knight1: Knight, knight2: Knight) -> list:
    knights = [knight1, knight2]

    print(knight1.knight_hp, knight2.knight_hp)

    # battle
    knight1.knight_hp -= knight2.knight_power - knight1.knight_protection
    knight2.knight_hp -= knight1.knight_power - knight2.knight_protection

    # health check
    for knight in knights:
        if knight.knight_hp <= 0:
            knight.knight_hp = 0

    return [knight1.knight_hp, knight2.knight_hp]
