from app.knight import Knight


def result(first: Knight,
           second: Knight) -> None:
    # BATTLE:

    # 1 Lancelot vs Mordred:
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection

    # check if someone fell in battle
    if first.hp <= 0:
        first.hp = 0

    if second.hp <= 0:
        second.hp = 0
