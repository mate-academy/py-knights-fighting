from app.equipment import knights_parameters, battle_knight
from app.knight_stats import KNIGHTS
from typing import Dict, Any


def battle(knights_config: Dict[Dict, Any]) -> dict:
    # Подготовка к бою:
    # lancelot
    lancelot = knights_config["lancelot"]

    knights_parameters(lancelot)

    # arthur
    arthur = knights_config["arthur"]

    knights_parameters(arthur)

    # mordred
    mordred = knights_config["mordred"]

    knights_parameters(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]

    knights_parameters(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle_knight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    battle_knight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
