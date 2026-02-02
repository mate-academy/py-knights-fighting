from copy import deepcopy

from app.knight.knight import Knight
from app.fight.fight import fight


def battle(knights_config: dict) -> dict:
    config = deepcopy(knights_config)

    lancelot = Knight(config["lancelot"])
    mordred = Knight(config["mordred"])
    arthur = Knight(config["arthur"])
    red_knight = Knight(config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
