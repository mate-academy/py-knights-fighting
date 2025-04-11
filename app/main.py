from typing import Dict
from app.battle_system.entities.knight import Knight


def battle(knights_config: Dict) -> Dict[str, int]:
    """
    Simulate battles between knights and return their remaining HP.

    Args:
        knights_config: Dictionary containing knights configuration

    Returns:
        Dictionary with knights' names as keys and their remaining HP as values
    """
    # Create knight instances
    lancelot = Knight.from_config(knights_config["lancelot"])
    mordred = Knight.from_config(knights_config["mordred"])
    arthur = Knight.from_config(knights_config["arthur"])
    red_knight = Knight.from_config(knights_config["red_knight"])

    # Battle 1: Lancelot vs Mordred
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # Battle 2: Arthur vs Red Knight
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
