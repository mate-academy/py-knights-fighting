from typing import Dict
from app.knight import Knight


def create_knights(config: Dict[str, dict]) -> Dict[str, Knight]:
    knights = {}
    for key, data in config.items():
        knights[key] = Knight(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data.get("potion")
        )
    return knights


def battle(knights_dict: Dict[str, dict]) -> Dict[str, int]:
    knights = create_knights(knights_dict)

    for knight in knights.values():
        knight.prepare_for_battle()

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    results = {}
    for first_knight, second_knight in battles:
        first = knights[first_knight]
        second = knights[second_knight]

        first_knight_hp = max(
            0, first.hp - (second.power - first.protection)
        )
        second_knight_hp = max(
            0, second.hp - (first.power - second.protection)
        )

        results[first.name] = first_knight_hp
        results[second.name] = second_knight_hp

    return results
