from app.knights.config import KNIGHTS
from app.knights.knight import Knight


def battle(knights_config: dict = KNIGHTS) -> dict:
    # Instantiates knights, runs pre-defined battles,
    # and returns final HP results.
    # Defaults to the central KNIGHTS config if no dict is provided.

    knights = {
        name: Knight(config)
        for name, config in knights_config.items()
    }

    # Battles: Lancelot vs Mordred, Arthur vs Red Knight
    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
