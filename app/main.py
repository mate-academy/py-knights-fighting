from __future__ import annotations

from app.Fights.Fight_1 import fight_1
from app.Knights.Knights_list import championship_knights_dict


def battle(tournament_dict: dict) -> dict:

    # Assign knights instances to variable
    lancelot = tournament_dict.get("Lancelot")
    artur = tournament_dict.get("Arthur")
    mordred = tournament_dict.get("Mordred")
    red_knight = tournament_dict.get("Red Knight")

    # First fight Lancelot vs Mordred:
    fight_1(lancelot, mordred)

    # Second fight Arthur vs Red Knight:
    fight_1(artur, red_knight)

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in tournament_dict.values()
    }


print(battle(championship_knights_dict))
