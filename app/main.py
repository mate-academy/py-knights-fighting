from app.statistics.knights import Tournament
from app.data.data import KNIGHTS

stat = Tournament(KNIGHTS)

def battle(knightsConfig):
    # BATTLE PREPARATIONS:
    # apply armour
    for value in knightsConfig.values():
        stat.configurations(value)

    # lancelot
    lancelot = knightsConfig["lancelot"]

    # arthur
    arthur = knightsConfig["arthur"]

    # mordred
    mordred = knightsConfig["mordred"]

    # red_knight
    red_knight = knightsConfig["red_knight"]


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


print(battle(KNIGHTS))
