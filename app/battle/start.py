from app.knight.creation import Knight


def check_hp(knights: list[Knight]) -> list[Knight]:
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0

    return knights


def get_damage(knight1: Knight, knight2: Knight) -> list[Knight]:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    return check_hp([knight1, knight2])
