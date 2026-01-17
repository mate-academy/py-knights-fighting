from app.characters.knight import Knight


def fight(
        knight_number_1: Knight,
        knight_number_2: Knight
) -> None:
    knight_number_1.hp -= knight_number_2.power - knight_number_1.protection
    knight_number_2.hp -= knight_number_1.power - knight_number_2.protection

    if knight_number_1.hp <= 0:
        knight_number_1.hp = 0

    if knight_number_2.hp <= 0:
        knight_number_2.hp = 0
