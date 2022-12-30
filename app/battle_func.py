from app.knight_class import Knight


def battle(knights_dict: dict) -> dict:
    knights = []
    for key, value in knights_dict.items():
        key = Knight(value)
        key.drink_the_potion()
        knights.append(key)

    for index in range(len(knights)):
        if index < len(knights) / 2:
            knights[index].hp -= (
                knights[index + 2].power - knights[index].protection
            )
        else:
            knights[index].hp -= (
                knights[index - 2].power - knights[index].protection
            )
        if knights[index].hp <= 0:
            knights[index].hp = 0

    return {
        knights[0].name: knights[0].hp,
        knights[1].name: knights[1].hp,
        knights[2].name: knights[2].hp,
        knights[3].name: knights[3].hp,
    }
