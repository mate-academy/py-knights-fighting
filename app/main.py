from typing import Dict

from app.knights.knights import KNIGHTS
from app.battle.battle_logic import Battle
from app.inventory.apply_inventory import Inventory


def battle(knights_config: Dict[str, dict]) -> dict:

    lancelot = knights_config["lancelot"]
    Inventory.inventory_application([lancelot])

    arthur = knights_config["arthur"]
    Inventory.inventory_application([arthur])

    mordred = knights_config["mordred"]
    Inventory.inventory_application([mordred])

    red_knight = knights_config["red_knight"]
    Inventory.inventory_application([red_knight])

    Battle.battle(lancelot, mordred)

    Battle.battle(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
