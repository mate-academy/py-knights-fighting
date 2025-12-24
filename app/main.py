from app.models.create_models import create_knight
from app.fight.fight import fight


def battle(knights_dict: dict) -> dict:
    knights = [
        create_knight(knight_data=knight[1])
        for knight in knights_dict.items()
        if knight[0] is not None
    ]
    for index in range(len(knights) - 2):
        fight(knights[index], knights[index + 2])
        fight(knights[index + 2], knights[index])

    return {knight.name: knight.hp for knight in knights}
