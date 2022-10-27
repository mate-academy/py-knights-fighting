from app.knights.knight import Knight
from app.fighting.fight import Fight
from tests.default_config import fights_config


def battle(knights_config: dict) -> dict:
    lancelot = Knight.pars(knights_config["lancelot"])
    arthur = Knight.pars(knights_config["arthur"])
    mordred = Knight.pars(knights_config["mordred"])
    red_knight = Knight.pars(knights_config["red_knight"])

    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.activate_items()

    Fight.fight(lancelot, mordred)
    Fight.fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(fights_config))
