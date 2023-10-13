from app.knight import Knight


def fight(first_knight, second_knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    first_knight.check_hp()
    second_knight.check_hp()


def battle(knights: dict) -> dict:
    list_of_knights = [Knight(knights[name])
                       for name in knights]
    for number in range(0, len(list_of_knights) - 2):
        fight(list_of_knights[number], list_of_knights[number + 2])
    return {knight.name: knight.hp
            for knight in list_of_knights}
