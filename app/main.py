"""Entry point: resolves the Camelot tournament battles."""

from app.config import BATTLE_PAIRS, KNIGHTS
from app.knight import Knight, fight


def battle(knights_config: dict) -> dict:
    results = {}
    for first_key, second_key in BATTLE_PAIRS:
        first = Knight.from_config(knights_config[first_key])
        second = Knight.from_config(knights_config[second_key])
        results.update(fight(first, second))
    return results


if __name__ == "__main__":
    print(battle(KNIGHTS))
