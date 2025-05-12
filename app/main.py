from app.game.battle import Battle
from app.game.heroes import Knight


def battle(knights_config: dict) -> dict:
    knights = []
    for knight_config in knights_config.values():
        knights.append(Knight(config=knight_config))

    Battle(first_knight=knights[0], second_knight=knights[2]).fight()
    Battle(first_knight=knights[1], second_knight=knights[3]).fight()

    return {knight.name: knight.hp for knight in knights}
