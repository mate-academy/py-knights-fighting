from __future__ import annotations
from app.models.knight import Knight


def prepare_knights(knight_stats: dict) -> dict:
    """
    Prepares the knights for battle by applying their armour,
        weapon, and potion effects.
    Args:
        knight_stats (dict): A dictionary containing the stats of the knights.
    Returns:
        dict: A dictionary containing the prepared stats of the knights.
    """
    knights = {name: Knight(**knight_stats[name]) for name in knight_stats}
    for knight in knights.values():
        knight.prepare()

    return knights


def battle(knight_stats: dict) -> dict:
    """
    Simulates a battle between the knights based on their stats.
    Args:
        knight_stats (dict): A dictionary containing the prepared
            stats of the knights.
    Returns:
        dict: A dictionary containing the remaining hp of each
            knight after the battle.
    """
    knights = prepare_knights(knight_stats)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    # 1 Lancelot vs Mordred:
    lancelot.receive_attack(attacker=mordred)
    mordred.receive_attack(attacker=lancelot)

    # 2 Arthur vs Red Knight:
    arthur.receive_attack(attacker=red_knight)
    red_knight.receive_attack(attacker=arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
