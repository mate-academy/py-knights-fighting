from app.knight import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    first_knight.hp = max(first_knight.hp, 0)

    second_knight.hp -= first_knight.power - second_knight.protection
    second_knight.hp = max(second_knight.hp, 0)
