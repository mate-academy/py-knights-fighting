from app.config.knights import KNIGHTS
from app.classes.knight import Knight
from app.classes.battleMethods import fight, results


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knightsconfig["lancelot"])
    lancelot.full_equip()

    # arthur
    arthur = Knight(knightsconfig["arthur"])
    arthur.full_equip()

    # mordred
    mordred = Knight(knightsconfig["mordred"])
    mordred.full_equip()

    # red_knight
    red_knight = Knight(knightsconfig["red_knight"])
    red_knight.full_equip()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return results(lancelot, arthur, mordred, red_knight)


print(battle(KNIGHTS))
