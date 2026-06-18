from typing import Dict

from app.knight import Knight


PAIRINGS = (
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
)

RESULT_ORDER = (
    "lancelot",
    "arthur",
    "mordred",
    "red_knight",
)


def build_army(knights_config: dict) -> Dict[str, Knight]:
    return {
        knight_key: Knight.from_config(config)
        for knight_key, config in knights_config.items()
    }


def prepare_army(knights: Dict[str, Knight]) -> None:
    for knight in knights.values():
        knight.prepare_for_battle()


def fight(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.take_damage_from(second_knight)
    second_knight.take_damage_from(first_knight)


def get_battle_results(knights: Dict[str, Knight]) -> Dict[str, int]:
    return {
        knights[knight_key].name: knights[knight_key].hp
        for knight_key in RESULT_ORDER
    }


def run_battle(knights_config: dict) -> Dict[str, int]:
    knights = build_army(knights_config)

    prepare_army(knights)

    for first_knight_key, second_knight_key in PAIRINGS:
        fight(
            knights[first_knight_key],
            knights[second_knight_key],
        )

    return get_battle_results(knights)
