from app.knights.actions import apply_armour, apply_weapon, apply_potion
from app.battle.config import config_duel


def battle(knights_config: dict) -> dict:

    for knight in knights_config.values():
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    config_duel(lancelot, mordred)
    config_duel(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
