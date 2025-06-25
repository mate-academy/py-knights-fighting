from app.tools.tools import (
    knights_from_dict,
    prepare_all_to_fights
)
from app.people.knight import Knight


def battle(knights_config: dict[str, dict]) -> dict:
    # BATTLE PREPARATIONS:
    knights = knights_from_dict(knights_config)
    prepare_all_to_fights(knights)

    lancelot: Knight = knights.get("lancelot", None)
    mordred: Knight = knights.get("mordred", None)

    arthur: Knight = knights.get("arthur", None)
    red_knight: Knight = knights.get("red_knight", None)

    # BATTLE:
    Knight.battle(lancelot, mordred)
    Knight.battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
