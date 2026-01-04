from app.config import KNIGHTS
from app.arena import Arena


def battle(
        knights_config: dict,
        pairs: list | tuple = None
) -> dict:
    # BATTLE PREPARATIONS:
    Arena.equip_knights(knights_config)

    battle_pairs = pairs or [
        ["lancelot", "mordred"],
        ["arthur", "red_knight"],
    ]

    # ----------------------------------------------
    # BATTLE:
    for pair in battle_pairs:
        Arena.battling(pair)

    # RESULTS:
    return Arena.get_statistics()


print(battle(KNIGHTS))
