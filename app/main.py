from typing import Dict, Any

from app.models.knight import Knight
from app.services.battle_service import battle_between


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    required_keys = {"lancelot", "mordred", "arthur", "red_knight"}
    missing = required_keys - knights_config.keys()
    if missing:
        raise ValueError(f"Missing knights in config: {missing}")

    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    result_1 = battle_between(lancelot, mordred)
    result_2 = battle_between(arthur, red_knight)

    return {
        **result_1,
        **result_2,
    }
