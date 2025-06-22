from copy import deepcopy
from app.knight import Knight


def fight(k1: Knight, k2: Knight) -> None:
    k1.take_damage(k2.power)
    k2.take_damage(k1.power)


def battle(knights_config: dict) -> dict:
    config = deepcopy(knights_config)

    lancelot = Knight(config["lancelot"])
    arthur = Knight(config["arthur"])
    mordred = Knight(config["mordred"])
    red_knight = Knight(config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
