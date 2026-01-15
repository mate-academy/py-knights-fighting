from app.knights_change.knights import Knights


def find_winner(
        first_knight: "Knights",
        second_knight: "Knights"
) -> Knights | str:
    if first_knight.hp <= 0:
        first_knight.hp = 0
    elif second_knight.hp <= 0:
        second_knight.hp = 0
    if first_knight.hp < second_knight.hp:
        return second_knight
    elif first_knight.hp > second_knight.hp:
        return first_knight
    else:
        return "Draw"


def duel(first_knight: "Knights", second_knight: "Knights") -> None:
    damage_to_first = max(0, second_knight.power - first_knight.protection)
    damage_to_second = max(0, first_knight.power - second_knight.protection)

    first_knight.hp -= damage_to_first
    second_knight.hp -= damage_to_second

    return find_winner(first_knight, second_knight)


def battle_result() -> dict:
    result = {}
    for knight_key in Knights.all_knights:
        knight = Knights.all_knights[knight_key]
        result[knight.name] = knight.hp
    return result
