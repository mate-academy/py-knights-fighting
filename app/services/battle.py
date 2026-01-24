from typing import Dict
from app.services.stats import prepare_knight


def fight(first_config: Dict, second_config: Dict) -> Dict[str, int]:
    first = prepare_knight(first_config)
    second = prepare_knight(second_config)

    first_hp = first["hp"] - (second["power"] - first["protection"])
    second_hp = second["hp"] - (first["power"] - second["protection"])

    return {
        "first": max(0, first_hp),
        "second": max(0, second_hp),
    }
