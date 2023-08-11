from app.championship.battle_functions import duel, results
from app.championship.knights import Knight


def battle(knights_config: dict) -> dict:
    # Create fighters:
    for stat in knights_config.values():
        Knight.add_knight(stat)

    # Battles:
    duel("Lancelot", "Mordred")
    duel("Arthur", "Red Knight")

    # Return battle results:
    return results(Knight.knights)
