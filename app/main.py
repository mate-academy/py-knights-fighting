from typing import Dict
from app.config import KNIGHTS
from app.models import Knight


def battle(knights_config: dict) -> Dict[str, int]:
    lancelot: Knight = Knight(knights_config["lancelot"])
    mordred: Knight = Knight(knights_config["mordred"])
    arthur: Knight = Knight(knights_config["arthur"])
    red_knight: Knight = Knight(knights_config["red_knight"])

    for knight in (lancelot, mordred, arthur, red_knight):
        knight.apply_gear()

    lancelot.attack(mordred)
    mordred.attack(lancelot)

    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
