from app.people.knight import Knight


def battle(knight_config: dict) -> dict:
    knights = [
        Knight(name=key, config=value)
        for key, value in knight_config.items()
    ]

    result = dict()

    for i in range(2):
        result.update(knights[i].fight_with(knight=knights[i + 2]))

    return result
