from app.knights.preparation import Knight
from app.knights.battle import pvp


def battle(knights_config):

    lancelot = Knight.create_knight(knights_config["lancelot"])
    arthur = Knight.create_knight(knights_config["arthur"])
    mordred = Knight.create_knight(knights_config["mordred"])
    red_knight = Knight.create_knight(knights_config["red_knight"])

    pvp(lancelot, mordred)
    pvp(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
