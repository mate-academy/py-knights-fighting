from app.knight_class import Knight


def battle(knights_dict: dict) -> dict:
    knights = [
        Knight(knight_parameters)
        for knight_parameters in knights_dict.values()
    ]

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
        knights[index].name: knights[index].hp
        for index in range(len(knights))
    }
