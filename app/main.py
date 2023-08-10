from app.championship.battles import Battle
from app.championship.knights import Knight
from app.championship.battle_results import results


def battle(knights_config: dict) -> None:
    # Create fighters:
    for stat in knights_config.values():
        Knight.add_knights(stat)

    # Battles:
    Battle.duel("Lancelot", "Mordred")
    Battle.duel("Arthur", "Red Knight")

    # Return battle results:
    return results(Knight.knights)
