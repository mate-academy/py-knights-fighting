from __future__ import annotations
from typing import Dict, Any


class Battle:
    """The class can store battle data if needed."""
    def __init__(self, lancelot: str, mordred: str) -> None:
        self.lancelot = lancelot
        self.mordred = mordred


def apply_items(knight: Dict[str, Any]) -> None:
    """
    We add up the knight's armor, weapons, and potions.
We write the resulting stats back into the dictionary.
    """
    knight["protection"] = sum(
        item["protection"] for item in knight.get("armour", [])
    )
    knight["power"] += knight["weapon"]["power"]

    potion = knight.get("potion")
    if potion and "effect" in potion:
        effect = potion["effect"]
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)
        knight["hp"] += effect.get("hp", 0)


def duel(first_knight: Dict[str, Any], second_knight: Dict[str, Any]) -> None:
    """
    A battle between two knights.
Damage = enemy's power – your defense (not less than zero).
    """
    first_knight["hp"] -= (
        max(0, second_knight["power"] - first_knight["protection"]))
    second_knight["hp"] -= (
        max(0, first_knight["power"] - second_knight["protection"]))

    first_knight["hp"] = max(first_knight["hp"], 0)
    second_knight["hp"] = max(second_knight["hp"], 0)


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """
    The main function of combat.
Accepts knights' configurations and restores their remaining health.
    """
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    for current_knight in (lancelot, arthur, mordred, red_knight):
        apply_items(current_knight)

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
