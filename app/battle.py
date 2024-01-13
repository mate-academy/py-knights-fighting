from app.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    # check if someone fell in battle
    for knight in (first_knight, second_knight):
        if knight.hp <= 0:
            knight.hp = 0
