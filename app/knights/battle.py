from typing import Dict
from app.knights.knight import Knight


def duel(knight1: Knight, knight2: Knight):
    """
    Simulates a simultaneous exchange of attacks between two knights.
    Each knight receives damage equal to the other's power, reduced by their own protection.

    Args:
        knight1 (Knight): The first knight.
        knight2 (Knight): The second knight.
    """
    knight1.receive_damage(knight2.power)
    knight2.receive_damage(knight1.power)


def battle_all(knights: Dict[str, Knight]) -> Dict[str, int]:
    """
    Conducts two independent duels:
      1) 'lancelot' vs. 'mordred'
      2) 'arthur'   vs. 'red_knight'

    Args:
        knights (Dict[str, Knight]): A dictionary mapping keys
            ("lancelot", "arthur", "mordred", "red_knight") to Knight instances.

    Returns:
        Dict[str, int]: A mapping from each knight's display name to
                        their remaining HP after the fights.
    """
    # Duel #1: Lancelot vs Mordred
    duel(knights["lancelot"], knights["mordred"])

    # Duel #2: Arthur vs Red Knight
    duel(knights["arthur"], knights["red_knight"])

    return {
        knights["lancelot"].name: knights["lancelot"].current_hp,
        knights["arthur"].name: knights["arthur"].current_hp,
        knights["mordred"].name: knights["mordred"].current_hp,
        knights["red_knight"].name: knights["red_knight"].current_hp,
    }
