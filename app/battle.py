from typing import Dict
from app.knights import Knight


def battle(knights_config: Dict[str, Dict[str, any]]) -> Dict[str, int]:
    # Create knights
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    # Prepare knights for battle
    lancelot.prepare_for_battle()
    arthur.prepare_for_battle()
    mordred.prepare_for_battle()
    red_knight.prepare_for_battle()

    # Battle: Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # Battle: Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Return battle results
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
