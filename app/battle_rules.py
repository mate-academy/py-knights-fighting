from app.fighters.сharacters import Knight


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    if first_knight.hp <= 0:
        first_knight.hp = 0
    second_knight.hp -= first_knight.power - second_knight.protection
    if second_knight.hp <= 0:
        second_knight.hp = 0
