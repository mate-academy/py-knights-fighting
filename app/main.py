from typing import Any

from app.battle.battle_action import Battle


def battle(knight_stats: dict) -> dict[Any, Any]:

    # BATTLE:

    # 1 Lancelot vs Mordred:
    knight1 = "Lancelot"
    knight2 = "Mordred"
    knight1, knight2 = Battle.battle(knight1, knight2, knight_stats)

    # 2 Arthur vs Red Knight:
    knight3 = "Arthur"
    knight4 = "Red Knight"
    knight3, knight4 = Battle.battle(knight3, knight4, knight_stats)

    # Return battle results:
    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
        knight3.name: knight3.hp,
        knight4.name: knight4.hp
    }
