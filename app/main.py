from typing import Dict, Any
from app.knights.battle import Battle


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    return Battle.fight(knights_config)
