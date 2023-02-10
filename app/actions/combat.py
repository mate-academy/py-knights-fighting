from app.actions.preparations import make_pairs
from app.people.knights import Knight


def fight(knights: dict) -> dict:
    result = {}

    pairs = make_pairs(knights)

    for pair in pairs:
        first_knight = pair[0]
        second_knight = pair[1]

        first_knight.hit(second_knight)
        second_knight.hit(first_knight)
        check_hp(pair)

        result[first_knight.name] = first_knight.hp
        result[second_knight.name] = second_knight.hp

    return result


def check_hp(knights: list[Knight]) -> None:
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0
