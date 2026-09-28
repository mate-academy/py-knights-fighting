from app.arena import duel
from app.config import DUELS, KNIGHTS
from app.knights import Knight


def battle(knights_config: dict) -> dict[str, int]:
    knights = {
        key: Knight.from_dict(data) for key, data in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    for first_key, second_key in DUELS:
        duel(knights[first_key], knights[second_key])

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
