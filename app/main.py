from __future__ import annotations
from app.knights.knights_data import KNIGHTS


def battle(knightsсonfig: dict) -> battle:
    lancelot = knightsсonfig["lancelot"]
    apply_effects(lancelot)
    arthur = knightsсonfig["arthur"]
    apply_effects(arthur)
    mordred = knightsсonfig["mordred"]
    apply_effects(mordred)
    red_knight = knightsсonfig["red_knight"]

    apply_effects(red_knight)
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


def apply_effects(knight: dict) -> None:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]
        for key in potion_effect:
            if key in knight:
                knight[key] += potion_effect[key]


print(battle(KNIGHTS))
