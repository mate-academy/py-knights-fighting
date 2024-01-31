from typing import Dict, Any


def calculate_stats(knight: Dict[str, Any]) -> Dict[str, Any]:
    stats = knight.copy()
    stats["protection"] = (
        sum(armor["protection"]for armor in knight["armour"])
    )
    stats["power"] += knight["weapon"]["power"]
    potion = knight.get("potion")
    if potion:
        potion_effect = potion.get("effect", {})
        stats["power"] += potion_effect.get("power", 0)
        stats["protection"] += potion_effect.get("protection", 0)
        stats["hp"] += potion_effect.get("hp", 0)
    return stats


def battle(knights_config: Dict[str, Any]) -> Dict[str, Any]:
    lancelot = calculate_stats(knights_config["lancelot"])
    arthur = calculate_stats(knights_config["arthur"])
    mordred = calculate_stats(knights_config["mordred"])
    red_knight = calculate_stats(knights_config["red_knight"])

    # Battle between Lancelot and Mordred
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    lancelot["hp"] = max(lancelot["hp"], 0)
    mordred["hp"] = max(mordred["hp"], 0)

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]
    arthur["hp"] = max(arthur["hp"], 0)
    red_knight["hp"] = max(red_knight["hp"], 0)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
