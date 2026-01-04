from typing import Dict, Any

from app.battle.knight import Knight


def battle(config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    knights = {}
    for knight_name, knight_attributes in config.items():
        knights[knight_name] = Knight(
            name=knight_attributes["name"],
            power=knight_attributes["power"],
            hp=knight_attributes["hp"],
            armour=knight_attributes.get("armour", []),
            weapon=knight_attributes["weapon"],
            potion=knight_attributes.get("potion", None)
        )

    battle_results = {}

    battle_results.update(Knight.battle(
        knights["lancelot"],
        knights["mordred"]
    ))

    battle_results.update(Knight.battle(
        knights["arthur"],
        knights["red_knight"]
    ))

    return battle_results
