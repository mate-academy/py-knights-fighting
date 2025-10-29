from app.characters.Knight import Knight


def take_battle(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    check_hp(first_knight, second_knight)


def check_hp(first_knight: Knight, second_knight: Knight) -> None:
    for knight in [first_knight, second_knight]:
        if knight.hp <= 0:
            knight.hp = 0
