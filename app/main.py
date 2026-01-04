from app.competitors import KNIGHTS
from app.knight import Knight
from app.battle import Battle


def battle(knightsconfig: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knightsconfig["lancelot"])

    # arthur
    arthur = Knight(knightsconfig["arthur"])

    # mordred
    mordred = Knight(knightsconfig["mordred"])

    # red_knight
    red_knight = Knight(knightsconfig["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot_mordred = Battle(lancelot, mordred)
    lancelot_mordred.battle()

    # 2 Arthur vs Red Knight:
    arthur_red_knight = Battle(arthur, red_knight)
    arthur_red_knight.battle()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
