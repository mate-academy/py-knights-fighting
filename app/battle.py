from app.knight import Knight


def fight(first: Knight, second: Knight) -> None:
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection

    first.hp = max(0, first.hp)
    second.hp = max(0, second.hp)
