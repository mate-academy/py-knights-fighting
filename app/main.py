from app.data import KNIGHTS, draw
from app.knights import set_knights, duel


def battle(knights_config: dict) -> dict:

    knights = set_knights(knights_config)

    for fighter1, fighter2 in draw.items():
        duel(knights[fighter1], knights[fighter2])

    return {knight.name : knight.hp for _, knight in knights.items()}
