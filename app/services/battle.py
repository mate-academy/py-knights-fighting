from typing import Dict

from app.services.stats import prepare_knight


def fight(first_config: Dict, second_config: Dict) -> Dict[str, int]:
    first = prepare_knight(first_config)
    second = prepare_knight(second_config)

    first_hp = first["hp"] - (second["power"] - first["protection"])
    second_hp = second["hp"] - (first["power"] - second["protection"])

    if first_hp <= 0:
        first_hp = 0
    if second_hp <= 0:
        second_hp = 0

    return {
        "first": first_hp,
        "second": second_hp,
    }
