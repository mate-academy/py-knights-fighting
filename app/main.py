from app.knight import Knight
from app.config import KNIGHTS
from app.arena import Arena


def battle(
        knights_config: dict,
        pairs: list | tuple = None
) -> dict:
    # BATTLE PREPARATIONS:
    knights = Arena.equip_knights(knights_config)

    battle_pairs = pairs or [
        ["lancelot", "mordred"],
        ["arthur", "red_knight"],
    ]

    # ----------------------------------------------
    # BATTLE:
    for pair in battle_pairs:
        Arena.fighting(pair)

    # RESULTS:
    return Knight.get_statistics(knights)


print(battle(KNIGHTS))
