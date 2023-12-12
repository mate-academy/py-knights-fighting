from knights_class import Knight


def calculate_battle(fighters: list[list[Knight]]) -> dict:
    result = {}
    for fighter in fighters:
        first_knight = fighter[0]
        second_knight = fighter[1]

        first_knight.hp -= second_knight.power - first_knight.protection
        if first_knight.hp <= 0:
            first_knight.hp = 0
        result[first_knight.name] = first_knight.hp

        second_knight.hp -= first_knight.power - second_knight.protection
        if second_knight.hp <= 0:
            second_knight.hp = 0
        result[second_knight.name] = second_knight.hp

    return result
