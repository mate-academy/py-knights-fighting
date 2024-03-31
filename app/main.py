from app.knight import KNIGHTS
from app.knight_class import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights_config["lancelot"])

    # arthur
    arthur = Knight(knights_config["arthur"])

    # mordred
    mordred = Knight(knights_config["mordred"])

    # red_knight
    red_knight = Knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)
    mordred.fight(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)
    red_knight.fight(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.check_hp(),
        arthur.name: arthur.check_hp(),
        mordred.name: mordred.check_hp(),
        red_knight.name: red_knight.check_hp(),
    }


print(battle(KNIGHTS))
