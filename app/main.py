from app.models import Knight
from app.engine import duel


def battle(knights_config: dict) -> dict:
    """
    Refactored battle function that preserves the original API.
    """
    # 1. Create Knight objects (Preparation is automatic in __init__)
    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    # 2. Execute fixed tournament pairings
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    # 3. Return results in the expected format
    return {k.name: k.hp for k in knights.values()}
