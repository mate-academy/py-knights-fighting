from typing import Any

from app.battle.battle_action import Battle
from app.parametrs import KNIGHTS


def battle(knights_config: dict) -> dict[Any, Any]:

    # BATTLE:

    # 1 Lancelot vs Mordred:
    knight_1 = "Lancelot"
    knight_2 = "Mordred"
    knight_1, knight_2 = Battle.medieval_battle(
        knight_1, knight_2, knights_config
    )

    # # 2 Arthur vs Red Knight:
    knight_3 = "Arthur"
    knight_4 = "Red Knight"
    knight_3, knight_4 = Battle.medieval_battle(
        knight_3, knight_4, knights_config
    )

    # Return battle results:
    return {
        knight_1.name: knight_1.hp,
        knight_2.name: knight_2.hp,
        knight_3.name: knight_3.hp,
        knight_4.name: knight_4.hp
    }


print(battle(KNIGHTS))
