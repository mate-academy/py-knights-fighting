from app.knights_data import KNIGHTS
from app.knights_duel import duel_of_knights


def battle(knights_config: dict) -> dict:
    first_results = duel_of_knights(
        knights_config["lancelot"], knights_config["mordred"]
    )
    second_results = duel_of_knights(
        knights_config["arthur"], knights_config["red_knight"]
    )
    results = {**first_results, **second_results}
    return results


print(battle(KNIGHTS))
