from app.config import knights_config
from app.models.knight import Knight
from app.models.battle import fight


def battle(knights_config: dict) -> dict:
    lancelot = Knight.config_optimize(knights_config["lancelot"])
    arthur = Knight.config_optimize(knights_config["arthur"])
    mordred = Knight.config_optimize(knights_config["mordred"])
    red_knight = Knight.config_optimize(knights_config["red_knight"])
    print(lancelot)
    print(arthur)
    print(mordred)
    print(red_knight)
    results = {}

    result1 = fight(lancelot, mordred)
    results.update(result1)
    print(results)
    result2 = fight(arthur, red_knight)
    results.update(result2)
    print(results)
    return results


result = battle(knights_config)
