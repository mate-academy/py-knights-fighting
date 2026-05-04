from app.config import KNIGHTS
from app.knight import Knight
from app.battle import Battle


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights = {
        knight: Knight(config)
        for knight, config in knights_config.items()
    }

    # -------------------------------------------------------------------------------
    # BATTLE:

    duel_pairs = (
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    )

    for first_knight, second_knight in duel_pairs:
        duel = Battle([
            knights[first_knight],
            knights[second_knight],
        ])
        duel.run_duel(rounds=1)

    return {
        knight.name: knight.get_hp()
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
