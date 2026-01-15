from app.battle import kombat
from app.knights_processing.knights_gearing import gearing
from app.knights_processing.knights_making import Knight


def battle(knights_data: dict) -> dict:

    lancelot = Knight.make_knight(knights_data["lancelot"])
    arthur = Knight.make_knight(knights_data["arthur"])
    mordred = Knight.make_knight(knights_data["mordred"])
    red_knight = Knight.make_knight(knights_data["red_knight"])

    gearing(lancelot)
    gearing(arthur)
    gearing(mordred)
    gearing(red_knight)

    kombat(lancelot, mordred)
    kombat(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
