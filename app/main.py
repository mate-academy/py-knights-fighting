from app.battle import Knight, run_duel
from app.config import DUELS


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    knights = {
        code: Knight.from_config(config)
        for code, config in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    for first_code, second_code in DUELS:
        run_duel(knights[first_code], knights[second_code])

    return {
        knight.name: knight.stats.hp
        for knight in knights.values()
    }
