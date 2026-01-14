from app.models.knight import Knight
from app.services.battle import duel


def battle(knights_config: dict) -> dict:
    # Create all knights dynamically
    knights = {
        key: Knight.from_config(config)
        for key, config in knights_config.items()
    }

    # Prepare all knights for battle
    for knight in knights.values():
        knight.prepare_for_battle()

    # Fixed battle pairs (as required by task)
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    # Build result dynamically
    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
