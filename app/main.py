from app.knight import KNIGHTS
from app.knight_class import Knight


def battle(knights_config: dict) -> dict:

    lancelot = Knight(knights_config["lancelot"])

    arthur = Knight(knights_config["arthur"])

    mordred = Knight(knights_config["mordred"])

    red_knight = Knight(knights_config["red_knight"])

    lancelot.fight(mordred)
    mordred.fight(lancelot)

    arthur.fight(red_knight)
    red_knight.fight(arthur)

    return {
        lancelot.name: lancelot.check_hp(),
        arthur.name: arthur.check_hp(),
        mordred.name: mordred.check_hp(),
        red_knight.name: red_knight.check_hp(),
    }


print(battle(KNIGHTS))
