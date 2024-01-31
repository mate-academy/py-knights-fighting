from typing import Dict, Any


def battle_preparation(knight: Dict[str, Any]) -> Dict[str, Any]:
    knight_stats = knight.copy()
    knight_stats["protection"] = (
        sum(armor["protection"]for armor in knight["armour"])
    )
    knight_stats["power"] += knight["weapon"]["power"]
    potion = knight.get("potion")
    if potion:
        potion_effect = potion.get("effect", {})
        knight_stats["power"] += potion_effect.get("power", 0)
        knight_stats["protection"] += potion_effect.get("protection", 0)
        knight_stats["hp"] += potion_effect.get("hp", 0)
    return knight_stats


def battle(knights_config: Dict[str, Any]) -> Dict[str, Any]:
    lancelot = battle_preparation(knights_config["lancelot"])
    arthur = battle_preparation(knights_config["arthur"])
    mordred = battle_preparation(knights_config["mordred"])
    red_knight = battle_preparation(knights_config["red_knight"])

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
