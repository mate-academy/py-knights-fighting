"""Arena battle logic: duel between two knights and championship."""

import copy

from app.knight import prepare_knight_for_battle

BATTLE_PAIRS = [
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
]


def duel(first_knight: dict, second_knight: dict) -> None:
    """
    Run a duel between two prepared knights. Updates hp in place.
    Defeated knight has hp set to 0.
    """
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    for knight in (first_knight, second_knight):
        if knight["hp"] <= 0:
            knight["hp"] = 0


def battle(knights_config: dict) -> dict:
    """
    Run championship: Lancelot vs Mordred, Arthur vs Red Knight.
    Returns dict mapping knight name to remaining hp. Does not mutate input.
    """
    config = copy.deepcopy(knights_config)

    for knight_key in config:
        prepare_knight_for_battle(config[knight_key])

    for first_key, second_key in BATTLE_PAIRS:
        duel(config[first_key], config[second_key])

    return {knight["name"]: knight["hp"] for knight in config.values()}
