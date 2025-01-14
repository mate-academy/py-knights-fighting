from typing import Dict
from app.knights import Knight


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    """
    Simulate a battle between knights based on their stats.

    :param knights_config: Configuration dictionary of all knights.
    :return: A dictionary with the names and
    final HP of all knights after the battle.
    """
    # Initialize knights
    knights: Dict[str, Knight] = {}
    for key, config in knights_config.items():
        knight = Knight(
            name=config["name"],
            base_power=config["power"],
            base_hp=config["hp"],
            armour=config.get("armour", []),
            weapon=config.get("weapon"),
            potion=config.get("potion"),
        )
        knight.prepare_for_battle()
        knights[key] = knight

    # Simulate battles
    lancelot: Knight = knights["lancelot"]
    mordred: Knight = knights["mordred"]
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur: Knight = knights["arthur"]
    red_knight: Knight = knights["red_knight"]
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Return battle results
    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
