from app.config.knights import KNIGHTS
from app.classes.knight import Knight
from app.classes.battleMethods import fight, get_results


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    lancelot.full_equip()

    arthur = Knight(knights_config["arthur"])
    arthur.full_equip()

    mordred = Knight(knights_config["mordred"])
    mordred.full_equip()

    red_knight = Knight(knights_config["red_knight"])
    red_knight.full_equip()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return get_results(lancelot, arthur, mordred, red_knight)


print(battle(KNIGHTS))
