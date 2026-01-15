import copy
from typing import Dict, Any

from app.apply_potion import apply_potion_if_exists


def lancelot(knights_config: Dict[str, Any]) -> Dict[str, Any]:
    lancelot_copy = copy.deepcopy(knights_config["lancelot"])

    lancelot_copy["protection"] = 0
    for _ in lancelot_copy["armour"]:
        lancelot_copy["protection"] += _["protection"]

    lancelot_copy["power"] += lancelot_copy["weapon"]["power"]

    apply_potion_if_exists(lancelot_copy)
    return lancelot_copy
