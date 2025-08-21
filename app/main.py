from app.knights import Knight
from app.battle import duel


def battle(config: dict) -> dict:
    lancelot = Knight(config["lancelot"])
    mordred = Knight(config["mordred"])
    arthur = Knight(config["arthur"])
    red_knight = Knight(config["red_knight"])

    result1 = duel(lancelot, mordred)
    result2 = duel(arthur, red_knight)

    return {**result1, **result2}
