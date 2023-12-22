from app.stats.knight_final_stats import KnightStats
from app.stats.knight_base_stats import KNIGHTS
from app.fight import fighting


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    lancelot = KnightStats(knights_config["lancelot"]).final_stats()
    mordred = KnightStats(knights_config["mordred"]).final_stats()
    arthur = KnightStats(knights_config["arthur"]).final_stats()
    red_knight = KnightStats(knights_config["red_knight"]).final_stats()

    # -------------------------------------------------------------------------------
    # BATTLE:
    round_1 = fighting(lancelot, mordred)

    round_2 = fighting(arthur, red_knight)

    # Return battle results:
    result = round_1.copy()
    result.update(round_2)
    return result


print(battle(KNIGHTS))
