from app.KnightConfiguration import KNIGHTS
from app.battle import Battle


def battle(knights_config: dict) -> dict:
    return Battle.battle(knights_config)


print(battle(KNIGHTS))
