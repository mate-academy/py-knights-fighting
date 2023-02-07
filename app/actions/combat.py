from app.actions.preparations import make_pairs
from app.people.knights import Knight


def fight(knights: dict) -> dict:
    result = {}

    for pair in make_pairs(knights):
        first_knight = pair[0]
        second_knight = pair[1]

        first_knight.hit(second_knight)
        second_knight.hit(first_knight)
        check_hp(first_knight)
        check_hp(second_knight)

        result[first_knight.name] = first_knight.hp
        result[second_knight.name] = second_knight.hp

    return result


def check_hp(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0
