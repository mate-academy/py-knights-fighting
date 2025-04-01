import copy
from typing import Dict, Any

from app.apply_potion import apply_potion_if_exists


def mordred(knights_config: Dict[str, Any]) -> Dict[str, Any]:
    mordred_copy = copy.deepcopy(knights_config["mordred"])

    mordred_copy["protection"] = 0
    for _ in mordred_copy["armour"]:
        mordred_copy["protection"] += _["protection"]

    mordred_copy["power"] += mordred_copy["weapon"]["power"]

    apply_potion_if_exists(mordred_copy)
    return mordred_copy
