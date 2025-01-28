from app.config import KNIGHTS
from app.models.knight import Knight
from app.models.battle import fight

def battle(KNIGHTS: dict) -> dict:
    lancelot = Knight.config_optimize(KNIGHTS["lancelot"])
    arthur = Knight.config_optimize(KNIGHTS["arthur"])
    mordred = Knight.config_optimize(KNIGHTS["mordred"])
    red_knight = Knight.config_optimize(KNIGHTS["red_knight"])
    print(lancelot)
    print(arthur)
    print(mordred)
    print(red_knight)
    results = {}

    result1 = fight(lancelot, arthur)
    results.update(result1)
    print(results)
    result2 = fight(mordred, red_knight)
    results.update(result2)
    print(results)
    return results

result = battle(KNIGHTS)



