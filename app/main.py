from app.knight import Knight
from app.battle import Battle
from app.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    knights = []
    for knight in knights_config:
        knights.append(Knight(**knights_config[knight]))

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle.battle(knights[0], knights[2])
    # 2 Arthur vs Red Knight:
    Battle.battle(knights[1], knights[3])
    # Return battle results:
    return Battle.tournament_result(knights)


battle(KNIGHTS)
