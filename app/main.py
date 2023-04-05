from app.battle_preparations import get_equipment
from app.battle import fight
from app.knights_characteristics import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    get_equipment(lancelot)
    arthur = knights_config["arthur"]
    get_equipment(arthur)
    mordred = knights_config["mordred"]
    get_equipment(mordred)
    red_knight = knights_config["red_knight"]
    get_equipment(red_knight)
    fight(lancelot, mordred)
    fight(arthur, red_knight)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
    print(battle(KNIGHTS))
