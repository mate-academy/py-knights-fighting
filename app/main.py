from app.statistics.knights import Tournament
from app.data.data import KNIGHTS

stat = Tournament(KNIGHTS)


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # apply armour

    for value in knights_config.values():
        stat.configurations(value)

    # lancelot
    lancelot = knights_config["lancelot"]

    # arthur
    arthur = knights_config["arthur"]

    # mordred
    mordred = knights_config["mordred"]

    # red_knight
    red_knight = knights_config["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    stat.battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    stat.battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
