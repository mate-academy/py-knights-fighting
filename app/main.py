from app.battle import Battle
from app.config import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = Knight("lancelot", knights_config).knight
    # arthur
    arthur = Knight("arthur", knights_config).knight
    # mordred
    mordred = Knight("mordred", knights_config).knight
    # red_knight
    red_knight = Knight("red_knight", knights_config).knight

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    result_battle_1 = Battle(lancelot, mordred).run_battle()
    # 2 Arthur vs Red Knight:
    result_battle_2 = Battle(arthur, red_knight).run_battle()

    # Return battle results:
    return {
        result_battle_1[0]["name"]: result_battle_1[0]["hp"],
        result_battle_2[0]["name"]: result_battle_2[0]["hp"],
        result_battle_1[1]["name"]: result_battle_1[1]["hp"],
        result_battle_2[1]["name"]: result_battle_2[1]["hp"],
    }


print(battle(KNIGHTS))
