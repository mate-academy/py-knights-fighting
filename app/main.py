from app.statistics.knights import Tournament
from app.data.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    stat = [Tournament(g) for g in knights_config.values()]
    # apply armour

    for value in stat:
        value.configurations()

    # -------------------------------------------------------------------------------
    # BATTLE:
    pars = [(0, 2), (1, 3)]
    for kin1, kin2 in pars:
        stat[kin1].battle(stat[kin2].king)

    # Return battle results:
    return {
        stat[i].king["name"]: stat[i].king["hp"] for i in range(len(stat))
    }


print(battle(KNIGHTS))
