from app.battle import Battle
from app.knights.knights_config import Knight


def battle(knights_config: dict) -> dict:
    Knight.initialize_knights(knights_config)

    lancelot = Knight.collection["Lancelot"]
    arthur = Knight.collection["Arthur"]
    mordred = Knight.collection["Mordred"]
    red_knight = Knight.collection["Red Knight"]

    duels = [
        (lancelot, mordred),
        (arthur, red_knight)
    ]
    result = Battle.battle(duels)
    return result
