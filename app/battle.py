from typing import Dict, Any
from app.knight import Knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # Battle: Lancelot vs Mordred
    lancelot.hp -= max(0, mordred.power - lancelot.armour.protection)
    mordred.hp -= max(0, lancelot.power - mordred.armour.protection)

    if lancelot.hp <= 0:
        lancelot.hp = 0
    if mordred.hp <= 0:
        mordred.hp = 0

    # Battle: Arthur vs Red Knight
    arthur.hp -= max(0, red_knight.power - arthur.armour.protection)
    red_knight.hp -= max(0, arthur.power - red_knight.armour.protection)

    if arthur.hp <= 0:
        arthur.hp = 0
    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
