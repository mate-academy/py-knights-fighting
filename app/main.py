from typing import Dict
from .config import KNIGHTS
from .entities import Armour, Weapon, Potion, Knight


def battle(knights: Dict[str, Knight]) -> Dict[str, int]:
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    # Apply potion effects before battle
    for knight in knights.values():
        knight.apply_potion_effects()

    # Lancelot vs Mordred
    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    # Arthur vs Red Knight
    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    # Return battle results
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
