import copy
from typing import Dict, Any

from app.apply_potion import apply_potion_if_exists


def red_knight(knights_config: Dict[str, Any]) -> Dict[str, Any]:
    red_knight_copy = copy.deepcopy(knights_config["red_knight"])
    red_knight_copy["protection"] = 0

    for _ in red_knight_copy["armour"]:
        red_knight_copy["protection"] += _["protection"]

    red_knight_copy["power"] += red_knight_copy["weapon"]["power"]

    apply_potion_if_exists(red_knight_copy)
    return red_knight_copy
