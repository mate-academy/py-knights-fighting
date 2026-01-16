from typing import Dict, Any
from knight import Knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    # Initialize Knight instances
    knights = {k: Knight(k, **v) for k, v in knights_config.items()}

    # Apply effects for each knight
    for knight in knights.values():
        knight.apply_effects()

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot, mordred = knights["lancelot"], knights["mordred"]
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur, red_knight = knights["arthur"], knights["red_knight"]
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        knight.name: knight.hp for knight in knights.values()
    }
