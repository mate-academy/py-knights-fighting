from app.knights.KNIGHTS import KNIGHTS
from app.knights.knight import Knight


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
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
