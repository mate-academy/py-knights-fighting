from app.knight_tournament.preparing import create_knights_list
from app.knight_tournament.preparing import invite_knights_for_battle
from app.knight_tournament.tournament import combat
from app.knights.__init__ import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = invite_knights_for_battle(
        create_knights_list(knights_config)
    )

    battle_results = {}

    for i in range(len(knights) // 2):
        battle_results.update(
            combat(knights[i], knights[i + 2])
        )

    return battle_results


print(battle(KNIGHTS))
