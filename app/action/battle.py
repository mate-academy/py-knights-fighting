from people.knight import Knight


def fight(knight01: Knight, knight02: Knight) -> dict:
    knight01.hp -= knight02.power - knight01.protection
    knight02.hp -= knight01.power - knight02.protection

    if knight01.hp <= 0:
        knight01.hp = 0

    if knight02.hp <= 0:
        knight02.hp = 0
    return {knight01.name: knight01.hp, knight02.name: knight02.hp}
