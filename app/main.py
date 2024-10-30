from app.knight import Knight
from app.battle import Battle


def battle(knights_config: dict) -> dict:
    # Initialize knights
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Conduct battles
    battle1 = Battle(lancelot, mordred)
    battle1.conduct_battle()
    result1 = battle1.get_result()

    battle2 = Battle(arthur, red_knight)
    battle2.conduct_battle()
    result2 = battle2.get_result()

    # Combine results
    results = {
        **result1,
        **result2
    }
    return results
