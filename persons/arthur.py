import copy
from typing import Any, Dict


from app.apply_potion import apply_potion_if_exists


def arthur(knights_config: Dict[str, Any]) -> Dict[str, Any]:
    arthur_copy = copy.deepcopy(knights_config["arthur"])

    arthur_copy["protection"] = 0
    for _ in arthur_copy["armour"]:
        arthur_copy["protection"] += _["protection"]

    arthur_copy["power"] += arthur_copy["weapon"]["power"]

    apply_potion_if_exists(arthur_copy)
    return arthur_copy
