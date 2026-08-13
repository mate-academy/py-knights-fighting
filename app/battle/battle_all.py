from typing import Any


def battle_all_knights(lancelot: dict[str, Any],
                       mordred: dict,
                       arthur: dict,
                       red_knight: dict
                       ) -> None:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0
    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0
    if mordred["hp"] <= 0:
        mordred["hp"] = 0
