from app.data import KNIGHTS
from app.fight import fight
from app.knights import Knight


def battle(config: dict) -> dict:
    lancelot = Knight(**config["lancelot"])
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])

    fight_results = {}
    fight_results.update(fight(lancelot, mordred))
    fight_results.update(fight(arthur, red_knight))

    return fight_results


print(battle(KNIGHTS))
