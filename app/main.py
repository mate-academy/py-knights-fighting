from __future__ import annotations

from app.Fights.Fight_1 import fight_1
from app.Knights.Knights import KnightBasic
from app.Knights.Knights_list import KNIGHTS, championship_knights_dict


def battle(tournament_dict: dict) -> dict:

    # Create a dict to return
    dict_of_results = {knight.name: knight.hp for knight in tournament_dict.values()}

    # BATTLE PREPARATIONS:

    # Assign knights instances to variable
    lancelot = tournament_dict.get("Lancelot")
    artur = tournament_dict.get("Arthur")
    mordred = tournament_dict.get("Mordred")
    red_knight = tournament_dict.get("Red Knight")

    # Use this method to prepare knights to battle
    for knight in tournament_dict.values():
        knight.battle_preparing()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight_1(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight_1(artur, red_knight)

    # Return battle results:
    return dict_of_results


print(battle(championship_knights_dict))
