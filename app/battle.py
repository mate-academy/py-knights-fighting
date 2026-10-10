from copy import deepcopy
from app.config import BATTLE_PAIRS
from app.knights import prepare_knight


def fight(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= (
        second_knight["power"] - first_knight["protection"]
    )
    second_knight["hp"] -= (
        first_knight["power"] - second_knight["protection"]
    )

    first_knight["hp"] = max(0, first_knight["hp"])
    second_knight["hp"] = max(0, second_knight["hp"])


def battle(knights_config: dict) -> dict:
    knights = deepcopy(knights_config)

    for knight in knights.values():
        prepare_knight(knight)

    for first_key, second_key in BATTLE_PAIRS:
        fight(knights[first_key], knights[second_key])

    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }
