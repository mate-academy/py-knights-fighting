from __future__ import annotations

from app.Knights.Knights import KnightBasic
from app.Fights.Fight_1 import fight_1
from app.Knights.Knights_list import KNIGHTS


def battle(tournament_dict: dict) -> dict:

    # Assign knights instances to variable
    lancelot = KnightBasic(tournament_dict.get("lancelot"))
    artur = KnightBasic(tournament_dict.get("arthur"))
    mordred = KnightBasic(tournament_dict.get("mordred"))
    red_knight = KnightBasic(tournament_dict.get("red_knight"))

    # First fight Lancelot vs Mordred:
    fight_1(lancelot, mordred)

    # Second fight Arthur vs Red Knight:
    fight_1(artur, red_knight)

    # Return battle results:
    return {lancelot.name: lancelot.hp,
            artur.name: artur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp}


print(battle(KNIGHTS))
