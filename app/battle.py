from typing import Dict, Any
from app.prepare import prepare_knight_stats


def fight(knight1: Dict[str, Any], knight2: Dict[str, Any]) -> None:
    damage_to_knight1 = max(0, knight2["power"] - knight1["protection"])
    damage_to_knight2 = max(0, knight1["power"] - knight2["protection"])
    knight1["hp"] = max(0, knight1["hp"] - damage_to_knight1)
    knight2["hp"] = max(0, knight2["hp"] - damage_to_knight2)


def battle(knights_config: dict) -> dict:
    lancelot = prepare_knight_stats(knights_config["lancelot"])
    arthur = prepare_knight_stats(knights_config["arthur"])
    mordred = prepare_knight_stats(knights_config["mordred"])
    red_knight = prepare_knight_stats(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
