from knights_class import Knight


def calculate_battle(fighters: list[list[Knight]]) -> dict:
    result = {}
    for fighter in fighters:
        first_knight = fighter[0]
        second_knight = fighter[1]

        first_knight.battle_match(second_knight)
        result[first_knight.name] = first_knight.hp

        second_knight.battle_match(first_knight)
        result[second_knight.name] = second_knight.hp

    return result
