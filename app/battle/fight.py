from copy import deepcopy

from app.models.knights import prepare_knight
from app.utils.stats import clamp


def calculate_damage(attacker: dict, defender: dict) -> int:
    damage = attacker["power"] - defender["protection"]

    return clamp(damage)


def attack(attacker: dict, defender: dict) -> None:
    damage = calculate_damage(attacker, defender)

    defender["hp"] -= damage

    defender["hp"] = clamp(defender["hp"])


def duel(knight1: dict, knight2: dict) -> None:
    attack(knight1, knight2)
    attack(knight2, knight1)


def prepare_all_knights(knights: dict) -> None:
    for knight in knights.values():
        prepare_knight(knight)


def get_results(knights: dict) -> dict:
    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }


def battle(knights_config: dict) -> dict:
    knights = deepcopy(knights_config)

    prepare_all_knights(knights)

    duel(
        knights["lancelot"],
        knights["mordred"]
    )

    duel(
        knights["arthur"],
        knights["red_knight"]
    )

    return get_results(knights)
