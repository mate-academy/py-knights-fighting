from typing import Dict

from app.combat.duel import duel
from app.application.factory import create_knight


def battle(config: dict) -> Dict[str, int]:
    """
    Orchestrates the entire battle.
    Creates warriors, initiates duels, aggregates and returns the result.
    """

    lancelot = create_knight(config["lancelot"])
    arthur = create_knight(config["arthur"])
    mordred = create_knight(config["mordred"])
    red_knight = create_knight(config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:
    duel(lancelot, mordred)
    duel(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
