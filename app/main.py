from typing import Optional, Dict
from app.services.battle import fight
from app.data.knights_config import KNIGHTS


def battle(knights: Optional[Dict] = None) -> Dict[str, int]:
    if knights is None:
        knights = KNIGHTS

    lm = fight(knights["lancelot"], knights["mordred"])
    ar = fight(knights["arthur"], knights["red_knight"])

    return {
        "Lancelot": lm["first"],
        "Mordred": lm["second"],
        "Arthur": ar["first"],
        "Red Knight": ar["second"],
    }
