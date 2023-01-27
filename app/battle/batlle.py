from app.knight.knight import Knight


def battle_for_two(first_knight: Knight, second_knight: Knight) -> dict:
    first_knight.hp = first_knight.hp - second_knight.power
    second_knight.hp = second_knight.hp - first_knight.power

# check if someone fell in battle
    if first_knight.hp < 0:
        first_knight.hp = 0

    if second_knight.hp < 0:
        second_knight.hp = 0

    return {
        first_knight.name: first_knight.hp,
        second_knight.name: second_knight.hp
    }
