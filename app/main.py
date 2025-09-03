from typing import Dict, Any

from app.models.knight import Knight
from app.services.battle_service import battle_between


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    # ✅ Validate required knights are present
    required_keys = {"lancelot", "mordred", "arthur", "red_knight"}
    missing = required_keys - knights_config.keys()
    if missing:
        raise ValueError(f"Missing knights in config: {missing}")

    # ✅ DRY: Create knights dynamically
    knights = {key: Knight(config) for key, config in knights_config.items()}

    # ✅ DRY: Define battle pairs and compute results
    battle_pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
    results: Dict[str, int] = {}
    for k1, k2 in battle_pairs:
        results.update(battle_between(knights[k1], knights[k2]))

    return results
