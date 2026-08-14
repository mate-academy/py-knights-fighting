from app.battle import Battle
from app.knight import Knight


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.get_knight(knights, "lancelot")
    lancelot.get_ready_for_fight()
    # arthur
    arthur = Knight.get_knight(knights, "arthur")
    arthur.get_ready_for_fight()

    # mordred
    mordred = Knight.get_knight(knights, "mordred")
    mordred.get_ready_for_fight()

    # red_knight
    red_knight = Knight.get_knight(knights, "red_knight")
    red_knight.get_ready_for_fight()

    # -------------------------------------------------------------------------------
    # BATTLE:
    epic_battle = Battle()

    # 1 Lancelot vs Mordred:
    epic_battle.hold_duel(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    epic_battle.hold_duel(arthur, red_knight)

    # Return battle results:
    return epic_battle.get_battle_results()
