from app.data.knights import KNIGHTS
from app.fighters.knight import Knight


def battle(knights_config):
    # BATTLE PREPARATIONS:

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
