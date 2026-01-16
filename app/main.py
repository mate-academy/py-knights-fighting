from app.knights.knight import Knight
from app.battle.battle import perform_battle
from app.knights_info.knights_info import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights_objects = {
        name: Knight(**knight)
        for name, knight in knights_config.items()
    }

    return {
        **perform_battle(knights_objects["lancelot"],
                         knights_objects["mordred"]),
        **perform_battle(knights_objects["arthur"],
                         knights_objects["red_knight"]),
    }


print(battle(KNIGHTS))
