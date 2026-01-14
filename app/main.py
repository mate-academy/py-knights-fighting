from app.models.knight import Knight
from app.services.battle import duel


def battle(knights_config: dict) -> dict:
    lancelot = Knight.from_config(knights_config["lancelot"])
    arthur = Knight.from_config(knights_config["arthur"])
    mordred = Knight.from_config(knights_config["mordred"])
    red_knight = Knight.from_config(knights_config["red_knight"])

    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        knight.prepare_for_battle()

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
