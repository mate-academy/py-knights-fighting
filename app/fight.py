from app.knights import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if_dead(first_knight)
    if_dead(second_knight)


def if_dead(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
