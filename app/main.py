from app.converter.data import convert_data_to_knights
from app.person.knight import Knight


def battle(data: dict) -> dict:
    knights = convert_data_to_knights(data)
    prepare_knights_to_battle(knights)

    fight(knights[0], knights[2])
    fight(knights[1], knights[3])

    return {knight.name: knight.hp for knight in knights}


def prepare_knights_to_battle(knights: list[Knight]) -> None:
    for knight in knights:
        knight.prepare_to_battle()


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection

    if first_knight.hp < 0:
        first_knight.hp = 0
    if second_knight.hp < 0:
        second_knight.hp = 0
