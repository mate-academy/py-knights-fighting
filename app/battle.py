from typing import Dict, Any

from app.battle_round import battle_round
from app.participants import KNIGHTS
from app.preparations import prepare_knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:

    # BATTLE PREPARATIONS:
    lancelot = knights_config["lancelot"]
    prepare_knight(lancelot)

    arthur = knights_config["arthur"]
    prepare_knight(arthur)

    mordred = knights_config["mordred"]
    prepare_knight(mordred)

    red_knight = knights_config["red_knight"]
    prepare_knight(red_knight)

    battle_round(lancelot, mordred)
    battle_round(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
