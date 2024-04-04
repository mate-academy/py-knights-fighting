from app.knight.create_knight import Knight


def battle_begin(first_knight: Knight, second_knight: Knight) -> None:

    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if first_knight.hp <= 0:
        first_knight.hp = 0
    if second_knight.hp <= 0:
        second_knight.hp = 0


def battle_result(knights: dict) -> dict:
    return {knight.name: knight.hp for knight in knights.values()}
